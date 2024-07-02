import socketio
from aiohttp import web
import random

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

clients = {}

@sio.event
async def connect(sid, environ):
    print('connect ', sid)
    clients[sid] = random.randint(1, 100)
    print(f'Assigned number for {sid}: {clients[sid]}')
    await sio.emit('message', 'Welcome! Start guessing.', room=sid)

@sio.event
async def guess(sid, data):
    number = clients[sid]
    guess = int(data)
    if guess < number:
        await sio.emit('response', 'Higher', room=sid)
    elif guess > number:
        await sio.emit('response', 'Lower', room=sid)
    else:
        await sio.emit('response', 'Correct! You guessed the number.', room=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
