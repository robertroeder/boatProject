from ent import Entity

class EntityMgr():
    """An Entity Manager Class"""
    def __init__(self):
        self.entList = []
        self.nodeList = []
        self.selected = None
    
    def attachEntity(self, _entity):
        self.entList.append(_entity)
        self.selected = 0
	
    def attachNode(self, _node):
        self.nodeList.append(_node)

    def nextShip(self):
        if self.selected is not None:
            self.selected = self.selected + 1
        if self.selected >= len(self.entList):
            self.selected = 0

