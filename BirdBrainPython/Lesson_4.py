from BirdBrain import Finch #Import Finch class from BirdBrain library
import time
from time import sleep

bird = Finch()

def exercise1():
    bird.setMotors(-50,-75)
    sleep(1)
    bird.stop()

def exercise2():
    rightSpeed = input("How fast should the right wheel go?")
    speedRight = int(rightSpeed)
    leftSpeed = input("How fast should the left wheel go?")
    speedLeft = int(leftSpeed)
    bird.setMotors(speedLeft, speedRight)
    sleep(1)
    bird.stop()

def exercise3():
    bird.setMotors(10, 10)
    sleep(2)
    bird.setMotors(65, 5)
    sleep(2)
    bird.setMotors(20, 20)
    sleep(1)
    bird.setMotors(5, 65)
    sleep(2)
    bird.setMotors(10, 10)
    sleep(1)
    bird.stop()

def exercise4():
    color = input("Please enter a letter: ")
    if (color == 'p'):
        bird.setBeak(0, 100, 0)
    else:
        print('Looks like thats not it...')
    sleep(1)
    bird.stopAll()

def exercise5():
    direction = input("l or r: ")
    if (direction == 'r'):
        bird.setMotors(0, 20)
    else:
        bird.setMotors(20, 0)
    sleep(1)
    bird.stopAll()

def exercise6():
    userResponse = input("please enter a speed (-100 to 100): ")
    speed = int(userResponse)
    if (speed >= -100) and (speed <= 100):
        bird.setMotors(speed, speed)
        sleep(1)
        bird.stop()
    else:
        print("that speed is not valid!")
    

def exercise7():
    userResponse = input("please enter a speed (-50 to 50): ")
    speed = int(userResponse)
    if (speed >= -50) and (speed <= 50):
        bird.setMotors(speed, speed * 2)
        sleep(5)
        bird.stop()
    else:
        print("that speed is not valid!")

def exercise8():
    danceType = input("which dance, 1 or 2: ")
    dance = int(danceType)
    if (dance == 1):
        bird.setMove('F', 10, 50)
        bird.setBeak(100, 0, 0)
        sleep(0.5)
        bird.setMove('B', 30, 60)
        bird.setBeak(0, 100, 0)
        sleep(0.5)
        bird.setTurn('R', 360, 75)
        bird.setBeak(0, 0, 100)
        sleep(0.5)
        bird.setTurn('L', 360, 100)
        bird.setBeak(100, 0, 100)
        bird.stopAll()
    else:
        bird.setTurn('R', 180, 75)
        bird.setTail(1, 100, 100, 0)
        sleep(0.5)
        bird.setTurn('L', 180, 75)
        bird.setTail(4, 0, 100, 100)
        sleep(0.5)
        bird.stopAll()
        
exercise8()

