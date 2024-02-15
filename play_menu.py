
#imports
from pygame import *
from button import *

#intialisers
pygame.init()
pygame.font.init()

def play_menu(screen):
    
    #creating button instances
    new_game_button = button('New Game', 30, 150, True, screen)
    load_game_button = button('Load Game', 200, 150, True, screen)

    #drawing buttons
    new_game_button.draw()
    load_game_button.draw()
