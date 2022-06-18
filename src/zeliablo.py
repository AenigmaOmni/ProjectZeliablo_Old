from tkinter.tix import WINDOW
import pygame
from pygame.locals import *
from src.globals import *

class Game:
    def __init__(self):
        self.running = True
        pygame.init()
        self.size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen = pygame.display.set_mode(self.size, vsync=1)
        pygame.display.set_caption(TITLE)
        pygame.mixer.set_num_channels(MAX_SOUND_CHANNELS)
        self.fpsLimit = FPS_CAP
        self.fpsClock = pygame.time.Clock()
        self.lastTime = 0

    def postInit(self):
        self.font = pygame.font.SysFont(None, 40)

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        t = pygame.time.get_ticks()
        #in seconds
        delta = (t - self.lastTime) / 1000.0
        self.lastTime = t

        #update here
        ...

    def draw(self):
        self.screen.fill( (0,0,0) )
        
        fpsSurface = self.font.render("FPS: " + str(round(self.fpsClock.get_fps())), True, (255, 255, 255))
        self.screen.blit(fpsSurface, (20,20))

        pygame.display.flip()

    def cleanup(self):
        pygame.quit()

    def run(self):
        self.postInit()

        while self.running:
            self.processEvents()
            self.update()
            self.draw()
            self.fpsClock.tick(self.fpsLimit)

        self.cleanup()