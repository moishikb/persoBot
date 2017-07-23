from flask import Flask, render_template
from flask_socketio import SocketIO, send
from dll.chatBI import get_message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/howto.html')
def howto():
    return render_template('howto.html')


@socketio.on('message')
def handleMessage(msg):
    results = get_message(msg)
    print('Message: '+ results)
    send(results, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)

