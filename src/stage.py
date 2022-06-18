from src.sys.sysActorRender import ActorRenderer

class Stage:
    def __init__(self):
        self.entities = []
        self.updateSystems = []
        self.renderSystems = []

    def addRenderSystem(self, s):
        self.renderSystems.append(s)

    def addUpdateSystem(self, s):
        self.updateSystems.append(s)

    def getUpdateSystems(self):
        return self.updateSystems

    def getRenderSystems(self):
        return self.renderSystems

    def addEntity(self, entity):
        self.entities.append(entity)

    def getAllEntities(self):
        return self.entities
    
    def getEntityWithTag(self, tag):
        for entity in self.entities:
            for t in entity.tags:
                if t == tag:
                    return entity

    def addBasicSystems(self):
        self.addRenderSystem(ActorRenderer(self))

    def update(self, screen):
        #update systems
        for sys in self.updateSystems:
            sys.process(screen)

    def render(self, screen):
        #draw systems
        for sysR in self.renderSystems:
            sysR.process(screen)
