import pygame
from pygame.locals import *
display = pygame.display.set_mode((1024,1024)) # window size is determined here
pygame.init()
character = pygame.image.load("ground.png")
background = pygame.image.load("haunted.png")
characterx = 0
charactery = 0
while True:
    display.blit(background,(0,0))
    display.blit(character,(characterx,charactery))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                characterx -= 2
            if event.key == K_d:
                characterx += 2
            if event.key == K_w:
                charactery -= 2
            if event.key == K_s:
                charactery += 2
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()