__author__ = 'Ben'
# First lesson on PyGame from Sentdex https://www.youtube.com/watch?v=ujOTNg17LjI

import pygame
import time

pygame.init()

# Window resolution
display_width = 800
display_height = 600

# Color definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_width = 73

# Set the size of the display
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Set Window Title
pygame.display.set_caption('A bit Racey')

# Define game clock for our game
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

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
        car(x,y)
        # Check to see if car collides with the edge of the screen
        if x > display_width - car_width or x < 0:
            crash()
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()