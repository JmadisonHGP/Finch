from BirdBrain import Finch #Import Finch class from BirdBrain library
import time
from time import sleep

bird = Finch()

def exercise1(): # Ask the user for their name. The program should then display “Hi” and then the user’s name
    userName = input("What is your name?")
    bird.print("Hi" + userName)
    sleep(10)

def exercise2(): # turn on the LEDs at the corners of the micro:bit display for one second  
    bird.setPoint(1, 1, 1)
    bird.setPoint(1, 5, 1)
    bird.setPoint(5, 1, 1)
    bird.setPoint(5, 5, 1)
    sleep(1)
    bird.stopAll()

def exercise3(): # Use a for loop to make the Finch move forward and backward six times.
    for x in range(6):
        bird.setMove('F', 7, 100)
        bird.setMove('B', 7, 100)

def exercise4(): # make a diagonal line across the microbit using loops
    for i in range(5):
        bird.setPoint(i+1, i+1, 1)
        sleep(.5)
    bird.stopAll()

def exercise5(): # Write a program that gradually draws a square on the micro:bit display.
    for i in range(2):
        bird.setPoint(i+1, 1, 1)
        sleep(0.3)
    for x in range(2):
        bird.setPoint(x+1, x+1, 1)
        sleep(0.3)
    for y in range(2):
        bird.setPoint(1, x+1, 1)
        sleep(0.3)
    bird.stopAll()

def hourglass6(): # make an hourglass design
    bird.setDisplay([1, 1, 1, 1, 1,
                     0, 1, 0, 1, 0,
                     0, 0, 1, 0, 0,
                     0, 1, 0, 1, 0,
                     1, 1, 1, 1, 1])
    sleep(0.4)
    bird.stopAll()
    
def hourglass7(): # make a sideways hourglass
    bird.setDisplay([1, 0, 0, 0, 1,
                     1, 1, 0, 1, 1,
                     1, 0, 1, 0, 1,
                     1, 1, 0, 1, 1,
                     1, 0, 0, 0, 1])
    sleep(0.4)
    bird.stopAll()
    
def exercise7(): # use hourglass6 & 7 to create a rotating hourglass animation
    for i in range(10):
        hourglass6()
        hourglass7()

def exercise8(): # Write a program to make the Finch move in a triangle, pentagon, or other shape
    userAmount = input("How many sides?")
    sideAmount = int(userAmount)
    for i in range(sideAmount):
        bird.print()
        bird.setMove('F', 15, 40)
        bird.setTurn('R', 360 / sideAmount, 40)
        
exercise8()

