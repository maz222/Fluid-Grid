# https://gamedevelopment.tutsplus.com/tutorials/make-a-neon-vector-shooter-in-xna-the-warping-grid--gamedev-9904

from Grid import Grid
from GridView import GridView
from Vector3 import TripleVector


import pygame

# pygame setup:
pygame.init()

iPhone6 = (int(1334 / 2), int(750 / 2))
iPhone6Plus = (int(1920 / 2), int(1080 / 2))

currentRes = iPhone6

screen = pygame.display.set_mode(currentRes)
# ----------------------------

# game setup:

geoGrid = Grid([0,0], currentRes[0], currentRes[1], 20, 20, .3)
# geoGrid = Grid([0,0], 300, 300, 20, 20, .28)

# print(geoGrid)

# used for keeping track of the cursor
mouse_pos = (0, 0)

done = False
clock = pygame.time.Clock()

# game loop:
while not done:
    # game logic:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            quit()
        # tracks the position of the cursor
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print("boom!")
            if event.button == 1:
                geoGrid.apply_explosive_force(100, TripleVector(mouse_pos[0], mouse_pos[1], 0), 50)
            elif event.button == 3:
                geoGrid.apply_implosive_force(100, TripleVector(mouse_pos[0], mouse_pos[1], 0), 50)

    geoGrid.update()


    # draw logic:
    screen.fill((255, 255, 255))
    GridView.draw(geoGrid, screen)

    pygame.display.flip()

    clock.tick(144)

# ------------------------------

