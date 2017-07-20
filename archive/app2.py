from flask import Flask, render_template
import socket
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
	
@app.route('/showmyip/')
def hello(name=None):
	myip = socket.gethostbyname(socket.gethostname())
	return render_template('index.html', name=myip)

	
if __name__ == "__main__":
    app.run(host='0.0.0.0')