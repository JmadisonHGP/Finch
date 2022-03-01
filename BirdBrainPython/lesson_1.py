from BirdBrain import Finch #Import Finch class from BirdBrain library
import time

bird = Finch() #Creates an object of type Finch

#_______Lesson 1 start_______

def exercise1():
    bird.setMove('F', 10, 70)
    bird.setMove('B', 10, 10)
    bird.setMove('F', 10, 70)
    bird.setMove('B', 25, 10)

def exercise2():
    bird.setTurn('R', 90, 30)

def exercise3():
    bird.setTurn('R', 360, 50)
    bird.setTurn('L', 360, 20)

def exercise4():
    bird.setMove('F', 50, 30)
    bird.setTurn('L', 90, 30)
    bird.setMove('F', 50, 30)
    bird.setTurn('L', 90, 30)
    bird.setMove('F', 50, 30)
    bird.setTurn('L', 90, 30)
    bird.setMove('F', 50, 30)
    bird.setTurn('L', 90, 30)

def example():
    bird.setMove('F', 85, 80)
    bird.setTurn('L', 60, 80)
    bird.setMove('F', 70, 80)
    bird.setMove('B', 85, 80)
    bird.setTurn('R', 60, 80)
    bird.setMove('B', 70, 80)

#_______Lesson 2 start_______

def exercise8Example():
    print(bird.getDistance())

def exercise8(): #longest distance I got is 106 cm, shortest is 2 cm
    print("Distance: ", bird.getDistance())

def exercise9():
    bird.getButton('A')
    print(bird.getButton('A'))
    
exercise9()