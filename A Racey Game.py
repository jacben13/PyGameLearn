__author__ = 'Ben'
# First lesson on PyGame from Sentdex https://www.youtube.com/watch?v=ujOTNg17LjI

import pygame
import time
import random

pygame.init()

# Window resolution
display_width = 800
display_height = 600

# Color definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

car_width = 73

# Set the size of the display
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Set Window Title
pygame.display.set_caption('A bit Racey')

# Define game clock for our game
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

def obstacles_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged ' + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def obstacle(obstaclex, obstacley, obstaclew, obstacleh, color):
    pygame.draw.rect(gameDisplay, color, [obstaclex, obstacley, obstaclew, obstacleh])

# Helper function to blit the car image
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def crash():
    message_display('You Crashed!')

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    textSurf, textRect = text_objects(text, largeText)
    textRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textSurf, textRect)

    pygame.display.update()
    time.sleep(2)

    game_loop()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    dodged = 0

    obstacle_startx = random.randrange(0, display_width)
    obstacle_starty = -600
    obstacle_speed = 7
    obstacle_width = 100
    obstacle_height = 100

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if not x_change == 5:
                        x_change = 0
                if event.key == pygame.K_RIGHT:
                    if not x_change == -5:
                        x_change = 0

        x += x_change

        gameDisplay.fill(white)
        obstacle(obstacle_startx, obstacle_starty, obstacle_width, obstacle_height, blue)
        obstacle_starty += obstacle_speed
        car(x,y)
        obstacles_dodged(dodged)
        # Check to see if car collides with the edge of the screen
        if x > display_width - car_width or x < 0:
            crash()

        # Check to see if the block has passed us
        if obstacle_starty > display_height:
            obstacle_starty = 0 - obstacle_height
            obstacle_startx = random.randrange(0, display_width)
            dodged += 1

        if y < obstacle_starty + obstacle_height:
            if x > obstacle_startx and x < obstacle_startx + obstacle_width or x + car_width > obstacle_startx and x + \
                    car_width < obstacle_startx + obstacle_width:
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()