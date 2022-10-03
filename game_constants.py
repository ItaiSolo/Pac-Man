'''
constants for the game.
modify the following however you wish
'''
#Colors
Blue = (0,0,255)

# the screen is divided to a squares grid
GRID_SIZE = (30, 30)
GRID_SIZE_Val = 30

# screen size
SCREEN_SIZE = (600, 600)
SCREEN_SIZE_Val = 600

# the title of the window
WINDOW_TITLE = "pygame pacman"

#last line colum or row
Last = (600/GRID_SIZE_Val) + 9 #29

# frame per seconds
FPS = 120

##########################
# DO NOT TOUCH FROM HERE #
##########################

# the size of a single square (derived from screen and grid sizes)
SQUARE_SIZE = SCREEN_SIZE[0] / GRID_SIZE[0] , SCREEN_SIZE[1] / GRID_SIZE[1]

