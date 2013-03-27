import ogre.renderer.OGRE as ogre

class Renderable:
    def __init__(self, _entity):
        self.entity = _entity
        self.node = None
        self.nodeAttached = False

    def attachNode(self, _node):
        self.node = _node
        self.nodeAttached = True

    def tick(self, dtime):
        if self.nodeAttached:
            self.node.position = self.entity.pos
            self.node.yaw(ogre.Degree(self.entity.headingChange))        

    def selected(self, selected):
        if self.nodeAttached:
            if selected:
                self.node.showBoundingBox(True)
            else:
                self.node.showBoundingBox(False)

