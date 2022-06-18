from src.globals import *
from src.comps.component import Component

class Position(Component):
    def __init__(self):
        super().__init__(C_POSITION)
        self.x = 0
        self.y = 0