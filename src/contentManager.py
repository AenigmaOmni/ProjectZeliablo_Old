from src.entity import Entity
from src.stage import Stage
from src.entity import Entity
from src.comps.cPosition import Position
from src.comps.cImage import Image
from src.sys.sysActorRender import ActorRenderer

class ContentManager:
    def __init__(self):
        self.stages = []
        
    def load(self):
        self.currentStage = self.loadTest()

    def addStage(self, s):
        self.stages.append(s)

    def getStageWithTag(self, t):
        for stage in self.stages:
            for tag in self.stages.tags:
                if tag == t:
                    return stage
    


    def loadTest(self):
        hI = Image()
        hI.load("res/sprites/hero/walk_down.png")
        
        p = Position()
        p.x = 25
        p.y = 25

        h = Entity()
        h.addComponent(hI)
        h.addComponent(p)

        s = Stage()
        s.addEntity(h)

        s.addBasicSystems()

        self.addStage(s)
        return s