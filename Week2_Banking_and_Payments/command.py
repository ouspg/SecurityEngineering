"""
Subdomain Takeover Allocator

Allocates ips for servers from an IPv4 network to simply simulate a hosting provider ip allocation.
Allocation is done by iterating all values in the network and mapping them to a host provider "app"
subdomain as "app" instances. A subdomain takeover is simulated by randomly assigning one ip as the
target and then giving that ip another route in Traefik when it is assigned.
"""
from ipaddress import IPv4Network
from os import urandom
from random import choice, seed
from secrets import token_urlsafe
from threading import Lock

from fastapi import FastAPI, Response, Request, Query

seed(int.from_bytes(
    urandom(64),
    byteorder='big',
    signed=False,
))


class Network:
    """Iterate an ipv4 block as strings
    """

    def __init__(self, network: str):
        self._network = IPv4Network(network)
        self._set_iter()

    def _get_iter(self):
        return iter(map(str, self._network))

    def _set_iter(self):
        self._iter = self._get_iter()

    @property
    def values(self):
        return [*self._get_iter()]

    def __next__(self):
        try:
            return next(self._iter)
        except StopIteration:
            self._set_iter()
            return next(self)

    def __iter__(self):
        return self


class Target:
    """Imaginary target domain information
    """

    def __init__(self, network: Network):
        self.domain = choice([
            'rss',
            'bss',
            'mail',
            'feed',
            'check',
            'quest',
        ])
        self.ip = choice(network.values[3:-3])


class Servers:
    """Allocated servers store

    Maximum size is set via the size param.
    """

    def __init__(self, size: int, network: Network):
        self._net = network
        self._size = size
        self._ips = set()
        self._lock = Lock()

    def add(self) -> str:
        with self._lock:
            if len(self._ips) < self._size:
                ip = next(self._net)
                while ip in self._ips:
                    ip = next(self._net)
                self._ips.add(ip)
                return ip

    def remove(self, ip: str):
        with self._lock:
            if ip in self._ips:
                self._ips.remove(ip)
                return True

    @property
    def ips(self):
        with self._lock:
            return [*self._ips]


class ProxyConfig:
    """Traefik HTTP config provider helper

    This adds "server ips" as routers with a corresponding service to Traefik.
    All servers are added to the hosting provider "*.app.hosting-provider.org" subdomains.

    If a server ip matches the provided target another route is added to the target domain.
    """

    def __init__(self, target: Target):
        self.target = target
        self._routers = {
            self.target.ip: {
                'rule': f'Host(`{self.target.domain}.bank.ouspg.org.localhost`)',
                'service': 'mock',
            },
        }
        self._services = {
            'mock': {
                'loadBalancer': {
                    'servers': [
                        {
                            'url': 'http://command/mock',
                        },
                    ],
                },
            },
        }
        self._config = {
            'http': {
                'routers': self._routers,
                'services': self._services,
            }
        }

    def add_server(self, server_ip: str):
        token = token_urlsafe(64)
        self._routers[token] = {
            'rule': f'Host(`{server_ip}.apps.hosting-provider.org.localhost`)',
            'service': token,
        }
        self._services[token] = {
            'loadBalancer': {
                'servers': [
                    {
                        'url': 'http://user/',
                    },
                ],
            },
        }
        if server_ip == self.target.ip:
            self._routers[self.target.ip]['service'] = token

    @property
    def config(self):
        return self._config


class Application:
    """Conifg store
    """

    def __init__(self):
        self.network = Network('185.20.15.0/27')
        self.target = Target(self.network)
        self.servers = Servers(5, self.network)

    @property
    def config(self):
        cfg = ProxyConfig(self.target)
        for sip in self.servers.ips:
            cfg.add_server(sip)
        return cfg.config


data = Application()
"""Creates a "random" target
"""

app = FastAPI(
    openapi_url=None,
    redoc_url=None,
    docs_url=None,
)


@app.on_event('startup')
def start():
    import logging
    logging.getLogger('uvicorn.error').info(f'Target: {data.target.ip} {data.target.domain}')


@app.get('/targets')
def get_service_urls():
    return data.config


@app.get('/')
def get_mock(request: Request):
    return Response(
        status_code=402,
        headers={
            'Location': f'{request.base_url.scheme}://hosting-provider.org.localhost:{request.base_url.port}'
        }
    )


@app.get('/servers', status_code=302)
def servers():
    return {
        'servers': data.servers.ips
    }


@app.post('/servers')
def provision(request: Request):
    ip = data.servers.add()
    if ip:
        return Response(
            status_code=201,
            headers={
                'Server-Ip': ip,
                'Location': str(request.base_url.replace(
                    hostname=f'{ip}.app.{request.base_url.hostname}',
                    path='',
                ))
            }
        )
    else:
        return Response(status_code=429)


@app.delete('/servers')
def deallocate(ip: str = Query(...)):
    return Response(
        status_code=204 if data.servers.remove(ip) else 404,
    )


@app.get('/servers/docs')
def docs():
    from textwrap import dedent
    response = Response(
        status_code=200,
        content=dedent(
            # language=html
            """
            <html lang='en'>
            <head>
                <title>Hosting Provider</title>
                <style>
                    .common {
                        display: flex; 
                        flex-direction: column;
                        justify-items: start;
                        justify-content: start;
                        font-family: monospace;
                    }
                    .header {
                        background: lightblue;
                        padding: 1vh; 
                    }
                    .body {
                        margin: 1vh auto auto;
                        background: white;
                    }
                    .actions-grid {
                        width: 100%;
                        height: 100%;
                        display: grid;
                        grid-template-columns: 1fr 1fr 1fr;
                        grid-template-rows: 1fr;
                    }
                    .actions-panel {
                        width: 100%;
                        height: 100%;
                        display: grid;
                        grid-template-columns: 1fr;
                        grid-template-rows: 1fr auto;
                        justify-content: stretch;
                        justify-items: stretch;
                    }
                </style>
                <script type='application/javascript'>
                    const baseUrl = '/servers'
                    function viewServers() {
                        window.fetch(
                            baseUrl,
                            {
                                method: 'GET',
                            }
                        )
                        .then(r => r.json())
                        .then(
                            txt => {
                                document.getElementById('server-display').value = JSON.stringify(txt, undefined, 4)
                            }
                        )
                    }
                    function allocateServer() {
                        window.fetch(
                            baseUrl,
                            {
                                method: 'POST',
                                redirect: 'manual',
                            }
                        )
                        .then(
                            r => {
                                const c = document.getElementById('server-allocate')
                                c.value = '' + c.value + '\\n' + r.headers.get('Server-Ip')
                            } 
                        )
                    }
                    function deleteServer() {
                        document.getElementById('server-delete').value
                        .split('\\n')
                        .forEach(ip => {
                            window.fetch(
                                baseUrl + '?ip=' + ip,
                                {
                                    method: 'DELETE',
                                }
                            ).then(_ => {
                                document.getElementById('server-delete').value = ''
                            })
                        })
                    }
                </script>
            </head>
            <header class='common header'>
            <h1>Hosting Provider API Gateway (Beta)</h1>
            </header>
            <body style='background: gray'>
            <div class='common body' style='height: 88vh'>
                <div class='actions-grid'>
                    <div class='common actions-panel'>
                        <textarea id='server-display'></textarea>
                        <button onclick='viewServers()'>Query Servers</button>
                    </div>
                    <div class='common actions-panel'>
                        <textarea id='server-allocate'></textarea>
                        <button onclick='allocateServer()'>Allocate a Server</button>
                    </div>
                    <div class='common actions-panel'>
                        <textarea id='server-delete'></textarea>
                        <button onclick='deleteServer()'>Delete a Server</button>
                    </div>
                </div>
            </div>
            </body>
            </html>
            """
        ).encode('utf-8'),
        media_type='text/html',
    )
    return response
