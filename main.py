
#imports
import pygame
from home_page import *
from button import *
from play_page import *


#intialisers
pygame.init()
pygame.font.init()


#display details
WIDTH = 900
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH,HEIGHT])
fps = 20
timer= pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 40)
pygame.display.set_caption('POkeR')


#drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


#colours
DARK_GREEN = (1, 50, 32)


#main game loop
run = True
home_button_value = True


while run:
    screen.fill(DARK_GREEN)
    timer.tick(fps)


    #writing main title
    draw_text("poker", font, 'black', 400, 150)
    home_menu(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.flip()

pygame.quit()
