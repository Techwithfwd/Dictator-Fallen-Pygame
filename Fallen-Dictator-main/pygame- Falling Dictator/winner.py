import pygame
from variables import *
from time import *
def winner(text):
    draw_text = WINNER_FONT.render(text,1,RED)
    screen.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2,HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)