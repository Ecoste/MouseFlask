__author__ = 'A pen is a pen'

from flask.ext.cors import CORS
from flask import Flask, g, session, sessions, request
from contextlib import closing
import mouse_simulation
import sqlite3
import os
import uuid

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))

    def __str__(self):
        return "{},{}".format(self.x, self.y)

app = Flask(__name__)
app.config.from_pyfile("config.ini", silent=False)
app.secret_key = os.urandom(24)
CORS(app, resources=r'/*', allow_headers='Content-Type')

@app.route('/receiveData/' , defaults={'uid': 0, 'index' : 0}, methods=['GET'])
@app.route('/receiveData/<int:uid>=<int:index>', methods=['GET'])
def sendData(uid, index):
    cur = g.db.cursor()
    cur.execute("SELECT x, y FROM points WHERE id >= {}{};".format(index, uid and " AND uid = {}".format(uid) or ""))
    values = cur.fetchall()

    return "C".join([str(Point(*values[i])) for i in range(len(values))]) #pointCpointCpointCpoint...point

'''
@app.route('/sendData/<path:data>', methods=['POST'])
def receiveData(data): #Normal
    def h(point):
        cur.execute("INSERT INTO points (x, y) VALUES({},{});".format(*point.split(",")))
        g.db.commit()

    cur = g.db.cursor()
    map(h, data.split("C"))
    return "thx m8"
'''
#Tbh I have no idea if the recursive or normal one is better. I think the normal one is way easier to understand, but that might be because I've never written a recursive function before this one.
@app.route('/sendData/<path:data>', methods=['POST'])
def receiveData(data): #Recursive
    cur = g.db.cursor()
    cur.execute("INSERT INTO points (x, y) VALUES({},{});".format(*data.split("C",1)[0].split(",")))
    g.db.commit()

    if data.count("C") == 0:
        return "Done"
    else:
        return receiveData(data.split("C",1)[1])


@app.before_request
def before_request():
    if 'uid' not in session:
        session['uid'] = uuid.uuid4()
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    init_db()
    mouse_simulation = mouse_simulation.MouseSimulation(1600 / 2, 900 / 2)
    app.run(port=80, debug = True)
    #app.run(host='0.0.0.0', port=80)