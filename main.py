import socket
from flask import Flask
from flask_socketio import SocketIO, send


def show_my_ip():
    return socket.gethostbyname(socket.gethostname())

def show_my_hostname():
    return socket.gethostname()

def whatsup():
    return "I'm doing great!, what about you?"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('message')
def handleMessage(msg):
    if 'how are you' in msg:
        msg = whatsup()
    if 'ip' in msg or 'IP' in msg:
        msg = 'Your IP: ' + show_my_ip()
    if 'machine name' in msg:
        msg = 'Your  host name: ' + show_my_hostname()
    print('Message: '+ msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)

