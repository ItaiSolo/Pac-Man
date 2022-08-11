import pygame
  
# Form screen with 1200x900 size
# and with resizable
screen = pygame.display.set_mode((1200, 900), 
                                 pygame.RESIZABLE)
  
# title
pygame.display.set_caption('PAC - MAN')
  
# run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
# quit pygame after closing window
pygame.quit()