#Import pygame and other modules used
import pygame, os, sys, random
from os.path import dirname, realpath, abspath
#Import SnakeFood, Head, and Body classes for game
import SnakeFood, SnakeHead, SnakeBody
from pygame.locals import *


#Constants for the game
BACKGROUND_COLOR = pygame.Color(0,0,0)
SNAKE_COLOR = pygame.Color(125, 255, 0)
MAX_SNAKE_LENGTH = 75
STARTING_POSITION = [400,300]
WINDOW = [800,600]
SNAKE_SIZE = [25,25]

#Constants for special state of boxes
RED_BOX = 1
BLUE_BOX = 2
GREEN_BOX = 3
PURPLE_BOX = 4

#Main Game Class
class MainGame:
    #Constructor initializes background music for the game and screen
    def __init__(self):
        #Initialize pygame
        pygame.init()
        #Initialize pygame mixer for music
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        #Load background music
        self.backgroundMusic = pygame.mixer.Sound("music.ogg")

        #Create screen for displaying everything
        self.MainScreen = pygame.display.set_mode((WINDOW[0],WINDOW[1]))

        #Create pygame clock object
        self.clockObj = pygame.time.Clock()

    #Loop for the Starting Screen
    def StartScreenLoop(self):
        #Initialize count for animating
        count = 0
        #Initialize boolean for whether a credit has been added
        coinBool = False

        #Play background music infinitely
        self.backgroundMusic.play(-1)
        
        # Load images needed for start screen
        coinImage = pygame.image.load("coin.png")
        titleImage = pygame.image.load("Super-Snake.png")
        background = pygame.image.load("background.png")
        start = pygame.image.load("start.png")
        copyRights = pygame.image.load("copyright.png")
        snake = pygame.image.load("snake2bz3.png")
        creditImage = pygame.image.load("credit.png")
        creditCount0 = pygame.image.load("0.png")
        creditCount1 = pygame.image.load("1.png")

        #Create variable to hold boolean so loop can be stopped when needed
        startVar = True
        #While loop to constantly loop through the display
        while startVar:
            
            # clear the screen before drawing it again
            self.MainScreen.fill(0)
            
            #draw the screen elements by blittig using the images used before
            self.MainScreen.blit(background, (0,0))
            self.MainScreen.blit(titleImage, (WINDOW[0]*.17,WINDOW[1]*.05))
            self.MainScreen.blit(snake, (WINDOW[0]*.05,WINDOW[1]*.45))
            self.MainScreen.blit(copyRights, (WINDOW[0]*.4,WINDOW[1]*.85))
            self.MainScreen.blit(coinImage, (WINDOW[0]*.42,WINDOW[1]*.80))
            self.MainScreen.blit(creditImage, (WINDOW[0]*.44,WINDOW[1]*.75))
            
    #Makes the start button image blit for everytime the count is between 0 and 100.
    #If not, the screen wont blit the start image. This is done to in a sense,
    #animate the start button.
    #Count variable is used to keep track of the number of frames passed through the
    #While loop. 
            count = (count + 1) % 200
            if count >= 0 and count < 100:
                self.MainScreen.blit(start, (WINDOW[0]*.5, WINDOW[1]*.65))

            #Loop through the events to listen for inputs from user
            for event in pygame.event.get():
                #Events for quitting game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Event for quitting game if escape key is pressed
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                #Event that adds credit and makes a noise when space is pressed
                elif event.type == KEYDOWN and event.key == K_SPACE:
                    coinBool = True
                    selectSound = pygame.mixer.Sound("sfx.ogg")
                    selectSound.play()
                #Event that starts main game loop if coin is given and enter is pressed
                elif event.type == KEYDOWN and event.key == K_RETURN and coinBool:
                    startVar = False
                    self.MainLoop()
                    
            #because coinBool is now true, it will blit an image of 1.
            if coinBool:
                self.MainScreen.blit(creditCount1, (WINDOW[0]*.63, WINDOW[1]*.7625))
            else:
                self.MainScreen.blit(creditCount0, (WINDOW[0]*.63, WINDOW[1]*.7625))
            

    # 7 - update the screen
            pygame.display.flip()



    #Main Game Loop    
    def MainLoop(self):
        #Clear screen
        self.MainScreen.fill(0)

        #Set counter for fps to control game speed
        self.fpsCounter = 20

        #Load all the sprites
        self.loadSprites()

        #Counter for 
        self.drawCount = 0

        #List to hold values of all the x and y coordinates of the snake
        snakeCoordinates = []
        #Append in the position for all the snake parts
        for snakelength in range(MAX_SNAKE_LENGTH+1):
            snakeCoordinates.append([STARTING_POSITION[0]-(snakelength*SNAKE_SIZE[0]),STARTING_POSITION[1]])
            
        #Debug Statement
        #print(snakeCoordinates)

        #Load all the images and sounds used for the game
        self.background = pygame.image.load("back.png")
        self.eatSound = pygame.mixer.Sound('nom.ogg')
        self.powerUp = pygame.mixer.Sound('powerup.ogg')
        self.powerDown = pygame.mixer.Sound('powerdown.ogg')
        self.powerNormal = pygame.mixer.Sound('powernormal.ogg')
        self.powerInvert = pygame.mixer.Sound('powerinvert.ogg')

        #Start variable to hold boolean for stopping loop
        startVar = True

        #While loop to constantly loop through display
        while startVar:
            #Clear screen
            self.MainScreen.fill(0)

            #Blit the background before you redraw in new position
            self.MainScreen.blit(self.background, (0,0))

            #Test
            #self.background.fill(pygame.Color(random.randint(1,255), random.randint(1,255), random.randint(1,255)))

            #Constantly moves snake depending on its current direction
            #Invokes snake head class's getDirection() method
            if self.snakeHead.getDirection() ==  0:
                self.snakeHead.moveUp()
            elif self.snakeHead.getDirection() == 1:
                self.snakeHead.moveRight()
            elif self.snakeHead.getDirection() == 2:
                self.snakeHead.moveDown()
            elif self.snakeHead.getDirection() == 3:
                self.snakeHead.moveLeft()

            #Loop through events from user
            for event in pygame.event.get():
                #Quit game if x button is pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Quit game if escape key is pressed
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                #If any key is pressed
                elif event.type == KEYDOWN:
                    #Check if controls are inverted
                    if self.snakeHead.getInverted() == 0:
                        #Changes direction depending on what key is pressed: up,down,left,right
                        if (event.key == K_UP):
                            self.snakeHead.changeDirection('u')
                            #print(self.snakeHead.getDirection())
                        elif (event.key == K_RIGHT):
                            self.snakeHead.changeDirection('r')
                            #print(self.snakeHead.getDirection())
                        elif (event.key == K_DOWN):
                            self.snakeHead.changeDirection('d')
                            #print(self.snakeHead.getDirection())
                        elif (event.key == K_LEFT):
                            self.snakeHead.changeDirection('l')
                            #print(self.snakeHead.getDirection())
                    #Changes direction but inverted if snake head state is inverted
                    else:
                        if (event.key == K_UP):
                            self.snakeHead.changeDirection('d')
                            #print(self.snakeHead.getDirection())
                        elif (event.key == K_RIGHT):
                            self.snakeHead.changeDirection('l')
                            #print(self.snakeHead.getDirection())
                        elif (event.key == K_DOWN):
                            self.snakeHead.changeDirection('u')
                            #print(self.snakeHead.getDirection())
                        elif (event.key == K_LEFT):
                            self.snakeHead.changeDirection('r')
                            #print(self.snakeHead.getDirection())

            #Collision between food and snake head
            #Checks if there is a collision
            if pygame.sprite.collide_rect(self.snakeHead, self.snakeFood):
                #Plays food eating noise
                self.eatSound.play()
                #Check what kind of box was eated
                if self.snakeFood.getSpecialStatus() == BLUE_BOX:
                    #Play appropriate power noise depending on what box was eaten
                    self.powerUp.play()
                    #Blue box will lower fps, causing game to 'slow down', limited at 10 fps at minimum
                    if not self.fpsCounter == 10:
                        #Lower fps, 'game speed'
                        self.fpsCounter -= 5
                    #Check that adding 3 to length wont put it out of max snake length possible
                    if self.snakeHead.getLength() + 3 > MAX_SNAKE_LENGTH:
                        #Sets to max if it does
                        self.snakeHead.setLength(MAX_SNAKE_LENGTH)
                    #Add 3 to snake length for eating blue box otherwise
                    else:
                        self.snakeHead.addLength(3)
                    #Reset special state of snake food
                    self.snakeFood.changeSpecialStatus(0)
                #Check what kind of box was eaten
                elif self.snakeFood.getSpecialStatus() == RED_BOX:
                    #Play appropriate power noise depending on what box was eaten
                    self.powerDown.play()
                    #Check that fps counter isn't at max speed
                    if not self.fpsCounter == 40:
                        #Add 10 to speed otherwise
                        self.fpsCounter += 10
                    #If at max speed
                    if self.fpsCounter > 40:
                        #Set fps to max
                        self.fpsCounter = 40
                    #Check that snake won't go past max length possible
                    if self.snakeHead.getLength() + 2 > MAX_SNAKE_LENGTH:
                        #Set to max if it does
                        self.snakeHead.setLength(MAX_SNAKE_LENGTH)
                    #Add 2 to length otherwise
                    else:
                        self.snakeHead.addLength(2)
                    #Reset special status
                    self.snakeFood.changeSpecialStatus(0)
                #Check what kind of box was eaten
                elif self.snakeFood.getSpecialStatus() == GREEN_BOX:
                    #Play appropriate power noise depending on what box was eaten
                    self.powerNormal.play()
                    #Reset speed
                    self.fpsCounter = 20
                    #Add one to length
                    self.snakeHead.addLength()
                    #Reset inversion
                    self.snakeHead.changeInversionTo(0)
                    #Reset special status
                    self.snakeFood.changeSpecialStatus(0)
                #Check what kind of box was eaten
                elif self.snakeFood.getSpecialStatus() == PURPLE_BOX:
                    #Play appropriate power noise
                    self.powerInvert.play()
                    #Flip inversion of controls
                    self.snakeHead.changeInversion()
                    #Reset special status
                    self.snakeFood.changeSpecialStatus(0)
                    #Check that adding 4 won't put snake length past max possible
                    if self.snakeHead.getLength() + 4 > MAX_SNAKE_LENGTH:
                        #Set to max if it does go over
                        self.snakeHead.setLength(MAX_SNAKE_LENGTH)
                    #Add 4 to length otherwise
                    else:
                        self.snakeHead.addLength(4)
                #Add one to length since a normal box was eaten
                else:
                    self.snakeHead.addLength()
                #Randomly generate food somewhere else again
                self.snakeFood.placeRandom(WINDOW[0], WINDOW[1])

            #Collision between snake head and body
            #Loop through all the snake bodies currently active behind snake
            for snakeBodyLength in range(self.snakeHead.getLength()):
                #Check if they collide
                if pygame.sprite.collide_rect(self.snakeHead, self.snakeBodies[snakeBodyLength]):
                    #Stop music if they collide since game is over
                    self.backgroundMusic.stop()
                    #Play alert noise signaling game over
                    self.snakeSound = pygame.mixer.Sound('alert.ogg').play()
                    #Clear out snake head
                    self.snakeHead.changeColor(BACKGROUND_COLOR)
                    #Loop through all the snake bodies and clear them out
                    for snakebody in self.snakeBodies:
                        snakebody.changeColor(BACKGROUND_COLOR)
                    #Stop loop
                    startVar = False
                    #Start game over screen loop
                    self.GameOverLoop()

            #Check that snake head doesn't go past walls and loops around if it does move it
            if self.snakeHead.getXPos() > WINDOW[0]-SNAKE_SIZE[0]:
                self.snakeHead.move(self.snakeHead.getXPos() - WINDOW[0], self.snakeHead.getYPos())
            elif self.snakeHead.getXPos() < 0:
                self.snakeHead.move(self.snakeHead.getXPos() + WINDOW[0], self.snakeHead.getYPos())
            elif self.snakeHead.getYPos() > WINDOW[1]-SNAKE_SIZE[0]:
                self.snakeHead.move(self.snakeHead.getXPos(), self.snakeHead.getYPos() - WINDOW[1])
            elif self.snakeHead.getYPos() < 0:
                self.snakeHead.move(self.snakeHead.getXPos(), self.snakeHead.getYPos() + WINDOW[1])

            #Loop through every active snake body behind snake and move it to its new position using snakeCoordinates list
            for body in range(self.snakeHead.getLength()):
                self.snakeBodies[body].move(snakeCoordinates[body][0], snakeCoordinates[body][1])
                #self.snakeBody_Sprites[body].draw(self.MainScreen)

            #Insert snake head's new position at index 0, pushing every other coordinate back one index
            snakeCoordinates.insert(0, [self.snakeHead.getXPos(),self.snakeHead.getYPos()])
            #Pop off last position since it won't be used
            snakeCoordinates.pop()

            
            self.snakeBody_Group.draw(self.MainScreen)
            self.snakeHead_Sprite.draw(self.MainScreen)
            self.snakeFood_Sprite.draw(self.MainScreen)

            #Updates display after all the changes
            pygame.display.flip()

            #Tick clock for controlling fps
            self.clockObj.tick(self.fpsCounter)

            #Check to see if max snake length has been reached and start game win loop if it has
            if self.snakeHead.getLength() >= MAX_SNAKE_LENGTH:
                #Change start var to stop game loop
                startVar = False
                #Start game win loop
                self.GameWinLoop()

    #Game over loop
    def GameOverLoop(self):
        #Counter for animating game over image
        count = 0

        #Load images for screen
        gameOverImage = pygame.image.load('gameover.png')
        enterLeaveImage = pygame.image.load('enterleave.png')

        #Start var to hold bool for loop
        startVar = True
        #Loop through display
        while startVar:
            #Clear screen
            self.MainScreen.fill(0)
            #Blit enter leave image, it wont be animated
            self.MainScreen.blit(enterLeaveImage, (WINDOW[0]*.1,WINDOW[1]*.65))

            #Animate game over image by making it blit only every now and then causing it to 'blink'
            count = (count + 1) % 200
            if count >= 0 and count < 100:
                #Blit game over image
                self.MainScreen.blit(gameOverImage, (WINDOW[0]*.07,WINDOW[1]*.2))
            #Loop through events
            for event in pygame.event.get():
                #Quit if x is clicked
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Quit is escape is pressed
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                #Start screen loop if enter is pressed
                elif event.type == KEYDOWN and event.key == K_RETURN:
                    #Change start Var so loop stops
                    startVar = False
                    #Play noise for pressing enter
                    selectSound = pygame.mixer.Sound("sfx.ogg").play()
                    #Start Start Screen Loop
                    self.StartScreenLoop()
            #Update display
            pygame.display.flip()

    #Game Win Loop
    def GameWinLoop(self):
        #Count for animating image
        count = 0

        #Load game win image
        gameWinImage = pygame.image.load('youwin.png')

        #Start var to stop loop if needed
        startVar = True
        #Loop through display
        while startVar:
            #Clear display
            self.MainScreen.fill(0)

            #Make image blit only every now and then
            count = (count + 1) % 200
            if count >= 0 and count < 100:
                #Blit game win image
                self.MainScreen.blit(gameWinImage, (WINDOW[0]*.23,WINDOW[1]*.15))
            #Loop through events
            for event in pygame.event.get():
                #Exit game if x is clicked
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Exit game if escape is pushed
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                #Play again if enter is pressed
                elif event.type == KEYDOWN and event.key == K_RETURN:
                    #Change start Var to end loop
                    startVar = False
                    #Play sound for pressing enter
                    selectSound = pygame.mixer.Sound("sfx.ogg").play()
                    #Enter Start Screen Loop
                    self.StartScreenLoop()
            #Update display
            pygame.display.flip()
        
    #Method for loading all the sprites using pygame sprite classes SnakeHead, SnakeBody, SnakeFood
    def loadSprites(self):
        #Create SnakeHead, only need 1
        self.snakeHead = SnakeHead.SnakeHead(SNAKE_SIZE[0], SNAKE_SIZE[1],
                                             STARTING_POSITION[0], STARTING_POSITION[1])
        #Render sprite of snakeHead
        self.snakeHead_Sprite = pygame.sprite.RenderPlain((self.snakeHead))
        #Create SnakeFood, only need 1
        self.snakeFood = SnakeFood.SnakeFood(SNAKE_SIZE[0], SNAKE_SIZE[1])
        #Render sprite of snakeFood
        self.snakeFood_Sprite = pygame.sprite.RenderPlain((self.snakeFood))

        #Create empty list to hold snake bodies
        self.snakeBodies = []
        #Create empty list to hold snake body sprites
        self.snakeBody_Sprites = []
        #Create as many snake bodies as max snake length
        for body in range(MAX_SNAKE_LENGTH):
            #Append them to list
            self.snakeBodies.append(SnakeBody.SnakeBody(SNAKE_SIZE[0], SNAKE_SIZE[1]))
        #Render the sprites using the bodies
        for bodies in self.snakeBodies:
            #Append them to list
            self.snakeBody_Sprites.append(pygame.sprite.RenderPlain((bodies)))
        #Create pygame group to hold all the snake bodies
        self.snakeBody_Group = pygame.sprite.Group()
        #Loop through the bodies in snakeBodies list and add them to group
        for bodies in self.snakeBodies:
            self.snakeBody_Group.add(bodies)

def main():
    mainGame = MainGame()
    mainGame.StartScreenLoop()

main()
