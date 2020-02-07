import tkinter
import pygame

class Background:
    pygame.init()

    def __init__(self, window_width, window_height, animation_increment, clock_rate):
        self.window_width = window_width
        self.window_height = window_height
        self.animation_increment = animation_increment
        self.clock_rate = clock_rate
        self.size = (window_width, window_height)
        self.screen = pygame.display.set_mode(self.size)

    def homepagebg(self):
        pygame.display.set_caption("Homepage")
        dead = False
        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("background1.gif").convert()
        menu = True

        while menu:
            self.screen.blit(background_image, [0, 0])
            race = pygame.draw.rect(self.screen, (255, 255, 255), (20, 20, 100, 40))
            flying = pygame.draw.rect(self.screen, (255, 255, 255), (150, 20, 100, 40))
            jumping = pygame.draw.rect(self.screen, (255, 255, 255), (280, 20, 100, 40))
            help = pygame.draw.rect(self.screen, (207, 185, 151), (420, 20, 50, 40))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Click race button
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    if mouse_x > 20 and mouse_x < 120 and mouse_y > 20 and mouse_y < 60:
                        self.racetrackbg()
                    elif mouse_x > 150 and mouse_x < 250 and mouse_y > 20 and mouse_y < 60:
                        self.flyingbg()
                    elif mouse_x > 280 and mouse_x < 380 and mouse_y > 20 and mouse_y < 60:
                        self.jumpingbg()
                if event.type == pygame.QUIT:
                    menu = False

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

        while (dead == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True

            self.screen.blit(background_image, [0, 0])

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

    def racetrackbg(self):
        pygame.display.set_caption("Race")
        dead = False

        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("ground1.jpg").convert()
        menu = True

        while menu:
            self.screen.blit(background_image, [0, 0])
            start = pygame.draw.rect(self.screen, (255, 255, 255), (20, 20, 100, 40))

            for event in pygame.event.get():
                print(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos() >= (150, 230):
                        if pygame.mouse.get_pos() <= (250, 280):
                            pygame.quit()

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

        while (dead == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True

            self.screen.blit(background_image, [0, 0])

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

    def jumpingbg(self):
        pygame.display.set_caption("Jump Practice")
        dead = False

        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("haunted.png").convert()
        menu = True

        while menu:
            self.screen.blit(background_image, [0, 0])
            start = pygame.draw.rect(self.screen, (255, 255, 255), (20, 20, 100, 40))

            for event in pygame.event.get():
                print(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos() >= (150, 230):
                        if pygame.mouse.get_pos() <= (250, 280):
                            pygame.quit()

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

        while (dead == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True

            self.screen.blit(background_image, [0, 0])

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

    def flyingbg(self):
        pygame.display.set_caption("Flying Practice")
        dead = False

        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("sky2.png").convert()
        menu = True

        while menu:
            self.screen.blit(background_image, [0, 0])
            start = pygame.draw.rect(self.screen, (255, 255, 255), (20, 20, 100, 40))

            for event in pygame.event.get():
                print(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos() >= (150, 230):
                        if pygame.mouse.get_pos() <= (250, 280):
                            pygame.quit()

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

        while (dead == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True

            self.screen.blit(background_image, [0, 0])

            pygame.display.flip()
            self.clock.tick(self.clock_rate)