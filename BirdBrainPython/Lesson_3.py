from BirdBrain import Finch #Import Finch class from BirdBrain library
import time
from time import sleep

bird = Finch()


def exercise1():
    bird.setBeak(255, 0, 255)
    sleep(1)
    bird.setBeak(0, 0, 0)

def exercise2():
    bird.setBeak(100, 0, 100)
    sleep(1)
    bird.setBeak(0, 100, 100)
    sleep(1)
    bird.setBeak(100, 100, 0)
    sleep(1)

def exercise3():
    bird.setTail(1, 0, 0, 100)
    bird.setTail(4, 0, 0, 100)
    sleep(2)
    bird.stopAll()

def exercise4():
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

def exercise5():
    userResponse = input("Which tail light (1-4) should be red?")
    number = int(userResponse)
    bird.setTail(number, 100, 0, 0)
    sleep(1)
    bird.stopAll()

def exercise6():
    userResponseRed = input("How much red?")
    numberRed = int(userResponseRed)
    userResponseBlue = input("How much blue?")
    numberBlue = int(userResponseBlue)
    userResponseGreen = input("How much green")
    numberGreen = int(userResponseGreen)
    bird.setTail(4, numberRed, numberGreen, numberBlue)
    sleep(4)
    bird.stopAll()
    

def stop():
    bird.stopAll()

exercise6()
