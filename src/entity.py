class Entity:
    def __init__(self):
        self.tags = []
        self.components = []
    
    def addComponent(self, component):
        self.components.append(component)

    def hasComponent(self, c):
        for comp in self.components:
            if comp.id == c:
                return True

    def getComponent(self, c):
        for comp in self.components:
            if comp.id == c:
                return comp

    def getComponents(self):
        return self.components

    def addTag(self, t):
        self.tags.append(t)