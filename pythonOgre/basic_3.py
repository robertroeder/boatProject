import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import SampleFramework as sf
 
class TutorialFrameListener(sf.FrameListener):
    def __init__(self, renderWindow, camera, sceneManager):
        sf.FrameListener.__init__(self, renderWindow, camera)
        self.toggle = 0
        self.mouseDown = False

        self.camNode = camera.parentSceneNode.parentSceneNode
        self.sceneManager = sceneManager
       
        self.rotate = 0.13
        self.move = 250

 
    def frameStarted(self, frameEvent):
        if(self.renderWindow.isClosed()):
            return False

        self.Keyboard.capture()
        self.Mouse.capture()

        currMouse = self.Mouse.getMouseState()
        if currMouse.buttonDown(OIS.MB_Left) and not self.mouseDown:
           light = self.sceneManager.getLight('Light1')
           light.visible = not light.visible
        
        self.mouseDown = currMouse.buttonDown(OIS.MB_Left)

        if self.toggle >= 0:
            self.toggle -= frameEvent.timeSinceLastFrame
            
        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_1):
            self.toggle = 0.1
            self.camera.parentSceneNode.detachObject(self.camera)
            self.camNode = self.sceneManager.getSceneNode("CamNode1")
            self.sceneManager.getSceneNode("PitchNode1").attachObject(self.camera)
        elif self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_2):
            self.toggle = 0.1
            self.camera.parentSceneNode.detachObject(self.camera)
            self.camNode = self.sceneManager.getSceneNode("CamNode2")
            self.sceneManager.getSceneNode("PitchNode2").attachObject(self.camera)

        transVector = ogre.Vector3(0, 0, 0)

        if self.Keyboard.isKeyDown(OIS.KC_UP) or self.Keyboard.isKeyDown(OIS.KC_W):
            transVector.z -= self.move

        if self.Keyboard.isKeyDown(OIS.KC_DOWN) or self.Keyboard.isKeyDown(OIS.KC_S):
            transVector.z += self.move

        if self.Keyboard.isKeyDown(OIS.KC_LEFT) or self.Keyboard.isKeyDown(OIS.KC_A):
            transVector.x -= self.move

        if self.Keyboard.isKeyDown(OIS.KC_RIGHT) or self.Keyboard.isKeyDown(OIS.KC_D):
            transVector.x += self.move

        if self.Keyboard.isKeyDown(OIS.KC_PGUP) or self.Keyboard.isKeyDown(OIS.KC_Q):
            transVector.y += self.move

        if self.Keyboard.isKeyDown(OIS.KC_PGDOWN) or self.Keyboard.isKeyDown(OIS.KC_E):
            transVector.y -= self.move

        self.camNode.translate(self.camNode.orientation * transVector * frameEvent.timeSinceLastFrame)

        if currMouse.buttonDown(OIS.MB_Right):
            self.camNode.yaw(ogre.Degree(-self.rotate * currMouse.X.rel).valueRadians())
            self.camNode.getChild(0).pitch(ogre.Degree(-self.rotate * currMouse.Y.rel).valueRadians())

        return not self.Keyboard.isKeyDown(OIS.KC_ESCAPE)


 
class TutorialApplication(sf.Application):
    def _createScene(self):
        sceneManager = self.sceneManager
        sceneManager.ambientLight = 0.25, 0.25, 0.25

        entity = sceneManager.createEntity('Ninja', 'ninja.mesh')
        node = sceneManager.getRootSceneNode().createChildSceneNode('NinjaNode')
        node.attachObject(entity)

        light = sceneManager.createLight('Light1')
        light.type = ogre.Light.LT_POINT
        light.position = 250, 150, 250
        light.diffuseColour = 1, 1, 1
        light.specularColour = 1, 1, 1

        node = sceneManager.getRootSceneNode().createChildSceneNode('CamNode1', (-400, 200, 400))
        node.yaw(ogre.Degree(-45))

        node = node.createChildSceneNode('PitchNode1')
        node.attachObject(self.camera)

        node = sceneManager.getRootSceneNode().createChildSceneNode('CamNode2', (0, 200, 400))
        node.createChildSceneNode('PitchNode2')
 
    def _createCamera(self):
        self.camera = self.sceneManager.createCamera('PlayerCam')
        self.camera.nearClipDistance = 5
 
    def _createFrameListener(self):
        self.frameListener = TutorialFrameListener(self.renderWindow, self.camera, self.sceneManager)
        self.root.addFrameListener(self.frameListener)
        self.frameListener.showDebugOverlay(True)
 
if __name__ == '__main__':
    try:
        ta = TutorialApplication()
        ta.go()
    except ogre.OgreException, e:
        print e
