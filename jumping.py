import tkinter
import pygame

# background
pygame.init()

window_width = 500
window_height = 300

animation_increment = 10
clock_rate = 60

size = (window_width, window_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Homepage")

dead = False

clock = pygame.time.Clock()
background_image = pygame.image.load("haunted.png").convert()

while (dead == False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_rate)

menu = True