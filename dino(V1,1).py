def movimentacao(p_y):
    if p_y >= 276:
        p_y = 276
        gravidade = 0
        jump = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jump = False
    
    
    if jump and p_y > 180:
        p_y -= 10
    return p_y

 



import pygame
from pygame import *
import random

#variaveis da tela
t_x = 600
t_y = 400
#variáveis do player
p_x = 100
p_y = 276



pygame.init()
screen = pygame.display.set_mode((t_x, t_y))
clock = pygame.time.Clock()
running = True


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dino = pygame.draw.rect(screen, (255,0,0),((p_x, p_y, 20,20)))
    chao = pygame.draw.line(screen, (0,255,0), (0,300), (600, 300), 10)
    
    p_y = movimentacao(p_y)
    pygame.display.flip()
    screen.fill("black")
pygame.quit()
