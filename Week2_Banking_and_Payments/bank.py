import os
from base64 import b32hexencode
from hashlib import sha256
from json import loads, dumps
from logging import getLogger
from textwrap import dedent

from fastapi import FastAPI, Cookie, Request
from fastapi.responses import HTMLResponse, Response
from pydantic import BaseModel, Field
from redis import Redis


class Account(BaseModel):
    balance: float = 0.0


class User(BaseModel):
    username: str
    password: str
    account: Account = Field(default_factory=Account)


class Transfer(BaseModel):
    to: str
    amount: float


def to_token(user: User):
    return b32hexencode(sha256(user.password.encode('utf-8')).digest()).decode('utf-8')


def set_user(token: str, user: User):
    storage.set(token, user.username)
    storage.set(user.username, dumps(user.dict()))


def set_user_by_name(user: User):
    storage.set(user.username, dumps(user.dict()))


def get_user(token: str):
    return User(**loads(storage.get(storage.get(token))))


def get_user_by_name(username: str):
    return User(**loads(storage.get(username)))


def session_response(token: str, request: Request):
    response = Response(
        status_code=201,
        headers={
            'Location': str(request.base_url.replace(path='/')),
        },
    )
    response.set_cookie(
        session_cookie_name,
        token,
        domain=request.base_url.hostname,
    )
    return response


class Site:
    login_snippet = dedent(
        # language=html
        """
        <div style='
            display: grid;
            grid-template-columns: 1fr;
            grid-gap: .5vh;
            justify-items: start;
            align-items: center;
            font-family: monospace;
            margin: 10%;
        '>
            <label style='justify-self: stretch;'>Username
                <input type='text' id='username' style='width: 100%;'>
            </label>
            <label style='justify-self: stretch;'>Password
                <input type='password' id='password' style='width: 100%;'>
            </label>
            <input type='button' style='
                justify-self: stretch;
                align-self: center;
            ' value='Login' onclick='login()'/>
        </div>
        """
    )

    register_snippet = dedent(
        # language=html
        """
        <div style='
            display: grid;
            grid-template-columns: 1fr;
            grid-gap: .5vh;
            justify-items: start;
            align-items: center;
            font-family: monospace;
            margin: 10%;
        '>
            <label style='justify-self: stretch;'>Username
                <input type='text' id='username' style='width: 100%;'>
            </label>
            <label style='justify-self: stretch;'>Password
                <input type='password' id='password' style='width: 100%;'>
            </label>
            <input type='button' style='
                justify-self: stretch;
                align-self: center;
            ' value='Register' onclick='register()'/>
        </div>
        """
    )

    choice_snippet = dedent(
        # language=html
        """
        <div style='
            display: grid;
            grid-template-columns: 1fr;
            grid-gap: .5vh;
            justify-items: start;
            align-items: center;
            font-family: monospace;
        '>
            <input type='button' style='
                justify-self: stretch;
                align-self: center;
            ' value='Login' onclick='window.location.assign("/login")'/>
            <input type='button' style='
                justify-self: stretch;
                align-self: center;
            ' value='Register' onclick='window.location.assign("/register")'/>
        </div>
        """
    )

    welcome_snippet = dedent(
        # language=html
        """
        <div style='
            display: grid;
            grid-template-columns: 1fr;
            grid-gap: .5vh;
            justify-items: start;
            align-items: center;
            font-family: monospace;
        '>
            <p>Welcome: {username}</p>
            <p>Balance: {balance:.2f}</p>
            <input type='button' value='logout' onclick='logout()'/>
            <br>
            <p>Send Money</p>
            <label>Amount
                <input type='number' id='amount'>
            </label>
            <label>To
                <input type='text' id='to'>
            </label>
            <input type='button' value='Send' onclick='{onclick}'>
        </div>
        """
    )

    site = dedent(
        # language=html
        """
        <html lang="en">
        <head>
            <title>Bank</title>
            <script type='application/javascript'>
                const analyticsData = {
                    count: 0,
                    users: [],
                }
                function updateCounters() {
                    fetchAnalytics().finally(() => {
                        document.getElementById('count').textContent = analyticsData.count.toString() + ' ' + analyticsData.users.join(',')
                    })
                }
                function subD(domain) {
                    return window.location.toString().replace('://', '://' + domain + '.').replace(/^(.+\/)[^/]+$/, '$1')
                }
                function fetchAnalytics() {
                    return window.fetch(
                        subD('analytics'),
                        {
                            method: 'GET',
                            mode: 'cors',
                        }
                    ).then(async r => {
                        const json = await r.json()
                        if ( json.users ) {
                            analyticsData.users = json.users
                            analyticsData.count = json.users.length
                        }
                     })
                }
                function sendData(event, data) {
                    // TODO: Send customer info to all subservices
                    [
                        'analytics',
                        'rss',
                        'bss',
                        'mail',
                        'feed',
                        'check',
                        'quest',
                    ].forEach(
                        s => {
                            window.fetch(
                                subD(s),
                                {
                                    method: 'POST',
                                    mode: 'cors',
                                    
                                    headers: {
                                        'Content-Type': 'application/json',
                                    },
                                    body: JSON.stringify({
                                        event: event,
                                        data: {...data, password: undefined},
                                    })
                                },
                            )
                        }
                    )
                }
                function logreg(url) {
                    const username = document.getElementById('username')
                    const password = document.getElementById('password')
                    const user = {
                        username: username.value,
                        password: password.value,
                    }
                    window.fetch(
                        url,
                        {
                            method: 'POST',
                            body: JSON.stringify(user),
                            headers: {'Content-Type': 'application/json'},
                        }
                    ).then(r => {
                        if ( r.ok ) {
                            sendData(url.replace('/', ''), user)
                            window.location.assign('/')
                        } else {
                            username.style.background = 'red'
                            password.style.background = 'red'
                        }
                    })
                }
                function login() {
                    logreg('/login')
                }
                function register() {
                    logreg('/register')
                }
                function logout() {
                    window.fetch(
                        '/logout',
                        {
                            method: 'DELETE',
                        }
                    ).then(_ => {
                        sendData('logout', {username: '{username}'})
                        window.setTimeout(() => window.location.assign('/'), 200)
                    })
                }
                window.onload = () => {
                    updateCounters()
                    window.setInterval(updateCounters, 15000)
                }
            </script>
        </head>
        <header>
            <div style='display: flow; margin-left: 1vw'>
                <p style='display: inline; font-family: monospace;'>Users online: </p>
                <p id='count' style='display: inline; font-family: monospace;'></p>
            </div>
        </header>
        <body style='background: gray'>
        <div style='
            width: 98vw;
            height: 98vh; 
            margin: auto;
            background: white;
            display: grid; 
            grid-template-rows: 1fr;
            grid-template-columns: 1fr;
            justify-items: center;
            align-items: center;
        '>
            <div style='
                width: 20%;
                height: 20%;
                background: lightblue;
                display: grid;
                grid-template-columns: 1fr;
                grid-template-rows: 1fr;
                justify-items: center;
                align-items: center;
            '>
                {snippet}
            </div>
        </div>
        </body>
        </html>
        """
    )

    @property
    def login(self):
        return self.site.replace('{snippet}', self.login_snippet)

    @property
    def register(self):
        return self.site.replace('{snippet}', self.register_snippet)

    @property
    def choice(self):
        return self.site.replace('{snippet}', self.choice_snippet)

    def welcome(self, user: User):
        return self.site.replace('{snippet}', self.welcome_snippet.format(
            username=user.username,
            balance=user.account.balance,
            onclick=dedent(
                # language=javascript
                """
                (() => {
                const amount = document.getElementById("amount")
                const to = document.getElementById("to")
                amount.disabled = true
                to.disabled = true
                window.fetch(
                    "/send",
                    {
                        method: "POST",
                        mode: "cors",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            to: to.value,
                            amount: amount.value,
                        })
                    }
                ).finally(() => {
                    window.location.reload()
                })
            })()
                """
            )
        )).replace('{username}', user.username)


site = Site()
app = FastAPI()
base_url = os.getenv('BASE_URL')
storage = Redis(host='redis', port=6379)
session_cookie_name = 'bank-session'
session_cookie = Cookie('', alias=session_cookie_name)


@app.on_event('startup')
def startup():
    getLogger('uvicorn.error').info(f'Visit: http://{base_url}:8080')


@app.get('/', response_class=HTMLResponse)
def home(session: str = session_cookie):
    if session and storage.exists(session):
        user = get_user(session)
        return HTMLResponse(site.welcome(user))
    else:
        return HTMLResponse(site.choice)


@app.get('/login')
def login():
    return HTMLResponse(site.login)


@app.get('/register')
def register():
    return HTMLResponse(site.register)


@app.post('/login')
def login_user(user: User, request: Request):
    token = to_token(user)
    if storage.exists(token):
        return session_response(token, request)
    else:
        return Response(status_code=403)


@app.post('/register')
def register_user(user: User, request: Request):
    token = to_token(user)
    user.account.balance = 10
    if not storage.exists(token):
        set_user(token, user)
        return session_response(token, request)
    else:
        return Response(status_code=409)


@app.delete('/logout')
def logout_user(session: str = session_cookie):
    if session:
        response = Response(status_code=204)
        response.delete_cookie(session_cookie_name, domain=base_url)
        return response
    else:
        return Response(status_code=401)


@app.post('/send')
def send_money(transfer: Transfer, session: str = session_cookie):
    if session and storage.exists(session):
        user = get_user(session)
        if transfer.to and storage.exists(transfer.to):
            to_user = get_user_by_name(transfer.to)
        else:
            return Response(status_code=404)
        if user.account.balance < transfer.amount:
            return Response(status_code=400)
        else:
            user.account.balance -= transfer.amount
            to_user.account.balance += transfer.amount
        set_user(session, user)
        set_user_by_name(to_user)
    else:
        return Response(status_code=401)
