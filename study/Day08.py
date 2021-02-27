#定义一个类描述数字时钟

import os
from time import sleep

class Clock(object):

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        return '%02d:%02d:%02d' % \
        (self.hour, self.minute, self.second)

def run_clock():
    clock = Clock()
    while True:
        os.system('cls')
        print(clock.show())
        sleep(1)
        clock.run()

'''
run_clock()
'''

#定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法

from math import sqrt

class Distance(object):

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def destination(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt((dx ** 2) + (dy ** 2))

def point(x1, y1, m1, m2):
    p1 = Distance(x1, y1)
    p2 = Distance(x1, y1)
    p2.move(m1, m2)
    print('Point1: (%d, %d)' % (x1, y1))
    print('Point2: (%d, %d)' % (p2.x, p2.y))
    print(p2.distance_to(p1))

'''
x1 = int(input('x: '))
y1 = int(input('y: '))
m1 = int(input('movex: '))
m2 = int(input('movey: '))
point(x1,y1,m1,m2)
'''