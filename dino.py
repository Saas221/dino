import pygame
from pygame import *

#variaveis da tela
t_x = 600
t_y = 400
#variáveis do player
p_x = 30
p_y = 30


pygame.init()
screen = pygame.display.set_mode((t_x, t_y))
clock = pygame.time.Clock()
running = True


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, (255,0,0),((t_x/2)-(p_x/2), (t_y/2)-(p_y/2), 20,20))
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p_y += 10
    if keys[pygame.K_s]:
        p_y -= 10
    if keys[pygame.K_a]:
        p_x += 10
    if keys[pygame.K_d]:
        p_x -= 10
    
    pygame.display.flip()
    screen.fill("black")

