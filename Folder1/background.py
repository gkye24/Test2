import pygame
from pygame.locals import *
import os
import random

pygame.mixer.init(44100, 16, 2, 4096)
pygame.init()

# background music
pygame.mixer.music.load("happymusic.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

W, H = 500, 300
win = pygame.display.set_mode((W, H))


class player(object):
    run = pygame.image.load(os.path.join('duckresized.png'))
    jump = pygame.image.load(os.path.join('duckresized.png'))
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2,
                -2, -2, -2, -3, -3, -3, -3, -3, -3,
                -3, -3, -3, -3, -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.falling = False
        self.jumpCount = 0
        self.runCount = 0


    def draw(self, win):
        # if self.falling:
        #     win.blit(self.fall)

        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 3
            win.blit(self.jump, (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 10)

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run, (self.x, self.y))
            self.runCount += 1
            self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 13)

        # pygame.draw.rect(win, (255,0,0),self.hitbox, 2) # Draws hitbox

class saw(object):
    img1 = pygame.image.load(os.path.join('log.jpg'))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotateCount = 0
        self.vel = 1.4
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)  # Defines the accurate hitbox for our character
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        win.blit(pygame.transform.scale(self.img1, (64, 64)), (self.x, self.y))  # scales our image down to 64x64 before drawing

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class spike(saw):
    img2 = pygame.image.load(os.path.join('gem2.png'))

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)  # Defines the accurate hitbox for our character
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        win.blit(pygame.transform.scale(self.img2, (64, 64)), (self.x, self.y))  # scales our image down to 64x64 before drawing

class bump(saw):
    img3 = pygame.image.load(os.path.join('flower2.jpg'))

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)  # Defines the accurate hitbox for our character
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        win.blit(pygame.transform.scale(self.img3, (64, 64)),
                 (self.x, self.y))  # scales our image down to 64x64 before drawing

class Background:
    pygame.init()

    def __init__(self, window_width, window_height, animation_increment, clock_rate):
        self.window_width = window_width
        self.window_height = window_height
        self.animation_increment = animation_increment
        self.clock_rate = clock_rate
        self.size = (window_width, window_height)
        self.screen = pygame.display.set_mode(self.size)
        self.bgX = 0
        self.bgX2 = window_width

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

        run = True
        speed = 30  # NEW

        while menu:
            self.screen.blit(background_image, [0, 0])
            self.screen.blit(character, (character_x, character_y))
            help = pygame.draw.rect(self.screen, (207, 185, 151), (20, 20, 50, 40))
            first = pygame.draw.rect(self.screen, (255, 255, 255), (110, 20, 100, 40))
            second = pygame.draw.rect(self.screen, (255, 255, 255), (250, 20, 100, 40))
            third = pygame.draw.rect(self.screen, (255, 255, 255), (390, 20, 100, 40))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    if mouse_x > 20 and mouse_x < 70 and mouse_y > 20 and mouse_y < 60:
                        self.helpbg()
                    elif mouse_x > 110 and mouse_x < 210 and mouse_y > 20 and mouse_y < 60:
                        self.obstacle1()
                    elif mouse_x > 250 and mouse_x < 350 and mouse_y > 20 and mouse_y < 60:
                        self.obstacle2()
                    elif mouse_x > 390 and mouse_x < 490 and mouse_y > 20 and mouse_y < 60:
                        self.obstacle3()

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

    def obstacle1(self):
        pygame.display.set_caption("Easy")
        dead = False

        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("ground2.jpg").convert()

        clock = pygame.time.Clock()

        runner = player(100, 200, 64, 64)
        pygame.time.set_timer(USEREVENT + 1, 500)  # Sets the timer for 0.5 seconds
        pygame.time.set_timer(USEREVENT + 2, random.randrange(5000, 7000))

        run = True
        obstacles = []
        speed = 30

        while run and not runner.falling:
            clock.tick(speed)

            for obstacle in obstacles:
                obstacle.x -= 1.4
                if obstacle.x < obstacle.width * -1:  # If our obstacle is off the screen we will remove it
                    obstacles.pop(obstacles.index(obstacle))

            self.bgX -= 1.4  # Move both background images back
            self.bgX2 -= 1.4

            if self.bgX < self.window_width * -1:  # If our bg is at the -width then reset its position
                self.bgX = self.window_width

            if self.bgX2 < self.window_width * -1:
                self.bgX2 = self.window_width

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                if event.type == USEREVENT+1:
                    speed += 1
                if event.type == USEREVENT + 2:
                    pygame.time.set_timer(USEREVENT + 2,
                    random.randrange(5000, 7000))

                    r = 0
                    if r == 0:
                        log = saw(self.window_width, 200, 64, 64)
                        obstacles.append(log)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:  # If user hits space or up arrow key
                if not runner.jumping:  # If we are not already jumping
                    runner.jumping = True

            self.redrawWindow(background_image, runner, obstacles)
            if runner.falling:
                self.fallbg()

        while not dead:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True

            self.screen.blit(background_image, [0, 0])

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

    def obstacle2(self):
        pygame.display.set_caption("Medium")

        dead = False

        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("haunted.png").convert()

        clock = pygame.time.Clock()

        runner = player(100, 220, 64, 64)
        pygame.time.set_timer(USEREVENT + 1, 500)  # Sets the timer for 0.5 seconds
        pygame.time.set_timer(USEREVENT + 2, random.randrange(3000, 5000))  # Will trigger every 2 - 3.5 seconds

        run = True
        obstacles = []
        speed = 40

        while run and not runner.falling:
            clock.tick(speed)

            for obstacle in obstacles:
                obstacle.x -= 1.4
                if obstacle.x < obstacle.width * -1:  # If our obstacle is off the screen we will remove it
                    obstacles.pop(obstacles.index(obstacle))

            self.bgX -= 1.4  # Move both background images back
            self.bgX2 -= 1.4

            if self.bgX < self.window_width * -1:  # If our bg is at the -width then reset its position
                self.bgX = self.window_width

            if self.bgX2 < self.window_width * -1:
                self.bgX2 = self.window_width

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                if event.type == USEREVENT + 1:
                    speed += 2
                if event.type == USEREVENT + 2:
                    pygame.time.set_timer(USEREVENT + 2,
                    random.randrange(3000, 5000))

                    r = random.randrange(0, 2)
                    if r == 0:
                        log = saw(self.window_width, 220, 64, 64)
                        obstacles.append(log)
                    else:
                        gem = spike(self.window_width, 220, 64, 64)
                        obstacles.append(gem)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:  # If user hits space or up arrow key
                if not runner.jumping:  # If we are not already jumping
                    runner.jumping = True

            self.redrawWindow(background_image, runner, obstacles)
            if runner.falling:
                self.fallbg()

        while not dead:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True

            self.screen.blit(background_image, [0, 0])

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

    def obstacle3(self):
        pygame.display.set_caption("Hard")

        dead = False

        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("sky2.png").convert()

        clock = pygame.time.Clock()

        runner = player(100, 220, 64, 64)
        pygame.time.set_timer(USEREVENT + 1, 500)  # Sets the timer for 0.5 seconds
        pygame.time.set_timer(USEREVENT + 2, random.randrange(2000, 4000))  # Will trigger every 2 - 3.5 seconds

        run = True
        obstacles = []
        speed = 50

        while run and not runner.falling:
            clock.tick(speed)

            for obstacle in obstacles:
                obstacle.x -= 1.4
                if obstacle.x < obstacle.width * -1:  # If our obstacle is off the screen we will remove it
                    obstacles.pop(obstacles.index(obstacle))

            self.bgX -= 1.4  # Move both background images back
            self.bgX2 -= 1.4

            if self.bgX < self.window_width * -1:  # If our bg is at the -width then reset its position
                self.bgX = self.window_width

            if self.bgX2 < self.window_width * -1:
                self.bgX2 = self.window_width

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                if event.type == USEREVENT + 1:
                    speed += 3
                if event.type == USEREVENT + 2:
                    pygame.time.set_timer(USEREVENT + 2,
                                          random.randrange(2000, 4000))

                    r = random.randrange(0, 2)
                    if r == 0:
                        log = saw(self.window_width, 200, 64, 64)
                        obstacles.append(log)
                    elif r == 1:
                        flower = bump(self.window_width, 200, 64, 64)
                        obstacles.append(flower)
                    else:
                        gem = spike(self.window_width, 200, 64, 64)
                        obstacles.append(gem)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:  # If user hits space or up arrow key
                if not runner.jumping:  # If we are not already jumping
                    runner.jumping = True

            self.redrawWindow(background_image, runner, obstacles)
            if runner.falling:
                self.fallbg()

        while not dead:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True

            self.screen.blit(background_image, [0, 0])

            pygame.display.flip()
            self.clock.tick(self.clock_rate)

    def fallbg(self):
        pygame.display.set_caption("Dead")
        dead = False
        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("diedresized.png").convert()

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

    def helpbg(self):
        pygame.display.set_caption("Rules")
        dead = False
        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("rules2.png").convert()

        menu = True

        while menu:
            self.screen.blit(background_image, [0, 0])
            back = pygame.draw.rect(self.screen, (0, 0, 0), (20, 10, 100, 30))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    if mouse_x > 20 and mouse_x < 120 and mouse_y > 10 and mouse_y < 40:
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

    def redrawWindow(self, bg, runner, obstacles):
        win.blit(bg, (self.bgX, 0))  # draws our first bg image
        win.blit(bg, (self.bgX2, 0))  # draws the second bg image
        for obstacle in obstacles:
            if obstacle.collide(runner.hitbox):
                runner.falling = True
            obstacle.draw(win)
        runner.draw(win)

        pygame.display.update()  # updates the screen