__author__ = 'A pen is a pen'

import sqlite3
from contextlib import closing
import sys

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

Points = []
db = None

def init():
    global db
    with closing(connect()) as db:
        with open('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def connect():
    return sqlite3.connect("C:\\Users\\A pen is a pen\\PycharmProjects\\Flasky\\db\\mouse_data.db")

def close():
    if db is not None:
        db.close()

def getData(index):
    return "C".join([str(Points[i]) for i in range(index, len(Points))]) + "C{}".format(len(Points))

def put(data):
    def m(point):
        Points.append(Point(*list(map(int, point.split(","))))) #This might be a little too much. Is it?

    list(map(m, data.split("C")))

def connectionWrapper(func):
    def func_wrapper(*args):
        db = connect()
        cur = db.cursor()
        func(cur, *args)
        close()
    return func_wrapper

@connectionWrapper
def putIntoDatabase(cur, data):
    def m(point):
        cur.execute("INSERT INTO points (x, y) VALUES({},{});".format(*point.split(",")))

    list(map(m, data.split("C")))

init()

'''Maybe this is better?
    if uid is not 0 and index is not 0:
        pass
    elif uid is not 0 and index is 0:
        pass
    elif uid is 0 and index is not 0:
        pass
    elif uid is 0 and index is 0:
        pass
    '''
    #cur = g.db.cursor()
    #cur.execute("SELECT x, y FROM points{};".format(uid and " WHERE uid = {}".format(uid) or ""))
    #values = cur.fetchall()
    #return "C".join([str(Point(*values[i])) for i in range(index, len(values))])  + "C{}".format(len(values)) #pointCpointCpointCpoint...pointCindex
'''
#Tbh I have no idea if the recursive or normal one is better. I think the normal one is way easier to understand, but that might be because I've never written a recursive function before this one.
@app.route('/sendData/<path:data>', methods=['POST'])
def receiveData(data):
    return "Derp"
    cur = g.db.cursor()
    cur.execute("INSERT INTO points (uid, x, y) VALUES({}, {},{});".format(session['uid'] ,*data.split("C",1)[0].split(","))) #Apparently, this is slow. Like, really slow.
    g.db.commit()
    print("Received data.")
    if data.count("C") == 0:
        return "Done"
    else:
        return receiveData(data.split("C",1)[1])
'''