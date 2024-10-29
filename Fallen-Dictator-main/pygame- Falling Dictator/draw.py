import pygame
from variables import *

def draw_window(ship, bullets,enemy, score, health):
    screen.blit(SPACE,(0,0))
    pygame.draw.rect(screen,BLACK,BORDER )
    score_text = SCORE_FONT.render('SCORE: '+str(score),1,BLACK)
    screen.blit(score_text, (WIDTH-score_text.get_width()-20,10))
    health_text = HEALTH_FONT.render('HEALTH: '+str(health),1,BLACK)
    screen.blit(health_text,(0+score_text.get_width()-150,10))
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    screen.blit(ENEMY,(enemy.x,enemy.y))
    screen.blit(SHIP,(ship.x, ship.y))

    pygame.display.update()