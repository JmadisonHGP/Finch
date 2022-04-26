from BirdBrain import Finch #Import Finch class from BirdBrain library
import time

bird = Finch() #Creates an object of type Finch

#_______Lesson 1 start_______

def exercise1(): #Moving the Finch back and forth
    bird.setMove('F', 10, 70)
    bird.setMove('B', 10, 10)
    bird.setMove('F', 10, 70)
    bird.setMove('B', 25, 10)

def exercise2(): #Rotating the Finch
    bird.setTurn('R', 90, 30)

def exercise3(): #Rotating the Finch 360 degrees both ways
    bird.setTurn('R', 360, 50)
    bird.setTurn('L', 360, 20)

def exercise4(): #Having the Finch make a square using Move and Turn commands
    bird.setMove('F', 50, 30)
    bird.setTurn('L', 90, 30)
    bird.setMove('F', 50, 30)
    bird.setTurn('L', 90, 30)
    bird.setMove('F', 50, 30)
    bird.setTurn('L', 90, 30)
    bird.setMove('F', 50, 30)
    bird.setTurn('L', 90, 30)

def example(): #Have the finch move away and, then have it retrace the steps
    bird.setMove('F', 85, 80)
    bird.setTurn('L', 60, 80)
    bird.setMove('F', 70, 80)
    bird.setMove('B', 85, 80)
    bird.setTurn('R', 60, 80)
    bird.setMove('B', 70, 80)

def drawstar(): #Have the Finch draw a star
    for x in range(5): #Repeat the code below 5 times
        bird.setMove('F', 10, 60)
        bird.setTurn('R', 144, 60)
    
    
    
example()
