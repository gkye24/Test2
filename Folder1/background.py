import pygame
from pygame.locals import *
import os

pygame.mixer.init(44100, 16, 2, 4096)
pygame.init()

# background music
pygame.mixer.music.load("happymusic.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

class player(object):
    run = [pygame.image.load(os.path.join('duckresized.png'))]
    jump = [pygame.image.load(os.path.join('duckresized.png'))]
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2,
                -2, -2, -2, -3, -3, -3, -3, -3, -3,
                -3, -3, -3, -3, -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.jumping = False
        self.jumpCount = 0
        self.runCount = 0

    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount // 18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount // 6], (self.x, self.y))
            self.runCount += 1


class Background:
    pygame.init()

    def __init__(self, window_width, window_height, animation_increment, clock_rate):
        self.window_width = window_width
        self.window_height = window_height
        self.animation_increment = animation_increment
        self.clock_rate = clock_rate
        self.size = (window_width, window_height)
        self.screen = pygame.display.set_mode(self.size)
        W, H = 500, 300
        self.win = pygame.display.set_mode((W, H))
        self.bgX = 0
        self.bgX2 = self.window_width

    def redrawWindow(self):
        self.win.blit(self.racetrackbg(), (self.bgX, 0))  # draws our first bg image
        self.win.blit(self.racetrackbg(), (self.bgX2, 0))  # draws the second bg image
        pygame.display.update()  # updates the screen

    def homepagebg(self):
        pygame.display.set_caption("Homepage")
        dead = False
        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("background1.gif").convert()

        character = pygame.image.load("duckresized.png")
        character_x = 0
        character_y = 220
        vel = 5
        menu = True

        while menu:
            self.screen.blit(background_image, [0, 0])
            self.screen.blit(character, (character_x, character_y))
            race = pygame.draw.rect(self.screen, (255, 255, 255), (20, 20, 100, 40))
            flying = pygame.draw.rect(self.screen, (255, 255, 255), (150, 20, 100, 40))
            running = pygame.draw.rect(self.screen, (255, 255, 255), (280, 20, 100, 40))
            help = pygame.draw.rect(self.screen, (207, 185, 151), (420, 20, 50, 40))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    if mouse_x > 20 and mouse_x < 120 and mouse_y > 20 and mouse_y < 60:
                        self.racetrackbg()
                    elif mouse_x > 150 and mouse_x < 250 and mouse_y > 20 and mouse_y < 60:
                        self.flyingbg()
                    elif mouse_x > 280 and mouse_x < 380 and mouse_y > 20 and mouse_y < 60:
                        self.runningbg()
                    elif mouse_x > 420 and mouse_x < 470 and mouse_y > 20 and mouse_y < 60:
                        self.helpbg()

                if event.type == pygame.QUIT:
                    menu = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                character_x -= vel

            if keys[pygame.K_RIGHT]:
                character_x += vel

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(self.clock_rate)

        pygame.quit()
        exit()

        while not dead:
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
        background_image = pygame.image.load("ground2.jpg").convert()

        clock = pygame.time.Clock()

        runner = player(0, 220)
        pygame.time.set_timer(USEREVENT + 1, 500)  # Sets the timer for 0.5 seconds

        run = True
        speed = 30  # NEW

        while run:
            clock.tick(speed)
            self.bgX -= 1.4  # Move both background images back
            self.bgX2 -= 1.4

            if self.bgX < self.window_width() * -1:  # If our bg is at the -width then reset its position
                self.bgX = self.window_width()

            if self.bgX2 < self.window_width() * -1:
                self.bgX2 = self.window_width()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:  # If user hits space or up arrow key
                if not runner.jumping:  # If we are not already jumping
                    runner.jumping = True

        menu = True

        while menu:
            pygame.time.delay(100)
            self.screen.blit(background_image, [0, 0])
            back = pygame.draw.rect(self.screen, (255, 255, 255), (20, 20, 100, 40))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    if 20 < mouse_x < 120 and 20 < mouse_y < 60:
                        self.homepagebg()

                if event.type == pygame.QUIT:
                    menu = False

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(self.clock_rate)

        pygame.quit()
        exit()

        while not dead:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True

            self.screen.blit(background_image, [0, 0])

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

    def runningbg(self):
        pygame.display.set_caption("Running")
        dead = False
        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("haunted.png").convert()

        character = pygame.image.load("duckresized.png")
        character_x = 0
        character_y = 220
        vel = 5

        menu = True

        while menu:
            pygame.time.delay(100)
            self.screen.blit(background_image, [0, 0])
            self.screen.blit(character, (character_x, character_y))

            back = pygame.draw.rect(self.screen, (255, 255, 255), (20, 20, 100, 40))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    if 20 < mouse_x < 120 and 20 < mouse_y < 60:
                        self.homepagebg()

                if event.type == pygame.QUIT:
                    menu = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                character_x -= vel

            if keys[pygame.K_RIGHT]:
                character_x += vel

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(self.clock_rate)

        pygame.quit()
        exit()

        while not dead:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True

            self.screen.blit(background_image, [0, 0])

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

    def flyingbg(self):
        pygame.display.set_caption("Flying")
        dead = False
        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("sky2.png").convert()

        character = pygame.image.load("duckresized.png")
        character_x = 0
        character_y = 220
        vel = 5

        menu = True

        while menu:
            pygame.time.delay(100)
            self.screen.blit(background_image, [0, 0])
            self.screen.blit(character, (character_x, character_y))

            back = pygame.draw.rect(self.screen, (255, 255, 255), (20, 20, 100, 40))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    if 20 < mouse_x < 120 and 20 < mouse_y < 60:
                        self.homepagebg()

                if event.type == pygame.QUIT:
                    menu = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                character_x -= vel

            if keys[pygame.K_RIGHT]:
                character_x += vel

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(self.clock_rate)

        pygame.quit()
        exit()

        while not dead:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True

            self.screen.blit(background_image, [0, 0])

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

    def helpbg(self):
        pygame.display.set_caption("Rules")
        dead = False
        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("newrules.png").convert()

        menu = True

        while menu:
            self.screen.blit(background_image, [0, 0])
            back = pygame.draw.rect(self.screen, (0, 0, 0), (20, 20, 100, 30))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    if mouse_x > 20 and mouse_x < 120 and mouse_y > 20 and mouse_y < 50:
                        self.homepagebg()

                if event.type == pygame.QUIT:
                    menu = False
                    pygame.quit()
                    exit()

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(self.clock_rate)

        while (dead == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True

            self.screen.blit(background_image, [0, 0])

            pygame.display.flip()
            self.clock.tick(self.clock_rate)
