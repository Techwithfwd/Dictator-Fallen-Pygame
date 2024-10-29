import pygame
from random import randint
from variables import *

def enemy_move(enemy):
    enemy.x -= ENEMY_SPEED
    if enemy.x < 0:
        enemy.x = WIDTH
        enemy.y = randint(25,HEIGHT-25)