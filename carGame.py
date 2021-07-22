import random
import time
import pygame

pygame.init()

# Assigning Display width, height and color(using RGB codes) of the window
window_width = 800
window_height = 750
windowColor = 102, 134, 148
blackColor = 0, 0, 0

# Setting Display width and height of the window
gameWindowConfig = pygame.display.set_mode((window_width,window_height))

# the title of the window
pygame.display.set_caption("CAR GAME")

# adding clock for time calculations and interval calculations
clock = pygame.time.Clock()

# loading the car image
carImage = pygame.image.load("carImage.png")

# loading game background pictures and intro and options background
pavementBackgroundImg = pygame.image.load("pavement.jpg")
middleStripeImg = pygame.image.load("middleStripe.png")
whiteStripeImg = pygame.image.load("whiteStripe.png")

# assigning width of the car
carWidth = 260


def textObjects(message, font):
    textSurface = font.render(message, True, blackColor)
    return textSurface, textSurface.get_rect()


# function to display a message when crashed
def displayMessage(message, message2):

    # font size and font style
    text = pygame.font.SysFont('arial', 61)
    text_Surface,textrect = textObjects(message, text)
    textrect.center = ((window_width/2), ((window_height/2)-160))

    text2 = pygame.font.SysFont('arial', 88)
    text2_Surface, text2rect = textObjects(message2, text2)
    text2rect.center = ((window_width/2), (window_height/2))

    # displaying the text in the window
    gameWindowConfig.blit(text_Surface, textrect)
    gameWindowConfig.blit(text2_Surface, text2rect)
    pygame.display.update()
    # providing the sleep time or break time before restarting
    time.sleep(3)
    # restarting the game
    carGame_loop()


# defining a function for carCrash
def carCrash():
    displayMessage(" ! Y O U    C R A S H E D ! ", "G A M E   O V E R")


# function related to background
def backgroundImages():

    # entering the background images to the window using blit function

    gameWindowConfig.blit(pavementBackgroundImg, (0, 0))
    gameWindowConfig.blit(pavementBackgroundImg, (0, 200))
    gameWindowConfig.blit(pavementBackgroundImg, (0, 400))
    gameWindowConfig.blit(pavementBackgroundImg, (716, 0))
    gameWindowConfig.blit(pavementBackgroundImg, (716, 200))
    gameWindowConfig.blit(pavementBackgroundImg, (716, 400))

    gameWindowConfig.blit(middleStripeImg, (400, 0))
    gameWindowConfig.blit(middleStripeImg, (400, 100))
    gameWindowConfig.blit(middleStripeImg, (400, 200))
    gameWindowConfig.blit(middleStripeImg, (400, 300))
    gameWindowConfig.blit(middleStripeImg, (400, 400))
    gameWindowConfig.blit(middleStripeImg, (400, 500))
    gameWindowConfig.blit(middleStripeImg, (400, 600))
    gameWindowConfig.blit(middleStripeImg, (400, 700))

    gameWindowConfig.blit(whiteStripeImg, (80, 0))
    gameWindowConfig.blit(whiteStripeImg, (80, 50))
    gameWindowConfig.blit(whiteStripeImg, (80, 100))
    gameWindowConfig.blit(whiteStripeImg, (80, 150))
    gameWindowConfig.blit(whiteStripeImg, (80, 200))
    gameWindowConfig.blit(whiteStripeImg, (80, 250))
    gameWindowConfig.blit(whiteStripeImg, (80, 300))
    gameWindowConfig.blit(whiteStripeImg, (80, 350))
    gameWindowConfig.blit(whiteStripeImg, (80, 400))
    gameWindowConfig.blit(whiteStripeImg, (80, 450))
    gameWindowConfig.blit(whiteStripeImg, (80, 500))
    gameWindowConfig.blit(whiteStripeImg, (80, 550))
    gameWindowConfig.blit(whiteStripeImg, (80, 600))
    gameWindowConfig.blit(whiteStripeImg, (80, 650))
    gameWindowConfig.blit(whiteStripeImg, (80, 700))
    gameWindowConfig.blit(whiteStripeImg, (695, 0))
    gameWindowConfig.blit(whiteStripeImg, (695, 50))
    gameWindowConfig.blit(whiteStripeImg, (695, 100))
    gameWindowConfig.blit(whiteStripeImg, (695, 150))
    gameWindowConfig.blit(whiteStripeImg, (695, 200))
    gameWindowConfig.blit(whiteStripeImg, (695, 250))
    gameWindowConfig.blit(whiteStripeImg, (695, 300))
    gameWindowConfig.blit(whiteStripeImg, (695, 350))
    gameWindowConfig.blit(whiteStripeImg, (695, 400))
    gameWindowConfig.blit(whiteStripeImg, (695, 450))
    gameWindowConfig.blit(whiteStripeImg, (695, 500))
    gameWindowConfig.blit(whiteStripeImg, (695, 550))
    gameWindowConfig.blit(whiteStripeImg, (695, 600))
    gameWindowConfig.blit(whiteStripeImg, (695, 650))
    gameWindowConfig.blit(whiteStripeImg, (695, 700))


# car function
def car(x,y):
    # entering the image to the window using blit function
    gameWindowConfig.blit(carImage,(x,y))


# Creating an obstacles function and loading and adding the obstacle images to the window
def obstacles(obstacleStartingPointX, obstacleStartingPointY, obstacle):
    if obstacle == 0:
        obstacleSelect = pygame.image.load("obstacle1.png")
    elif obstacle == 1:
        obstacleSelect = pygame.image.load("obstacle1.png")
    elif obstacle == 2:
        obstacleSelect = pygame.image.load("obstacle1.png")
    elif obstacle == 3:
        obstacleSelect = pygame.image.load("obstacle1.png")
    elif obstacle == 4:
        obstacleSelect = pygame.image.load("obstacle1.png")
    elif obstacle == 5:
        obstacleSelect = pygame.image.load("obstacle1.png")
    elif obstacle == 6:
        obstacleSelect = pygame.image.load("obstacle1.png")

    gameWindowConfig.blit(obstacleSelect, (obstacleStartingPointX,obstacleStartingPointY))


# Creating a playerScoringSystem function
def playerScoringSystem(obstaclesPassed, playerScore):
    font = pygame.font.SysFont(None, 30)
    numberOfObstaclesPassed = font.render("Passed: "+str(obstaclesPassed), True, blackColor)
    scoreOfPlayer = font.render("SCORE: "+str(playerScore), True, blackColor)
    gameWindowConfig.blit(numberOfObstaclesPassed, (0, 52))
    gameWindowConfig.blit(scoreOfPlayer, (0, 25))


# Creating the game level function
def displaylevel(level):
    textLevel = pygame.font.SysFont('arial', 88)
    text_SurfaceLevel, textrectLevel = textObjects(level, textLevel)
    textrectLevel.center = ((window_width / 2), (window_height / 2))

    # displaying the text in the window
    gameWindowConfig.blit(text_SurfaceLevel, textrectLevel)
    pygame.display.update()
    time.sleep(2)


# Creating the car game function
def carGame_loop():

    # car position using x and y coordinates
    x = (window_width*0.35)
    y = (window_height*0.71)
    x_move = 0
    # speed of the obstacles moving towards the player
    ObstacleCarSpeed = 7
    obstacle = 0
    yAxisChange = 0
    obstacleStartingPointX = random.randrange(250, (window_width-250))
    obstacleStartingPointY = -800

    # height and width of obstacles
    obstacle1Width = 102
    obstacle1Height = 222

    # No. of obstacles passed
    obstaclesPassed = 0

    # Game level
    gameLevel = 1

    # Score of the player
    playerScore = 0

    # obstacle2Width = 92
    # obstacle2Height = 207
    #
    # obstacle3Width = 93
    # obstacle3Height = 183
    #
    # obstacle4Width = 90
    # obstacle4Height = 184
    #
    # obstacle5Width = 91
    # obstacle5Height = 172
    #
    # obstacle6Width = 101
    # obstacle6Height = 254
    #
    # obstacle7Width = 87
    # obstacle7Height = 174

    knocked = False
    while not knocked:

        for event in pygame.event.get():
            # to close the game
            if event.type == pygame.QUIT:
                # quiting the game and quiting
                pygame.quit()
                quit()

            # refer this link(documentation) to check the pygame keys:  https://www.pygame.org/docs/ref/key.html
            # if the any arrow key is pressed
            if event.type == pygame.KEYDOWN:

                # move the car towards left when left arrow key is pressed
                if event.key == pygame.K_LEFT:
                    x_move = -5

                # move the car towards right when right arrow key is pressed
                if event.key == pygame.K_RIGHT:
                    x_move = 5

                # to accelerate the car or increase speed of obstacles press 'w'
                if event.key == pygame.K_w:
                    ObstacleCarSpeed += 2

                # To apply brake to the car or slow down the car or slow down the obstacles press 'Space bar'
                if event.key == pygame.K_SPACE:
                    ObstacleCarSpeed -= 2

            # if any arrow key is lifted or not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0

        x = x + x_move

        # adding the window color
        gameWindowConfig.fill(windowColor)

        # calling the backgroundImages function
        backgroundImages()

        obstacleStartingPointY = obstacleStartingPointY-(ObstacleCarSpeed/4)

        # calling the obstacles function
        obstacles(obstacleStartingPointX,obstacleStartingPointY,obstacle)
        obstacleStartingPointY += ObstacleCarSpeed

        # calling the car function
        car(x, y)

        # calling the playerScoringSystem function
        playerScoringSystem(obstaclesPassed, playerScore)

        #  assigning the crashing boundaries
        if x > 800-carWidth or x < 10:
            carCrash()
        if x > window_width - (carWidth+10) or x < 10:
            carCrash()
        if obstacleStartingPointY > window_height:
            obstacleStartingPointY = 0 - obstacle1Height

            obstacleStartingPointX=random.randrange(200,(window_width-200))
            obstacle = random.randrange(0, 7)

            # calculating the score of the player and the number of obstacles passed
            obstaclesPassed = obstaclesPassed + 1
            playerScore = obstaclesPassed * 5

            # calculating the level and in each level the speed of the obstacles increases
            if int(obstaclesPassed) % 7 == 0:
                gameLevel = gameLevel + 1
                ObstacleCarSpeed = ObstacleCarSpeed + 1

                # display the level
                displaylevel("LEVEL - "+str(gameLevel))

        # Assigning the crashing boundaries on the obstacles
        if y < obstacleStartingPointY + (obstacle1Height-88):
            x1 = x -20
            statement1 = obstacleStartingPointX < x1 < obstacleStartingPointX -400+ (obstacle1Width+90)
            statement2 = obstacleStartingPointX < x1 + (carWidth-90) < obstacleStartingPointX - 50 + (obstacle1Width+90)
            if statement1 or statement2:
                carCrash()
                carGame_loop()

        pygame.display.update()
        clock.tick(60)


#  running the game loop
carGame_loop()
# quiting the game and quiting
pygame.quit()
quit()

