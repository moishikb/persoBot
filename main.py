from flask import Flask
from flask_socketio import SocketIO, send
from dll.chatBI import get_message

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

