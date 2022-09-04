'''
constants for the game.
modify the following however you wish
'''

# the screen is divided to a squares grid
GRID_SIZE = (30, 30)

# screen size
SCREEN_SIZE = (600, 600)

# the title of the window
WINDOW_TITLE = "pygame pacman"

# frame per seconds
FPS = 30

##########################
# DO NOT TOUCH FROM HERE #
##########################

# the size of a single square (derived from screen and grid sizes)
SQUARE_SIZE = SCREEN_SIZE[0] / GRID_SIZE[0] , SCREEN_SIZE[1] / GRID_SIZE[1]

