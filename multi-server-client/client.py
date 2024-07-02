import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")
    sio.emit('message', 'Client is connected!')

@sio.event
def message(data):
    print(data)
    while True:
        guess = input('Enter your guess: ')
        sio.emit('guess', guess)

@sio.event
def response(data):
    print(data)
    if data == 'Correct! You guessed the number.':
        sio.disconnect()

@sio.event
def disconnect():
    print("I'm disconnected!")

if __name__ == '__main__':
    sio.connect('http://127.0.0.1:8080')
    sio.wait()
