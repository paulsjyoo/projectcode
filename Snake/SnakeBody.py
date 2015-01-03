#Import pygame module
import pygame
from pygame.locals import *

#Initialize pygame module, required before any time pygame is used
pygame.init()

#SnakeBody Class
#Class is made using pygame sprite to allow for collision checks and image loading
#Constructor takes in parameters
#x : size of snake body length in pixels
#y : size of snake body width in pixels
class SnakeBody(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #Create pygame sprite object
        pygame.sprite.Sprite.__init__(self)
        #Load an image to use as snake body
        self.image = pygame.image.load('snakebox.png')

        #Set snake body's length and width size from parameters
        self.snakeSizeX = x
        self.snakeSizeY = y

        #Test
        #self.image = pygame.Surface((self.snakeSizeX, self.snakeSizeY))
        #self.image.fill(snakeColor)

        #Get the rect property from image loaded
        #All pygame sprites must have a rect property
        #rect holds the x and y coordinates of the image's top left corner
        #It also holds the length and width of the objects
        self.rect = self.image.get_rect()
        #0 Index of rect is the image's x coordinate, defaulted at a position where it can't be seen
        self.rect[0] = -100
        #1 Index of rect is the image's y coordinate, defaulted at a position where it can't be seen
        self.rect[1] = -100

    #Mutator method that change's snake body's x and y position
    def move(self, x, y):
        self.rect[0] = x
        self.rect[1] = y

    #Accessor method that gets x position of body
    def getXPos(self):
        return self.rect[0]

    #Accessor method that gets y position of body
    def getYPos(self):
        return self.rect[1]

    #Mutator method for changing color of body
    def changeColor(self, colorObj):
        self.image.fill(colorObj)

    #To String Method
    def __str__(self):
        return ('Snake Body is currently at position (%i, %i)' %
                (self.getXPos(), self.getYPos()))

##def main():
##    snakeBody = SnakeBody(25,25)
##    snakeBody.move(50,50)
##    print(snakeBody)
    
