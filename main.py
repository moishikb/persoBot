import os
import socket
from flask import Flask
from flask_socketio import SocketIO, send


def show_my_ip():
    return socket.gethostbyname(socket.gethostname())

def show_my_hostname():
    return socket.gethostname()

def whatsup():
    return "I'm doing great!, what about you?"

def run_command(msg):
    command = str(msg).replace('run:', '')
    os.system(command)
    return 'Done, dude'


def get_message(msg):
    if 'run:' in msg:
        msg = run_command(msg)
    if 'thanks' in msg:
        msg = 'You\'re welcome!!'
    if 'how are you' in msg:
        msg = whatsup()
    if 'ip' in msg or 'IP' in msg:
        msg = 'Your IP: ' + show_my_ip()
    if 'machine name' in msg:
        msg = 'Your  host name: ' + show_my_hostname()
    return msg


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('message')
def handleMessage(msg):
    results = get_message(msg)
    print('Message: '+ results)
    send(results, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)

