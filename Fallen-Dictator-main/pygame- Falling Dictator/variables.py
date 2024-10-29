import pygame
import os
import sys
pygame.font.init()
WIDTH = 800
HEIGHT = 400
FPS = 60
RED = (255,0,0)
BLACK = (0,0,0)
SPACE = pygame.image.load(os.path.join('images','space.png'))
SHIP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('images','spaceship.png')),(50,50))
SHIP = pygame.transform.rotate(SHIP_IMAGE, 90)
ENEMY = pygame.transform.scale(pygame.image.load(os.path.join('images','hitler.png')),(50,50))
SPEED = 10
ENEMY_SPEED = 3 
ROCKET_SPEED = 10
SCORE_FONT = pygame.font.SysFont('comicsans', 40)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
ENEMY_HIT = pygame.USEREVENT + 1
BORDER = pygame.Rect(WIDTH//2+150, 0, 10, HEIGHT)
WINNER_FONT = pygame.font.SysFont('comicsans', 50)


# 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jump Shot')