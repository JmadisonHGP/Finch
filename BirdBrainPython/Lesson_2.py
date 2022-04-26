from BirdBrain import Finch #Import Finch class from BirdBrain library
import time

bird = Finch()

def exercise1Example(): #prints the distance the finches sensors see
    print(bird.getDistance())

def exercise1(): #longest distance I got is 106 cm, shortest is 2 cm
    print("Distance: ", bird.getDistance())

def exercise2(): #if button A is pressed print true
    bird.getButton('A')
    print(bird.getButton('A'))

def exercise4(): #find the distance between the finch and obstacle, then print distance, x2 and x4
    currentDistance = bird.getDistance()
    print(currentDistance)
    print(2*currentDistance)
    print(4*currentDistance)

def exercise5(): # get both light values from each light sensor, and print the difference between the two
    leftSensor = bird.getLight('L')
    rightSensor = bird.getLight('R')
    difference = leftSensor - rightSensor
    print(difference)

def exercise6(): # get both light values and print the average value
    leftSensor = bird.getLight('L')
    rightSensor = bird.getLight('R')
    mean = leftSensor + rightSensor / 2
    print(mean)


exercise6()
