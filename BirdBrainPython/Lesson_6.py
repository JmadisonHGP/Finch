from BirdBrain import Finch #Import Finch class from BirdBrain library
import time
from time import sleep

bird = Finch()

def exercise1():
    userName = input("What is your name?")
    bird.print("Hi" + userName)
    sleep(10)

def exercise2():
    bird.setPoint(1, 1, 1)
    bird.setPoint(1, 5, 1)
    bird.setPoint(5, 1, 1)
    bird.setPoint(5, 5, 1)
    sleep(1)
    bird.stopAll()

def exercise3():
    for x in range(6):
        bird.setMove('F', 7, 100)
        bird.setMove('B', 7, 100)

def exercise4():
    for i in range(5):
        bird.setPoint(i+1, i+1, 1)
        sleep(.5)
    bird.stopAll()

def exercise5():
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

def hourglass6():
    bird.setDisplay([1, 1, 1, 1, 1,
                     0, 1, 0, 1, 0,
                     0, 0, 1, 0, 0,
                     0, 1, 0, 1, 0,
                     1, 1, 1, 1, 1])
    sleep(0.4)
    bird.stopAll()
    
def hourglass7():
    bird.setDisplay([1, 0, 0, 0, 1,
                     1, 1, 0, 1, 1,
                     1, 0, 1, 0, 1,
                     1, 1, 0, 1, 1,
                     1, 0, 0, 0, 1])
    sleep(0.4)
    bird.stopAll()
    
def exercise7():
    for i in range(10):
        hourglass6()
        hourglass7()

def exercise8():
    userAmount = input("How many sides?")
    sideAmount = int(userAmount)
    for i in range(sideAmount):
        bird.print()
        bird.setMove('F', 15, 40)
        bird.setTurn('R', 360 / sideAmount, 40)
        
exercise8()

