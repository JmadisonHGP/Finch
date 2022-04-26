from BirdBrain import Finch #Import Finch class from BirdBrain library
import time
from time import sleep

bird = Finch()


def exercise1(): # set the color of the beak for 1 second, and then turn it off
    bird.setBeak(255, 0, 255)
    sleep(1)
    bird.setBeak(0, 0, 0)

def exercise2(): # flash the beak 3 different colors for 1 second each
    bird.setBeak(100, 0, 100)
    sleep(1)
    bird.setBeak(0, 100, 100)
    sleep(1)
    bird.setBeak(100, 100, 0)
    sleep(1)

def exercise3(): # set the tail lights in 2 ports for 2 seconds
    bird.setTail(1, 0, 0, 100)
    bird.setTail(4, 0, 0, 100)
    sleep(2)
    bird.stopAll()

def exercise4(): # change the color of the beak and tail lights 3 times each for 0.5 seconds, and repeat 3 times
    for x in range(3):
        bird.setBeak(100, 0, 0)
        sleep(0.5)
        bird.setTail(1, 0, 100, 0)
        sleep(0.5)
        bird.setBeak(0, 0, 100)
        sleep(0.5)
        bird.setTail(1, 100, 0, 0)
        sleep(0.5)
        bird.setBeak(0, 100, 0)
        sleep(0.5)
        bird.setTail(1, 0, 0, 100)
        sleep(0.5)

def exercise5(): # ask the user which tail light should be red, and set it to the inputed integer for 1 second
    userResponse = input("Which tail light (1-4) should be red?")
    number = int(userResponse)
    bird.setTail(number, 100, 0, 0)
    sleep(1)
    bird.stopAll()

def exercise6(): # Set port 4 to the combination of red, green, and blue decided by the user
    userResponseRed = input("How much red?")
    numberRed = int(userResponseRed)
    userResponseBlue = input("How much blue?")
    numberBlue = int(userResponseBlue)
    userResponseGreen = input("How much green")
    numberGreen = int(userResponseGreen)
    bird.setTail(4, numberRed, numberGreen, numberBlue)
    sleep(4)
    bird.stopAll()

def exercise7(): # Write a program that moves the Finch in a square. The user should choose the side length of the square, and the Finch tail should be a different color for each side of the square.
    userResponseLength = input("How long are the sides?")
    sideLength = int(userResponseLength)
    bird.setMove('F', sideLength, 70)
    bird.setTail(1, 100, 0, 0)
    bird.setTurn('R', 90, 70)
    bird.setMove('F', sideLength, 70)
    bird.setTail(2, 100, 100, 0)
    bird.setTurn('R', 90, 70)
    bird.setMove('F', sideLength, 70)
    bird.setTail(3, 100, 100, 100)
    bird.setTurn('R', 90, 70)
    bird.setMove('F', sideLength, 70)
    bird.setTail(4, 0, 100, 100)
    bird.setTurn('R', 90, 70)
    bird.stopAll()

def stop(): # i was testing something here
    bird.stopAll()

exercise7()
