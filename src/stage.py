class Stage:
    def __init__(self):
        self.entities = []
        self.mapData = None

    def update(self):
        pass
        
    def draw(self):
        pass

    def addEntity(self, entity):
        self.entities.append(entity)

    def getAllEntities(self):
        return self.entities
    
    def getEntityWithTag(self, tag):
        for entity in self.entities:
            for t in entity.tags:
                if t == tag:
                    return entity
