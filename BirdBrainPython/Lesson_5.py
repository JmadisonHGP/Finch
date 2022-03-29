from BirdBrain import Finch #Import Finch class from BirdBrain library
import time
from time import sleep

bird = Finch()

def exercise1():
    if bird.getButton('A'):
        bird.setBeak(0, 100, 0)
    if bird.getButton('B'):
        bird.setBeak(0, 100, 0)
    else:
        bird.setBeak(100, 0, 0)
    sleep(1)
    bird.stopAll()

def exercise2():
    if bird.getButton('B'):
        bird.setMove('B', 10, 25)
    else:
        bird.setMove('F', 10, 25)

def exercise3():
    print(bird.getDistance())
    if bird.getDistance() < 30:
        bird.setTail("all", 0, 0, 100)
    else:
        bird.setTail("all", 100, 0, 0)
    sleep(2)
    bird.stopAll()

def exercise4():
    print(bird.getDistance())
    move = bird.getDistance()
    if bird.getDistance() > 25:
        bird.setMove('F', move, 50)
    else: bird.setMove('B', 15, 50)
    bird.stopAll()

def exercise5():
    while bird.getDistance() < 30:
        bird.setBeak(100, 0, 0)
    bird.setBeak(0, 100, 0)
    sleep(1)
    bird.stopAll()

def exercise6():
    while bird.getDistance() > 20:
        bird.setMove('F', 10, 25)
    bird.stopAll()

def exercise7():
    while bird.getDistance() > 20:
        bird.setTail("all", 0, 0, 100)
        sleep(3)
        bird.setTail("all", 100, 0, 100)
        sleep(3)
    bird.stopAll()

def printDistance():
    print(bird.getDistance())

def exercise8():
    while bird.getDistance() < 10:
        bird.setTail("all", 100, 0, 0)
        bird.setBeak(100, 0, 0)
        sleep(1)
        bird.stopAll()
    bird.setTail("all", 100, 100, 0)
    bird.setBeak(100, 100, 0)
    sleep(0.7)
    bird.setTail("all", 0, 100, 100)
    bird.setBeak(0, 100, 100)
    sleep(0.7)
    bird.setTail("all", 100, 100, 50)
    bird.setBeak(100, 100, 50)
    sleep(0.7)
    bird.stopAll()

def exercise9():
    while not bird.getButton('A'):
        bird.setTail(1, 0, 100, 0)
        sleep(0.1)
        bird.setTail(3, 0, 100, 0)
        sleep(0.1)
        bird.stopAll()
        sleep(0.1)

def exercise10():
    while not bird.getButton('B'):
        bird.setMove('F', 10, 10)
        bird.setMove('B', 10, 10)
    bird.setBeak(0, 100, 0)
    bird.stopAll()

def exercise11():
    bird.setBeak(100, 0, 0)
    while bird.getDistance() < 30:
        pass
    bird.setBeak(0, 100, 0)
    sleep(1)
    bird.stopAll()

def exercise12():
    while not bird.getButton('A'):
        if (bird.getDistance() > 30):
            bird.setTail("all", 0, 100, 0)
        else:
            bird.setTail("all", 100, 0, 0)
    bird.stopAll()

exercise12()
