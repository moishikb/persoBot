from flask import Flask,render_template
import socket

application = Flask(__name__)


@application.route('/')
def show_machine_list():
    return render_template('index.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')


@application.route("/execute", methods=['GET'])
def execute():
    try:
        hostip = socket.gethostbyname(socket.gethostname())
        return render_template('index.html', ip=hostip)
    except Exception, e:
        print 'Error is ' + str(e)
        return jsonify(status='ERROR',message=str(e))