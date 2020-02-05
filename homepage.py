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

pygame.display.set_caption("Homepage")

dead = False

clock = pygame.time.Clock()
background_image = pygame.image.load("background1.gif").convert()

menu = True



while menu:
    screen.blit(background_image, [0, 0])
    start_button = pygame.draw.rect(screen, (0, 0, 240), (150, 90, 100, 50))
    continue_button = pygame.draw.rect(screen, (0, 244, 0), (150, 160, 100, 50))
    quit_button = pygame.draw.rect(screen, (244, 0, 0), (150, 230, 100, 50))

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