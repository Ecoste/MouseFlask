__author__ = 'A pen is a pen'

from flask.ext.cors import CORS
from flask import Flask
from time import sleep
from threading import Thread
import random

app = Flask(__name__)
CORS(app, resources=r'/*', allow_headers='Content-Type') #

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

@app.route('/')
def index():
    return '<head><title>Ecoste!</title><head><body>Hai.</body>'

@app.route('/test')
def test():
    return '<head><title>Test</title><head><body>This page is exclusively for dangerous tests only. ALSO YOU HAVE BEEN INFECTED GET FUCKED. <br> <img src="http://i.imgur.com/iFSpenr.gif" alt="Mountain View"></body>'


@app.route('/mouseCoord/<index>')
def mouse_coords(index): #pointCpointCpointC...Cindex
    return "C".join([str(mouse_simulation.mouse_points[i]) for i in range(int(index), len(mouse_simulation.mouse_points))]) \
        + "C" + str(len(mouse_simulation.mouse_points))

class MouseSimulation:
    def __init__(self, startX, startY, mouse_speed = 3, simulation_speed = 0.1):
        self.mouse_pos = Point(startX, startY)
        self.mouse_speed = mouse_speed
        self.simulation_speed = simulation_speed
        self._kill = False
        self.mouse_points = []

        self.thread = Thread(target = self.update)
        self.thread.start()

    def update(self):
        while not self._kill:
            self.mouse_points.append(self.mouse_pos)
            self.mouse_pos += Point(*[random.randint(-self.mouse_speed, self.mouse_speed) for _ in range(2)])

            sleep(self.simulation_speed)

    def destroy(self):
        self._kill = True

if __name__ == '__main__':
    mouse_simulation = MouseSimulation(1600 / 2, 900 / 2)

    #app.run(port=80)
    app.run(host='0.0.0.0', port=80)