
#imports
from pygame import *
from button import *
from play_page import *


#intialisers
pygame.init()
pygame.font.init()


def home_menu(screen):

    #creating button instances
    play_button = button('Play', 30, 350, True, screen)
    leader_board_button = button('Leader Board', 200, 350, True, screen)
    shop_button = button('Shop', 370, 350, True, screen)
    login_button = button('Login', 540, 350, True, screen)
    tutorial_button = button('Tutorial', 710, 350, True, screen)
    setting_button = button('Settings', 710, 50, True, screen)

    #drawing options
    
    play_button.draw()
    leader_board_button.draw()
    shop_button.draw()
    login_button.draw()
    tutorial_button.draw()
    setting_button.draw()

    if play_button.check_click():
        play_menu(screen)
    
    
    
