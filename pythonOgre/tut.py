import ogre.renderer.OGRE as ogre
import SampleFramework as sf

class TutorialApplication(sf.Application):

    def _createScene(self):
       # Setup the ambient light. 
       sceneManager = self.sceneManager 
       sceneManager.ambientLight = (1.0, 1.0, 1.0) 
 
       # Setup a mesh entity and attach it to the root scene node. 
       ent1 = sceneManager.createEntity ('Robot', 'robot.mesh') 
       node1 = sceneManager.getRootSceneNode().createChildSceneNode ('RobotNode') 
       node1.attachObject (ent1) 
 
       # Setup a second mesh entity as a child node. 
       ent2 = sceneManager.createEntity ('Robot2', 'robot.mesh') 
       node2 = node1.createChildSceneNode ('RobotNode2', (50, 0, 0)) 
       node2.attachObject (ent2) 
       """
       #SET UP A LOT OF MESH ENTITIES
       for i in range(0,400):
           print i
           # Setup a second mesh entity as a child node. 
           ent2 = sceneManager.createEntity ('RobotMesh'+str(i), 'robot.mesh') 
           node1 = sceneManager.getRootSceneNode().createChildSceneNode ('RobotNodeU'+str(i), (i,0,0)) 
           node1.attachObject (ent2) 
       #SET UP A LOT OF MESH ENTITIES
       for i in range(0,400):
           print i
           # Setup a second mesh entity as a child node. 
           ent2 = sceneManager.createEntity ('RobotMesha'+str(i), 'robot.mesh') 
           node1 = sceneManager.getRootSceneNode().createChildSceneNode ('RobotNodew'+str(i), (0,i,0)) 
           node1.attachObject (ent2) 
       #SET UP A LOT OF MESH ENTITIES
       for i in range(0,400):
           print i
           # Setup a second mesh entity as a child node. 
           ent2 = sceneManager.createEntity ('RobotMeshd'+str(i), 'robot.mesh') 
           node1 = sceneManager.getRootSceneNode().createChildSceneNode ('RobotNodea'+str(i), (0,0,i)) 
           node1.attachObject (ent2) 
           """
if __name__ == '__main__':
    ta = TutorialApplication()
    ta.go()
