from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
from dll.chatBI import get_message, add_new_fac_to_knowledge

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/<name>')
def index(name):
    if name:
        return render_template('index.html', name=name)
    else:
        return render_template('index.html', name='My friend')


@app.route('/')
@app.route('/index.html')
def index2():
        return render_template('index.html', name='My friend')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/howto.html')
def howto():
    return render_template('howto.html')


@app.route('/teach.html')
def teach():
    return render_template('teach.html', reses='')


@app.route('/simple', methods=['GET', 'POST'])
def simple():
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']
        add_new_fac_to_knowledge(question, answer)
        return render_template('teach.html', reses='Done')
    return render_template('teach.html', reses='')


@socketio.on('message')
def handleMessage(msg):
    results = get_message(msg)
    print('Message: '+ results)
    send(results, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)

