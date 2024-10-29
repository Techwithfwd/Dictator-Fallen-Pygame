import pygame
import os
import sys
from variables import *
from draw import *
from enemy_move import *
from shoot import *
from movement import *
from winner import *
pygame.init()
# 
def main():
    ship = pygame.Rect(50,(HEIGHT//2-25), 50,50)
    enemy = pygame.Rect((WIDTH//2),(HEIGHT//2-25), 50,50)
    bullets = []
    score = 0
    health = 3
    run = True
    clock = pygame.time.Clock()
    while run and score < 10:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(ship.x, (ship.y + ship.height//2 - 2), 15, 5)
                    bullets.append(bullet)
            if event.type == ENEMY_HIT:
                score += 1
        winner_text = ''
        if score == 10:
            winner_text = 'You defeated the Dictator!'
            if winner != '':
                winner(winner_text)
    
        keys_pressed = pygame.key.get_pressed()
        enemy_move(enemy)
        fire_rockets(bullets, enemy)
        ship_movements(keys_pressed, ship, enemy, health)
        draw_window(ship, bullets, enemy, score, health)

    pygame.display.update()
    main()

if __name__ in '__main__':
    main() 
