import pygame
from random import randint
from variables import *
# 
def fire_rockets(bullets, enemy):
    for bullet in bullets:
        bullet.x += ROCKET_SPEED
        if pygame.Rect.colliderect(bullet,enemy):
            pygame.event.post(pygame.event.Event(ENEMY_HIT))
            enemy.x = WIDTH
            enemy.y = randint(25,HEIGHT-25)