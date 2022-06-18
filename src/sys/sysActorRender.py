import pygame
from pygame.locals import *
from src.sys.system import System
from src.globals import *

class ActorRenderer(System):
    def __init__(self, stage):
        self.stage = stage

    def draw(self, entity, screenSurface):
        iC = entity.getComponent(C_IMAGE)
        iP = entity.getComponent(C_POSITION)
        screenSurface.blit( iC.surface, (iP.x, iP.y))


    def process(self, screenSurface):
        ents = self.stage.getAllEntities()
        for ent in ents:
            if ent.hasComponent(C_IMAGE) and ent.hasComponent(C_POSITION):
                self.draw(ent, screenSurface)

        