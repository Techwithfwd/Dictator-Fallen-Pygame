import pygame
from random import randint
from variables import *

def ship_movements(keys_pressed, ship, enemy, health):
    if keys_pressed[pygame.K_UP] and ship.y > 0 +5:
        ship.y -= SPEED
    elif keys_pressed[pygame.K_DOWN] and ship.y < HEIGHT - 55:
        ship.y += SPEED
    elif keys_pressed[pygame.K_LEFT] and ship.x > 0 + 5:
        ship.x -= SPEED
    elif keys_pressed[pygame.K_RIGHT] and ship.x < BORDER.x-50:
        ship.x += SPEED
    elif ship.colliderect(enemy):
        ship.y = randint(50, 550)