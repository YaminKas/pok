
import pygame
pygame.init()
pygame.font.init()

font = pygame.font.Font("freesansbold.ttf", 18)

class button():
    def __init__(self, text, x_pos, y_pos, enabled, screen):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.clicked = False
        self.screen = screen


    def draw(self):
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(150,40 )) 
        if self.enabled == True:
            if self.check_click() == True:
                pygame.draw.rect(self.screen, 'dark grey', button_rect, 0 ,5)
            else:
                pygame.draw.rect(self.screen, 'light grey', button_rect, 0 ,5)
        else:
            pygame.draw.rect(self.screen, 'black', button_rect, 0 ,5)
        pygame.draw.rect(self.screen, 'black', button_rect, 2 ,5)
        self.screen.blit(button_text, (self.x_pos+5, self.y_pos+5))

    def check_click(self):
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 25))

        if left_click and button_rect.collidepoint((pygame.mouse.get_pos())) and self.enabled: #and not self.clicked:
            self.clicked = True
            return True
        elif not left_click:
            self.clicked = False
        return False
