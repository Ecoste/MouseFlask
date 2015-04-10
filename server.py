__author__ = 'A pen is a pen'

from flask.ext.cors import CORS
from flask import Flask, g, session, sessions, request
import os
import uuid
import db_manager

app = Flask(__name__)
app.config.from_pyfile("config.ini", silent=False)
app.secret_key = os.urandom(24)
CORS(app, resources=r'/*', allow_headers='Content-Type')

@app.route('/receiveData/<int:uid>=<int:index>', methods=['GET'])
def sendData(uid = 0, index = 0):
    return db_manager.getData(index)

@app.route('/sendData/<path:data>', methods=['POST'])
def receiveData(data):
    db_manager.put(data)
    return "Done"

@app.route('/receiveUID', methods=['GET'])
def sendUID():
    return str(session['uid'])

@app.before_request
def before_request():
    if 'uid' not in session:
        session['uid'] = int(str(uuid.uuid4().int)[:10]) #This might be a little too much. Is it?

@app.teardown_request
def teardown_request(exception):
    pass

if __name__ == '__main__':
    app.run(port=80, debug = False, threaded = True)
    #app.run(host='0.0.0.0', port=80)