# Entity class to hold information about entities for 38Engine
# Sushil Louis

#from vector import MyVector
import ogre.renderer.OGRE as ogre
from physics import Physics
from render import Renderable

class Entity:
    mesh = 'robot.mesh'
    pos  = ogre.Vector3(0, 0, 0)
    vel  = ogre.Vector3(0, 0, 0)
    yaw  = 0

    aspectTypes = [Physics, Renderable]
    
    def __init__(self, id, pos = ogre.Vector3(0,0,0), mesh = 'robot.mesh', speed = 0, heading = 0, acceleration=10, turningRate=.05, topSpeed = 100):
        self.id = id
        self.pos = pos
        self.speed = speed
        self.mesh = mesh
        self.heading = heading
        self.topSpeed = topSpeed
        self.headingChange = 0
        self.aspects = []
        self.initAspects()
        self.acceleration = acceleration
        self.turningRate = turningRate
        self.desiredSpeed = 0
        self.desiredHeading = 0


    def initAspects(self):
        for aspType in self.aspectTypes:
            self.aspects.append(aspType(self))
        

    def tick(self, dtime):
        print "Ent tick", str(self.vel)
        for aspect in self.aspects:
            aspect.tick(dtime)


    def __str__(self):
        x = "Entity: %s \nPos: %s, Vel: %s, yaw: %f" % (self.id, str(self.pos), str(self.vel), self.yaw)
        return x


