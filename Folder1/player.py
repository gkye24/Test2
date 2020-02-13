import pygame
import sys
import os # new code below

class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','cuteduck' + str(i) + '.gif')).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()