__author__ = 'Ben'
# First lesson on PyGame from Sentdex https://www.youtube.com/watch?v=ujOTNg17LjI

import pygame

pygame.init()

# Window resolution
display_width = 800
display_height = 600

# Color definitions
black = (0, 0, 0)
white = (255, 255, 255)

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

x = (display_width * 0.45)
y = (display_height * 0.8)

x_change = 0

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

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
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()