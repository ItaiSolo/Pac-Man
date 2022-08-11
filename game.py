import os
import pygame
  
# Form screen with 1200x900 size
# and with resizable
width = 1200
heigth = 900
fps = 120
screen = pygame.display.set_mode((1200, 900), 
                                 pygame.RESIZABLE)



def draw():
    
    pygame.display.update() 

# title
pygame.display.set_caption('PAC - MAN')
def main():
    clock = pygame.time.Clock() #delay 
    running = True
    while running: #while running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
               
    pygame.quit()
# quit pygame after closing window



if __name__ == "__main__":
    main()