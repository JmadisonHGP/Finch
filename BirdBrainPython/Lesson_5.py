from BirdBrain import Finch #Import Finch class from BirdBrain library
import time
from time import sleep

bird = Finch()

def exercise1(): # If button A or B is pressed set the beak green
    if bird.getButton('A'):
        bird.setBeak(0, 100, 0)
    if bird.getButton('B'):
        bird.setBeak(0, 100, 0)
    else:
        bird.setBeak(100, 0, 0)
    sleep(1)
    bird.stopAll()

def exercise2(): # Write a program that moves the Finch backward if button B is pressed. Otherwise, the Finch should move forward. 
    if bird.getButton('B'):
        bird.setMove('B', 10, 25)
    else:
        bird.setMove('F', 10, 25)

def exercise3(): # Print the distance, and if it's less than 30 cm then display green. If else, red
    print(bird.getDistance())
    if bird.getDistance() < 30:
        bird.setTail("all", 0, 0, 100)
    else:
        bird.setTail("all", 100, 0, 0)
    sleep(2)
    bird.stopAll()

def exercise4(): # Write a program that moves the Finch forward if it does not sense an obstacle. If the Finch does see an obstacle, it should move backward.
    print(bird.getDistance())
    move = bird.getDistance()
    if bird.getDistance() > 25:
        bird.setMove('F', move, 50)
    else: bird.setMove('B', 15, 50)
    bird.stopAll()

def exercise5(): # while the distance is less than 30 display red; if bigger then set green
    while bird.getDistance() < 30:
        bird.setBeak(100, 0, 0)
    bird.setBeak(0, 100, 0)
    sleep(1)
    bird.stopAll()

def exercise6(): # Write a program to make the Finch move forward until it is close to an obstacle.
    while bird.getDistance() > 20:
        bird.setMove('F', 10, 25)
    bird.stopAll()

def exercise7(): # while the distance is greater than 20, set all lights to blue for 3 seconds, then purple for 3 seconds
    while bird.getDistance() > 20:
        bird.setTail("all", 0, 0, 100)
        sleep(3)
        bird.setTail("all", 100, 0, 100)
        sleep(3)
    bird.stopAll()

def printDistance():
    print(bird.getDistance())

def exercise8(): # Use the finch as a security system. If the finch sees and obsticle less than 10 cm away display red. If the obstacle is further, blink the lights a multitude of colors
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

def exercise9(): # while A is not pressed, blink the tail green. 
    while not bird.getButton('A'):
        bird.setTail(1, 0, 100, 0)
        sleep(0.1)
        bird.setTail(3, 0, 100, 0)
        sleep(0.1)
        bird.stopAll()
        sleep(0.1)

def exercise10(): # Write a program that moves the Finch back and forth until you press button B.
    while not bird.getButton('B'):
        bird.setMove('F', 10, 10)
        bird.setMove('B', 10, 10)
    bird.setBeak(0, 100, 0)
    bird.stopAll()

def exercise11(): # set the beak red. while distance is less than 30, keep the light red.
    bird.setBeak(100, 0, 0)
    while bird.getDistance() < 30:
        pass
    bird.setBeak(0, 100, 0)
    sleep(1)
    bird.stopAll()

def exercise12(): # make your Finch avoid obstacles: If there is an obstacle in front of the Finch, it should back up and turn. When there is no obstacle, the Finch should move forward.
    while not bird.getButton('A'):
        if (bird.getDistance() > 30):
            bird.setTail("all", 0, 100, 0)
        else:
            bird.setTail("all", 100, 0, 0)
    bird.stopAll()

exercise12()
