"""
a game class to maintain the pygame stuff easily
"""

import pygame

# import all game constants
from game_constants import * 


class Game:
    """
    the game class
    """

    def __init__(self):

        # initialize pygame
        pygame.init()

        # the pygame screen surface
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        # clock to maintain fps
        self.clock = pygame.time.Clock()

        # game is running? (will be set to true when game starts running)
        self.running = False

    def event_loop(self):
        """
        look for events like key-presses, window close, etc
        """
        
        # iterate current events
        for e in pygame.event.get():

            # if window is closed
            if e.type == pygame.QUIT:
                self.running = False


    def render_stuff(self):
        """
        draw on the screen everything that needs to be drawn
        then update the screen
        """

        self.draw_on_grid(0, 0, (0xff, 0xff, 0xff))

        # update the screen
        pygame.display.update()


    def draw_on_grid(self, row, column, color):
        """
        fills a square on the screen grid.

        note:
            0 <= row < GRID_SIZE[0]
            0 <= column < GRID_SIZE[1]

            color is a tuple of rgb
        """

        rect = (row * SQUARE_SIZE[0], column * SQUARE_SIZE[1], SQUARE_SIZE[0], SQUARE_SIZE[1])
        pygame.draw.rect(self.screen, color, rect)
        
    def mainloop(self):

        self.running = True

        while self.running:

            # stick to fps
            self.clock.tick(FPS)

            # check events. might make the window close
            self.event_loop()

            # render stuff
            self.render_stuff()

