__author__ = 'A pen is a pen'

from threading import Thread
import random
from time import sleep

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

class MouseSimulation: #This class gon get purged.
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
