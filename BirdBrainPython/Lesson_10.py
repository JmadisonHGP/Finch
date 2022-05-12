from BirdBrain import Finch #Import Finch class from BirdBrain library
import time
from time import sleep
import random #import random number generator

bird = Finch()

def exercise1():
    for i in range(4): #make a square, but after a square is made rotate 60 degrees before making the next one
        bird.setMove('F', 15, 50)
        bird.setTurn('R', 90, 50)
        bird.setTurn('L', 60, 50)

def exercise2(): #make the finch go in a circle
    for i in range(180):
        bird.setMove('F', 2, 100)
        bird.setTurn('R', 2, 100)

def selfNav(): #I wanted to experiment with navigating around without hitting any obstacles. If an obstacle is seen, readjust
    for i in range(10):
        while (bird.getDistance() > 25):
            bird.setMove('F', 20, 25)
        else:
            while (bird.getDistance() <= 25):
                bird.setMove('B', 10, 20)
                bird.setTurn('R', 45, 50)

def exercise5(): #draw 5 squares of random size in length
    length = (random.randint(5,20))
    for i in range(5):
        for i in range(4):
            bird.setMove('F', length, 100)
            bird.setTurn('R', 90, 100)
    bird.stopAll()

def exercise6(red, green, blue): #while button A isn't pressed, blink all the lights in the color determined by the user
    while not bird.getButton('A'):
        bird.setBeak(red, green, blue)
        bird.setTail("all", red, green, blue)
        sleep(0.5)
        bird.setBeak(0, 0, 0)
        bird.setTail("all", 0, 0, 0)
        sleep(0.5)

def exercise7(): #if the finch isn't level, then print false and blink all lights. If finch is level, then print true.
    while not (bird.getOrientation()) == isLevel:
        print("False")
        blinkAll(0, 100, 0)
    else:
        print("True")
        

    

bird.stopAll()
