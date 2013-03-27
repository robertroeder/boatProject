# Assignment 4

import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import SampleFramework as sf

from ent import Entity
from entityMgr import EntityMgr

class ControlFrameListener(ogre.FrameListener):
    """To call the ent's tick and copy ent's new position to corresponding 
    scene node"""

    def __init__(self, entMgr):
        ogre.FrameListener.__init__(self)
        self.entMgr = entMgr

    def frameStarted(self, frameEvent):
        for index, value in enumerate(self.entMgr.entList):
            if index == self.entMgr.selected:
                self.entMgr.entList[index].aspects[1].selected(True)
            else:
                self.entMgr.entList[index].aspects[1].selected(False)

            self.entMgr.entList[index].tick(frameEvent.timeSinceLastFrame)
        return True


 
class TutorialFrameListener(sf.FrameListener):
    """A FrameListener class that handles basic user input."""
 
    def __init__(self, renderWindow, camera, sceneManager, ent):
        # Subclass any Python-Ogre class and you must call its constructor.
        sf.FrameListener.__init__(self, renderWindow, camera)
 
        #For as3
        self.ent = ent
        self.deltaVelocity = 25

        # Key and mouse state tracking.
        self.toggle = 0
        self.mouseDown = False
 
        # Populate the camera and scene manager containers.
        self.camNode = camera.parentSceneNode.parentSceneNode
        self.sceneManager = sceneManager
 
        # Set the rotation and movement speed.
        self.rotate = 0.13
        self.move = 250
 
    def frameStarted(self, frameEvent):
        # If the render window has been closed, end the program.
        if(self.renderWindow.isClosed()):
            return False
 
        # Capture and update each input device.
        self.Keyboard.capture()
        self.Mouse.capture()
 
        # Get the current mouse state.
        currMouse = self.Mouse.getMouseState()
 
        # Use the Left mouse button to turn Light1 on and off.         
        if currMouse.buttonDown(OIS.MB_Left) and not self.mouseDown:
            light = self.sceneManager.getLight('Light1')
            light.visible = not light.visible
 
        # Update the mouseDown boolean.            
        self.mouseDown = currMouse.buttonDown(OIS.MB_Left)
 
        # Update the toggle timer.
        if self.toggle >= 0:
            self.toggle -= frameEvent.timeSinceLastFrame
 
        # Swap the camera's viewpoint with the keys 1 or 2.
        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_1):
            # Update the toggle timer.
            self.toggle = 0.1
            # Attach the camera to PitchNode1.
            self.camera.parentSceneNode.detachObject(self.camera)
            self.camNode = self.sceneManager.getSceneNode("CamNode1")
            self.sceneManager.getSceneNode("PitchNode1").attachObject(self.camera)
 
        elif self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_2):
            # Update the toggle timer.
            self.toggle = 0.1
            # Attach the camera to PitchNode2.
            self.camera.parentSceneNode.detachObject(self.camera)
            self.camNode = self.sceneManager.getSceneNode("CamNode2")
            self.sceneManager.getSceneNode("PitchNode2").attachObject(self.camera)
 
        # Move the camera using keyboard input.
        transVector = ogre.Vector3(0, 0, 0)
        # Move Forward.
        if self.Keyboard.isKeyDown(OIS.KC_W):
           transVector.z -= self.move
        # Move Backward.
        if self.Keyboard.isKeyDown(OIS.KC_S):
            transVector.z += self.move
        # Strafe Left.
        if self.Keyboard.isKeyDown(OIS.KC_A):
            transVector.x -= self.move
        # Strafe Right.
        if self.Keyboard.isKeyDown(OIS.KC_D):
           transVector.x += self.move
        # Move Up.        
        if self.Keyboard.isKeyDown(OIS.KC_Q):
            transVector.y += self.move
        # Move Down.
        if self.Keyboard.isKeyDown(OIS.KC_E):
            transVector.y -= self.move
 
        # Translate the camera based on time.
        self.camNode.translate(self.camNode.orientation
                              * transVector
                              * frameEvent.timeSinceLastFrame)
 
        # Rotate the camera when the Right mouse button is down.
        if currMouse.buttonDown(OIS.MB_Right):
           self.camNode.yaw(ogre.Degree(-self.rotate 
                            * currMouse.X.rel).valueRadians())
           self.camNode.getChild(0).pitch(ogre.Degree(-self.rotate
                                          * currMouse.Y.rel).valueRadians())


        self.handleEnts(frameEvent)
 
        # If the escape key is pressed end the program.
        return not self.Keyboard.isKeyDown(OIS.KC_ESCAPE)


    def handleEnts(self, frameEvent):

        ent = self.sceneManager.entManager.entList[self.sceneManager.entManager.selected]
        
        if self.toggle >= 0:
            self.toggle -= frameEvent.timeSinceLastFrame

        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_NUMPAD8):
            ent.desiredSpeed += self.deltaVelocity
            self.toggle = 0.1

        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_NUMPAD2):
            ent.desiredSpeed -= self.deltaVelocity
            self.toggle = 0.1

        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_NUMPAD4):
            ent.desiredHeading += 10
            #if ent.desiredHeading > 180:
            #    ent.desiredHeading -= 360
            self.toggle = 0.2

        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_NUMPAD6):
            ent.desiredHeading -= 10
            #if ent.desiredHeading < 180:
            #    ent.desiredHeading += 360
            self.toggle = 0.2

        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_TAB):
            self.sceneManager.entManager.nextShip()
            self.toggle = 0.5

        return
 
class TutorialApplication(sf.Application):
    """The Application class."""
 
    def _createScene(self):
        # Setup a scene with a high level of ambient light.
        sceneManager = self.sceneManager
        #sceneManager.ambientLight = 0.25, 0.25, 0.25
        #more light
        sceneManager.ambientLight = 1.0, 1.0, 1.0
 
        sceneManager.entManager = EntityMgr()

        # create game engine's entity from our as2 class (with small changes)
        self.sailEnt = Entity("Sail", mesh = 'sailboat.mesh', pos = ogre.Vector3(0,-95,-120), acceleration=10, turningRate=0.1, topSpeed = 200)
        sceneManager.entManager.attachEntity(self.sailEnt)
        # create corresponding ogre ent
        self.pEnt2    = sceneManager.createEntity(self.sailEnt.id, self.sailEnt.mesh)
        # create scene node to attach pEnt to
        self.sailEntSceneNode   = sceneManager.getRootSceneNode().createChildSceneNode(self.sailEnt.id + 'node')
        self.sailEntSceneNode.attachObject(self.pEnt2)
        self.sailEnt.aspects[1].attachNode(self.sailEntSceneNode)

        # create game engine's entity from our as2 class (with small changes)
        self.alienEnt = Entity("Alien", mesh = 'alienship.mesh', pos = ogre.Vector3(0,-95,0), acceleration=150, turningRate=0.5, topSpeed = 1000)
        sceneManager.entManager.attachEntity(self.alienEnt)
        # create corresponding ogre ent
        self.pEnt    = sceneManager.createEntity(self.alienEnt.id, self.alienEnt.mesh)
        # create scene node to attach pEnt to
        self.alienEntSceneNode   = sceneManager.getRootSceneNode().createChildSceneNode(self.alienEnt.id + 'node')
        self.alienEntSceneNode.attachObject(self.pEnt)
        self.alienEnt.aspects[1].attachNode(self.alienEntSceneNode)

        # create game engine's entity from our as2 class (with small changes)
        self.montEnt = Entity("Monterey", mesh = '3699_Monterey_189_92.mesh', pos = ogre.Vector3(0,-95,80), acceleration=20, turningRate=.2, topSpeed = 400)
        sceneManager.entManager.attachEntity(self.montEnt)
        # create corresponding ogre ent
        self.pEnt3    = sceneManager.createEntity(self.montEnt.id, self.montEnt.mesh)
        # create scene node to attach pEnt to
        self.montEntSceneNode   = sceneManager.getRootSceneNode().createChildSceneNode(self.montEnt.id + 'node')
        self.montEntSceneNode.yaw(ogre.Degree(90))
        self.montEntSceneNode.attachObject(self.pEnt3)
        self.montEnt.aspects[1].attachNode( self.montEntSceneNode)

         # create game engine's entity from our as2 class (with small changes)
        self.boatEnt = Entity("Boat", mesh = '5086_Boat.mesh', pos = ogre.Vector3(0,-95,160), acceleration=30, turningRate=.4, topSpeed = 600)
        sceneManager.entManager.attachEntity(self.boatEnt)
        # create corresponding ogre ent
        self.pEnt5    = sceneManager.createEntity(self.boatEnt.id, self.boatEnt.mesh)
        # create scene node to attach pEnt to
        self.boatEntSceneNode   = sceneManager.getRootSceneNode().createChildSceneNode(self.boatEnt.id + 'node')
        self.boatEntSceneNode.attachObject(self.pEnt5)
        self.boatEnt.aspects[1].attachNode( self.boatEntSceneNode)

         # create game engine's entity from our as2 class (with small changes)
        self.boat2Ent = Entity("Boat2", mesh = 'boat.mesh', pos = ogre.Vector3(0,-95,200), acceleration=10, turningRate=.05, topSpeed = 100)
        sceneManager.entManager.attachEntity(self.boat2Ent)
        # create corresponding ogre ent
        self.pEnt6    = sceneManager.createEntity(self.boat2Ent.id, self.boat2Ent.mesh)
        # create scene node to attach pEnt to
        self.boat2EntSceneNode   = sceneManager.getRootSceneNode().createChildSceneNode(self.boat2Ent.id + 'node')
        self.boat2EntSceneNode.attachObject(self.pEnt6)
        self.boat2Ent.aspects[1].attachNode( self.boat2EntSceneNode)

         # create game engine's entity from our as2 class (with small changes)
        self.cigEnt = Entity("Cigarette", mesh = 'cigarette.mesh', pos = ogre.Vector3(0,-95,240), acceleration=10, turningRate=.05, topSpeed = 100)
        sceneManager.entManager.attachEntity(self.cigEnt)
        # create corresponding ogre ent
        self.pEnt7    = sceneManager.createEntity(self.cigEnt.id, self.cigEnt.mesh)
        # create scene node to attach pEnt to
        self.cigEntSceneNode   = sceneManager.getRootSceneNode().createChildSceneNode(self.cigEnt.id + 'node')
        self.cigEntSceneNode.attachObject(self.pEnt7)
        self.cigEnt.aspects[1].attachNode( self.cigEntSceneNode)

         # create game engine's entity from our as2 class (with small changes)
        self.sleekEnt = Entity("Sleek", mesh = 'sleek.mesh', pos = ogre.Vector3(0,-95,360), acceleration=10, turningRate=.05, topSpeed = 100)
        sceneManager.entManager.attachEntity(self.sleekEnt)
        # create corresponding ogre ent
        self.pEnt10    = sceneManager.createEntity(self.sleekEnt.id, self.sleekEnt.mesh)
        # create scene node to attach pEnt to
        self.sleekEntSceneNode   = sceneManager.getRootSceneNode().createChildSceneNode(self.sleekEnt.id + 'node')
        self.sleekEntSceneNode.attachObject(self.pEnt10)
        self.sleekEnt.aspects[1].attachNode( self.sleekEntSceneNode)

         # create game engine's entity from our as2 class (with small changes)
        self.cvnEnt = Entity("CVN68", mesh = 'cvn68.mesh', pos = ogre.Vector3(0,-95,480), acceleration=10, turningRate=.05, topSpeed = 100)
        sceneManager.entManager.attachEntity(self.cvnEnt)
        # create corresponding ogre ent
        self.pEnt8    = sceneManager.createEntity(self.cvnEnt.id, self.cvnEnt.mesh)
        # create scene node to attach pEnt to
        self.cvnEntSceneNode   = sceneManager.getRootSceneNode().createChildSceneNode(self.cvnEnt.id + 'node')
        self.cvnEntSceneNode.attachObject(self.pEnt8)
        self.cvnEnt.aspects[1].attachNode( self.cvnEntSceneNode)
 
        # create game engine's entity from our as2 class (with small changes)
        self.watrEnt = Entity("Watercraft", mesh = '4685_Personal_Watercr.mesh', pos = ogre.Vector3(0,-95,560), acceleration=10, turningRate=.05, topSpeed = 100)
        sceneManager.entManager.attachEntity(self.watrEnt)
        # create corresponding ogre ent
        self.pEnt4    = sceneManager.createEntity(self.watrEnt.id, self.watrEnt.mesh)
        # create scene node to attach pEnt to
        self.watrEntSceneNode   = sceneManager.getRootSceneNode().createChildSceneNode(self.watrEnt.id + 'node')
        self.watrEntSceneNode.yaw(ogre.Degree(90))
        self.watrEntSceneNode.attachObject(self.pEnt4)
        self.watrEnt.aspects[1].attachNode( self.watrEntSceneNode)

         # create game engine's entity from our as2 class (with small changes)
        self.ddgEnt = Entity("DDG51", mesh = 'ddg51.mesh', pos = ogre.Vector3(0,-95,620), acceleration=10, turningRate=.05, topSpeed = 100)
        sceneManager.entManager.attachEntity(self.ddgEnt)
        # create corresponding ogre ent
        self.pEnt9    = sceneManager.createEntity(self.ddgEnt.id, self.ddgEnt.mesh)
        # create scene node to attach pEnt to
        self.ddgEntSceneNode   = sceneManager.getRootSceneNode().createChildSceneNode(self.ddgEnt.id + 'node')
        self.ddgEntSceneNode.attachObject(self.pEnt9)
        self.ddgEnt.aspects[1].attachNode( self.ddgEntSceneNode)

        # Setup the second camera node and pitch node.
        # don't need this
        node = sceneManager.getRootSceneNode().createChildSceneNode('CamNode2',
                                                              (0, 200, 400))
        node.createChildSceneNode('PitchNode2')  


        surfaceHeight = -100
        # Setup a ground plane at -100 height so the entire cube shows up
        plane = ogre.Plane ((0, 1, 0), surfaceHeight)
        meshManager = ogre.MeshManager.getSingleton ()
        #large plane 10000x10000
        meshManager.createPlane ('Ground', 'General', plane,
                                     10000, 10000, 20, 20, True, 1, 5, 5, (0, 0, 1))
        ent = sceneManager.createEntity('GroundEntity', 'Ground')
        sceneManager.getRootSceneNode().createChildSceneNode ().attachObject (ent)
        ent.setMaterialName ('Examples/Water')
        ent.castShadows = False
        #Like nice sky
        self.sceneManager.setSkyDome (True, "Examples/CloudySky", 5, 8)
        # Setup the first camera node and pitch node and aim it.
        camnode = sceneManager.getRootSceneNode().createChildSceneNode('CamNode1',
                                                               (0, 50, 500))
        #camnode.yaw(ogre.Degree(-45))

        node = camnode.createChildSceneNode('PitchNode1')
        node.attachObject(self.camera)      
 
    def _createCamera(self):
        self.camera = self.sceneManager.createCamera('PlayerCam')
        self.camera.nearClipDistance = 5
 
    def _createFrameListener(self):
        self.frameListener = TutorialFrameListener(self.renderWindow,
                                                   self.camera,
                                                   self.sceneManager, 
                                                   self.alienEnt)
        
        self.root.addFrameListener(self.frameListener)
        
        #add my ent frame listener
        self.controlFrameListener = ControlFrameListener(self.sceneManager.entManager)
        self.root.addFrameListener(self.controlFrameListener)

        self.frameListener.showDebugOverlay(True)
 
 
if __name__ == '__main__':
    try:
        ta = TutorialApplication()
        ta.go()
    except ogre.OgreException, e:
        print e
