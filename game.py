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

        # update the screen
        pygame.display.update()


    def mainloop(self):

        self.running = True

        while self.running:

            # stick to fps
            self.clock.tick(FPS)

            # check events. might make the window close
            self.event_loop()

            # render stuff
            self.render_stuff()

