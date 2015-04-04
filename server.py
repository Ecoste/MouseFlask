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

@app.route('/')
def index():
    return '<head><title>Ecoste!</title><head><body>Hai.</body>'

@app.route('/test')
def test():
    return '<head><title>Test</title><head><body>This page is exclusively for dangerous tests only. ALSO YOU HAVE BEEN INFECTED GET FUCKED. <br> <img src="http://i.imgur.com/iFSpenr.gif" alt="Mountain View"></body>'


@app.route('/mouseCoord/<index>')
def mouse_coords(index):
    ret = ""
    points = mouse_simulation.mouse_coords

    for x in range(int(index), len(points)):
        ret += "C" + str(points[x].x) + "," + str(points[x].y)

    ret += "C" + str(len(points))
    return ret

class MouseSimulation: #Should this be creating a thread within itself instead of the user doing it themselves?
    def __init__(self,startX, startY, mouse_speed = 3, simulation_speed = 0.1):
        self.x = startX
        self.y = startY
        self.mouse_speed = mouse_speed
        self.simulation_speed = simulation_speed
        self._kill = False
        self.mouse_coords = [] #Mouse Simulation, not Simulator. That's why we keep track of and have an .update() function so it goes in real time.
                               #But, maybe a Mouse Simulator with getNextCoords or something would've been better. Maybe not.
                               #I don't know, pretty specific task so I think this is okay.

        self.thread = Thread(target = self.update) #Do we even need to save the thread?
        self.thread.start()                        #Thread(target = self.update).start() and add return thread funtction with threading.current_thread()

    def update(self): #Skips the starting point. But for some reason I don't like setting the random after appending the point or adding an if.
        while True:
            if self._kill == True:
                break

            self.x += random.randint(-self.mouse_speed,self.mouse_speed)
            self.y += random.randint(-self.mouse_speed,self.mouse_speed)

            t = Point(self.x, self.y)
            self.mouse_coords.append(t)
            sleep(self.simulation_speed)

    def destroy(self):
        self._kill = True

if __name__ == '__main__':
    mouse_simulation = MouseSimulation(1600 / 2, 900 / 2)

    #app.run(port=80)
    app.run(host='0.0.0.0', port=80)