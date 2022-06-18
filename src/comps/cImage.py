from msilib.schema import Component
import pygame
from src.comps.component import Component
from src.globals import C_IMAGE

class Image(Component):
    def __init__(self):
        super().__init__(C_IMAGE)
        self.surface = None

    def load(self, path):
        self.surface = pygame.image.load(path)