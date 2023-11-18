def movimentacao(p_y):
    if p_y >= 276:
        p_y = 276
        gravidade = 0
        jumping = False
    elif p_y < 200 and p_y:
        gravidade = 3
        jumping = True
    elif p_y < 220:
        gravidade = 9
        jumping = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        p_y -= pulo
    
    p_y += gravidade
    return p_y




import pygame
from pygame import *

#variaveis da tela
t_x = 600
t_y = 400
#variáveis do player
p_x = 100
p_y = 276
#outras variáveis
pulo = 20
gravidade = 3

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
