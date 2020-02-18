from Folder1.background import Background
from Folder1.background import player
import pygame
from pygame.locals import *

def main():
    background1 = Background(500, 300, 10, 20)
    background1.homepagebg()

    background1.redrawWindow()

    # background2 = Background(500, 280, 10, 20)
    # background2.racetrackbg()
    #
    # background3 = Background(500, 300, 10, 20)
    # background3.jumpingbg()
    #
    # background4 = Background(500, 300, 10, 20)
    # background4.flyingbg()
main()