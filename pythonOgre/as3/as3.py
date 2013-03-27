import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import SampleFramework as sf
import time
from physics import Physics

 
class TutorialFrameListener(sf.FrameListener):
    def __init__(self, renderWindow, camera, sceneManager):
        sf.FrameListener.__init__(self, renderWindow, camera)
        self.toggle = 0
        self.mouseDown = False

        self.camNode = camera.parentSceneNode.parentSceneNode
        self.sceneManager = sceneManager
        self.cubeNode=self.sceneManager.getSceneNode("CubeNode")

        #Add a velocity and postion to the cube entity
        self.cube = self.sceneManager.getEntity("Cube")
        self.cube.velocity=ogre.Vector3(0,0,0)
        self.cube.position=ogre.Vector3(0,0,0)

        #Add a physics aspect to the cube entity
        self.cube.physics = Physics(self.cube)
        self.rotate = 0.13
        self.move = 250
 
    def frameStarted(self, frameEvent):
        if(self.renderWindow.isClosed()):
            return False

        self.Keyboard.capture()
        self.Mouse.capture()
        
        self.cubeNode=self.sceneManager.getSceneNode("CubeNode")

        #Camera movement controls
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

        if self.Keyboard.isKeyDown(OIS.KC_W):
            transVector.z -= self.move
  
        if self.Keyboard.isKeyDown(OIS.KC_S):
            transVector.z += self.move

        if self.Keyboard.isKeyDown(OIS.KC_A):
            transVector.x -= self.move

        if self.Keyboard.isKeyDown(OIS.KC_D):
            transVector.x += self.move

        if self.Keyboard.isKeyDown(OIS.KC_E):
            transVector.y += self.move

        if self.Keyboard.isKeyDown(OIS.KC_F):
            transVector.y -= self.move
  
        #Cube movement controls
        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_NUMPAD9):
            self.toggle = 0.1
            self.cube.velocity.y += 10

        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_NUMPAD3):
            self.toggle = 0.1
            self.cube.velocity.y -= 10

        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_NUMPAD8):
            self.toggle = 0.1
            self.cube.velocity.z += 10

        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_NUMPAD2):
            self.toggle = 0.1
            self.cube.velocity.z -= 10

        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_NUMPAD6):
            self.toggle = 0.1
            self.cube.velocity.x += 10

        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_NUMPAD4):
            self.toggle = 0.1
            self.cube.velocity.x -= 10

        if self.Keyboard.isKeyDown(OIS.KC_SPACE):
            self.cube.velocity = ogre.Vector3(0,0,0)

        self.camNode.translate(self.camNode.orientation * transVector * frameEvent.timeSinceLastFrame)

        #Update the position of the cube based off velocity
        self.cube.physics.update(frameEvent.timeSinceLastFrame)
        #Set the cube node position to the entity position
        self.cubeNode.setPosition(self.cube.position)

        if currMouse.buttonDown(OIS.MB_Right):
            self.camNode.yaw(ogre.Degree(-self.rotate * currMouse.X.rel).valueRadians())
            self.camNode.getChild(0).pitch(ogre.Degree(-self.rotate * currMouse.Y.rel).valueRadians())

        return not self.Keyboard.isKeyDown(OIS.KC_ESCAPE)

      
class TutorialApplication(sf.Application):
    def _createScene(self):
        sceneManager = self.sceneManager
        sceneManager.ambientLight = 0.25, 0.25, 0.25

        surfaceHeight = -60
        entity = sceneManager.createEntity('Cube', 'cube.mesh')
        entity.setMaterialName ('Examples/Borg')
        node = sceneManager.getRootSceneNode().createChildSceneNode('CubeNode')
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

				 # Setup a ground plane.
        plane = ogre.Plane ((0, 1, 0), surfaceHeight)
        meshManager = ogre.MeshManager.getSingleton ()
        #Create a giant plane
        meshManager.createPlane ('Ground', 'General', plane,
                                     10000, 10000, 20, 20, True, 1, 5, 5, (0, 0, 1))
        ent = sceneManager.createEntity('GroundEntity', 'Ground')
        sceneManager.getRootSceneNode().createChildSceneNode ().attachObject (ent)
        ent.setMaterialName ('Examples/Water')
        ent.castShadows = False
 
        # Setup a sky plane.
        plane = ogre.Plane ((0, -1, 0), -10)
        self.sceneManager.setSkyPlane (True, plane, "Examples/Pizza",
                                      100, 45, True, 0.5, 150, 150)

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
