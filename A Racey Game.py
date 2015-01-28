__author__ = 'Ben'
# First lesson on PyGame from Sentdex https://www.youtube.com/watch?v=ujOTNg17LjI

import pygame

pygame.init()

# Set the size of the display
gameDisplay = pygame.display.set_mode((800,600))

# Set Window Title
pygame.display.set_caption('A bit Racey')

# Define game clock for our game
clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)
#test
pygame.quit()
quit()