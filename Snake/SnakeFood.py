#Import pygame module
import pygame, random
from pygame.locals import *

#Initialize pygame module, required before any time pygame is used
pygame.init()

#SnakeFood Class
#Class is made using pygame sprite to allow for collision checks and image loading
#Constructor takes in parameters
#x : size of food length in pixels
#y : size of food width in pixels
class SnakeFood(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #Create pygame sprite object
        pygame.sprite.Sprite.__init__(self)
        #Load an image to use as snake food
        self.image = pygame.image.load('snakebox.png')

        #Set snake food's length and width size from parameters
        self.foodX = x
        self.foodY = y

        #Variable for what kind of box the snake food is
        self.specialStatus = 0
        
        #self.image = pygame.Surface((self.foodX, self.foodY))
        #self.image.fill(foodColor)

        #Get the rect property from the image loaded
        self.rect = self.image.get_rect()
        #All pygame sprites must have a rect property
        #rect holds the x and y coordinates of the image's top left corner
        #It also holds the length and width of the objects

        #0 index of the rect is the image's x coordinate
        self.rect[0] = 100
        #1 index of the rect is the image's y coordinate
        self.rect[1] = 100

        #Debug
        #print(self.rect)

    #Method for randomized box generation, moves the box into a random spot and
    #randomly picks a special type of box
    #Takes in max screen size x and y as parameters so box isnt placed out of range
    def placeRandom(self, screenX, screenY):
        #Randomly changes type of box by switching image used and changing specialstatus variable
        if random.randint(0,5) == 1:
            self.image = pygame.image.load('snakeredbox.png')
            self.specialStatus = 1
        elif random.randint(0,5) == 2:
            self.image = pygame.image.load('snakebluebox.png')
            self.specialStatus = 2
        elif random.randint(0,10) == 3:
            self.image = pygame.image.load('snakegreenbox.png')
            self.specialStatus = 3
        elif random.randint(0,13) == 4:
            self.image = pygame.image.load('snakepurplebox.png')
            self.specialStatus = 4
        else:
            self.image = pygame.image.load('snakebox.png')

        #Moves snake food to random spot using parameters
        self.rect[0] = random.randrange(0,screenX,self.foodX)
        self.rect[1] = random.randrange(0,screenY,self.foodY)

        #Debug
        #print(self.rect)

    #Accessor method that returns what the special state of the box is as a string
    def getSpecialStatusStr(self):
        if self.specialStatus == 0:
            return 'Normal'
        elif self.specialStatus == 1:
            return 'Red'
        elif self.specialStatus == 2:
            return 'Blue'
        elif self.specialStatus == 3:
            return 'Green'
        elif self.specialStatus == 4:
            return 'Purple'

    #Accessor for food's x position
    def getXPos(self):
        return self.rect[0]

    #Accessor for food's y position
    def getYPos(self):
        return self.rect[1]
    
    #Accessor method that returns what the special state of the box is
    def getSpecialStatus(self):
        return self.specialStatus

    #Mutator method to change the special state of the box
    def changeSpecialStatus(self, status):
        self.specialStatus = status

    #To string method
    def __str__(self):
        return ('Snake Food is currently at position (%i, %i)' +\
                'and is currently %s' %
                (self.getXPos(), self.getYPos(), self.getSpecialStatusStr()))

def main():
    snakeFood = SnakeFood(30, 30)
    print(snakeFood)
##    snakeFood_Sprite = pygame.sprite.RenderPlain((snakeFood))
##    screen = pygame.display.set_mode((800,600))
##    snakeFood_Sprite.draw(screen)
##    pygame.display.flip()
##    snakeFood.placeRandom(800,600)
##    snakeFood_Sprite.draw(screen)
##    pygame.display.flip()
##
##main()
