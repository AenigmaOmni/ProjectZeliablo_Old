class ContentManager:
    def __init__(self):
        self.stages = []
        self.currentStage = None

    def addStage(self, s):
        self.stages.append(s)

    def getStageWithTag(self, t):
        for stage in self.stages:
            for tag in self.stages.tags:
                if tag == t:
                    return stage
    
    