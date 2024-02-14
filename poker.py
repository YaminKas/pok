
import pygame
pygame.init()
pygame.font.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH,HEIGHT])
fps = 20
timer= pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption('POkeR')

class button():
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()


    def draw(self):
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(150,25 )) 
        pygame.draw.rect(screen, (90, 90, 90), button_rect, 0 ,5)
        pygame.draw.rect(screen, 'black', button_rect, 2 ,5)
        screen.blit(button_text, (self.x_pos+3, self.y_pos+3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(150,25 )) 
        if left_click and button_rect.collidepoint(mouse_pos ) and self.enabled:
            return True
        else:
            return False
        

 

DARK_GREEN = (1, 50, 32)
run = True
while run:
    screen.fill(DARK_GREEN)
    timer.tick(fps)

    my_button = button('click', 10, 10 ,True)
    print(my_button.check_click())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
