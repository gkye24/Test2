import tkinter
import pygame

#background
pygame.init()

window_width=500
window_height=300

animation_increment=10
clock_rate = 20

size=(window_width, window_height)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("Homepage")

dead = False

clock = pygame.time.Clock()
background_image = pygame.image.load("background1.gif").convert()

while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_rate)

class Homepage(tkinter.Frame):
    def __init__(self, master, jump, fly, racetrack, call_on_next):
        super(Homepage, self).__init__(master)

        self.jump = jump
        self.fly = fly
        self.racetrack = racetrack

        self.call_on_selected = call_on_next

        self.create_widgets()
        self.grid()

    def create_widgets(self):

