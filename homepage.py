import tkinter
import pygame

# background
pygame.init()

window_width = 500
window_height = 300

animation_increment = 10
clock_rate = 20

size = (window_width, window_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Homepage").

dead = False

clock = pygame.time.Clock()
background_image = pygame.image.load("background1.gif").convert()

menu = True

while menu:
    screen.blit(background_image, [0, 0])
    race = pygame.draw.rect(screen, (255, 255, 255), (20, 20, 100, 40))
    running = pygame.draw.rect(screen, (255, 255, 255), (150, 20, 100, 40))
    jumping = pygame.draw.rect(screen, (255, 255, 255), (280, 20, 100, 40))
    help = pygame.draw.rect(screen, (207, 185, 151), (420, 20, 50, 40))

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (150, 230):
                if pygame.mouse.get_pos() <= (250, 280):
                    pygame.quit()

    pygame.display.flip()
    clock.tick(clock_rate)

while (dead == False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_rate)