#Import pygame module
import pygame
from pygame.locals import *

#Initialize pygame module, required before any time pygame is used
pygame.init()

#SnakeHead Class
#Class is made using pygame sprite to allow for collision checks and image loading
#Constructor takes in parameters
#x : size of snake length in pixels
#y : size of snake width in pixels
#snakeColor : color of snake, must be a pygame.Color object
#sx : starting x position of snake head
#sy : starting y position of snake head
class SnakeHead(pygame.sprite.Sprite):
    def __init__(self, x, y, sx, sy):
        #Create pygame sprite object
        pygame.sprite.Sprite.__init__(self)
        #Load an image to use as snake head
        #All pygame sprites must have an image property
        self.image = pygame.image.load('right.png')

        #Set snake's length and width size from parameters
        self.snakeSizeX = x
        self.snakeSizeY = y

        #self.image used for testing purposes, created a colored square instead of an image
        #self.image = pygame.Surface((self.snakeSizeX, self.snakeSizeY))
        #self.image.fill(snakeColor)

        #Get the rect property from the image loaded
        #All pygame sprites must have a rect property
        #rect holds the x and y coordinates of the image's top left corner
        #It also holds the length and width of the objects
        self.rect = self.image.get_rect()
        #0 index of rect is the image's x coordinate
        self.rect[0] = sx
        #1 index of rect is the image's y coordinate
        self.rect[1] = sy

        #Direction of snake head, default is 1 which is right
        self.direction = 1
        #Length of the snake's body parts, held in the snake head
        self.length = 0

        #Inverted variable, 0 means controls are normal, 1 means controls are inverted
        self.inverted = 0

    #Move function for snake head
    def move(self, x, y):
        #Change snake head's x and y coordinates to those given
        self.rect[0] = x
        self.rect[1] = y

    #Accessor function that returns snake's current direction
    def getDirection(self):
        return self.direction

    #Accessor function that returns snake's current direction as a string
    def getDirectionStr(self):
        if self.direction == 0:
            return 'up'
        elif self.direction == 1:
            return 'right'
        elif self.direction == 2:
            return 'down'
        elif self.direction == 3:
            return 'left'

    #Change direction function, takes in diretion to change to
    def changeDirection(self, eventKey):
        #If/elif loops that changes direction depending on the input
        #Also checks that direction doesn't change to opposite direction so snake can't go backwards
        #Also changes image used depending on the direction the snake head is facing
        if eventKey == 'u':
            if self.direction != 2:
                self.direction = 0
                self.image = pygame.image.load('up.png')
        elif eventKey == 'r':
            if self.direction != 3:
                self.direction = 1
                self.image = pygame.image.load('right.png')
        elif eventKey == 'd':
            if self.direction != 0:
                self.direction = 2
                self.image = pygame.image.load('down.png')
        elif eventKey == 'l':
            if self.direction != 1:
                self.direction = 3
                self.image = pygame.image.load('left.png')

    #Function for adding length to snake's length variable, defaults at 1 if no parameters given
    def addLength(self, slen=1):
        self.length += slen

    #Sets the length of the snake's length variable to whatever value given
    def setLength(self, slen):
        self.length = slen

    #Accessor method for getting the snake's length variable, returns self.length
    def getLength(self):
        return self.length

    #Mutator method for changing color of snake head
    def changeColor(self, color):
        self.image.fill(color)

    #Accessor method for getting the snake's current x position, returns 0 index of rect
    def getXPos(self):
        return self.rect[0]

    #Accessor method for getting the snake's current y position, returns 1 index of rect
    def getYPos(self):
        return self.rect[1]
    
    #Mutator method for moving snake up one snake size unit
    def moveUp(self):
        self.rect.move_ip(0, -self.snakeSizeY)

    #Mutator method for moving snake right one snake size unit
    def moveRight(self):
        self.rect.move_ip(self.snakeSizeX, 0)

    #Mutator method for moving snake down one snake size unit
    def moveDown(self):
        self.rect.move_ip(0, self.snakeSizeY)

    #Mutator method for moving snake left one snake size unit
    def moveLeft(self):
        self.rect.move_ip(-self.snakeSizeX, 0)

    #Mutator method for flipping inversion of controls by changing the inverted variable
    def changeInversion(self):
        #Checks what state the controls are before changing
        if self.inverted == 0:
            self.inverted = 1
        else:
            self.inverted = 0

    #Mutator method for setting inverted variable to the value given
    def changeInversionTo(self, inv):
        self.inverted = inv

    #Accessor method for getting what the inverted state of the controls is
    def getInverted(self):
        return self.inverted

    #To string method
    def __str__(self):
        return ('Snake Head is currently at position (%i, %i) +\
                facing %s and its body has length %i. +\
                Controls are currently %s inverted.' %
                (self.getXPos(), self.getYPos(), self.getDirectionStr(),
                 self.getLength(), ('not' if self.getInverted() == 0 else '')))
                

def main():
    snakeHead = SnakeHead(25,25,100,100)
    print(snakeHead)
    snakeHead_Sprite = pygame.sprite.RenderPlain((snakeHead))
    screen = pygame.display.set_mode((800,600))

    clock = pygame.time.Clock()
    while True:
        #Clear background so everything can be redrawn
        screen.fill(0)

        #Try making snakehead move constantly depending on direction value
        if snakeHead.getDirection() ==  0:
            snakeHead.moveUp()
        elif snakeHead.getDirection() == 1:
            snakeHead.moveRight()
        elif snakeHead.getDirection() == 2:
            snakeHead.moveDown()
        elif snakeHead.getDirection() == 3:
            snakeHead.moveLeft()

        #Test position returner
        print(snakeHead.getXPos())
        print(snakeHead.getYPos())

        #Test length functions
        print(snakeHead.getLength())
        print(snakeHead.addLength())

        #Test color changer function
        snakeHead.changeColor(pygame.Color(255,125,0))

        #Test move function
        snakeHead.move(300,300)
        
        #Updates where snake head is since it draws it at the end of the loop
        snakeHead_Sprite.draw(screen)
        pygame.display.flip()
        clock.tick(30)

#main()
