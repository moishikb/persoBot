import socket
from flask import Flask
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('message')
def handleMessage(msg):
    if 'ip' in msg or 'IP' in msg:
        myIp= socket.gethostbyname(socket.gethostname())
        msg = 'Your IP: '+ myIp
    if 'machine name' in msg:
        msg = socket.gethostname()
    print('Message: '+ msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)