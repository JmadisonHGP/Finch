from BirdBrain import Finch #Import Finch class from BirdBrain library
import time

bird = Finch()

def exercise1Example():
    print(bird.getDistance())

def exercise1(): #longest distance I got is 106 cm, shortest is 2 cm
    print("Distance: ", bird.getDistance())

def exercise2():
    bird.getButton('A')
    print(bird.getButton('A'))

def exercise4():
    currentDistance = bird.getDistance()
    print(currentDistance)
    print(2*currentDistance)
    print(4*currentDistance)

def exercise5():
    leftSensor = bird.getLight('L')
    rightSensor = bird.getLight('R')
    difference = leftSensor - rightSensor
    print(difference)

def exercise6():
    leftSensor = bird.getLight('L')
    rightSensor = bird.getLight('R')
    mean = leftSensor + rightSensor / 2
    print(mean)


exercise6()
