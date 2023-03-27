from fastapi import FastAPI, Response
from pydantic import BaseModel, Extra
from redis import Redis

app = FastAPI()
storage = Redis(host='redis', port=6379)


class User(BaseModel):
    username: str

    class Config:
        extra = Extra.ignore


class Event(BaseModel):
    event: str
    data: User


def add_cors(response: Response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'


@app.middleware('http')
async def cors(request, call_next):
    response = await call_next(request)
    add_cors(response)
    return response


@app.options('/')
def cors_entry():
    """Noop
    """


@app.post('/')
def post_user_logon(event: Event):
    if event.event == 'login' or event.event == 'register':
        storage.sadd('ANALYTICS::USERS', event.data.username)
    elif event.event == 'logout':
        storage.srem('ANALYTICS::USERS', event.data.username)


@app.get('/')
def get_user_count():
    return {
        'users': [*storage.smembers('ANALYTICS::USERS')]
    }
