from flask import Flask,render_template
import socket

application = Flask(__name__)
@application.route('/')
def showMachineList():
    return render_template('list.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')

	
@application.route("/execute",methods=['GET'])
def execute():
    try:
		return render_template('list2.html')
		return socket.gethostbyname(socket.gethostname())
    except Exception, e:
        print 'Error is ' + str(e)
        return jsonify(status='ERROR',message=str(e))