import math
import ogre.renderer.OGRE as ogre

class Physics:
    def __init__(self, entity, sceneNode=None):
        self.entity = entity
        
    def tick(self, _dt):
        #print "Physics tick", dtime
        #For now all we do is update position
        self.updateHeading(_dt)
        self.updateSpeed(_dt)
        self.updatePos(_dt)
		
    def updateHeading(self, _dt):
        oldHeading = self.entity.heading

        if(self.entity.heading < self.entity.desiredHeading):
            self.entity.heading = self.entity.heading + (self.entity.turningRate)
            #if( self.entity.heading > self.entity.desiredHeading):
            #    self.entity.heading = self.entity.desiredHeading

        elif(self.entity.heading > self.entity.desiredHeading):
            self.entity.heading = self.entity.heading - (self.entity.turningRate)
            #if( self.entity.heading < self.entity.desiredHeading):
            #    self.entity.heading = self.entity.desiredHeading

        self.entity.headingChange = self.entity.heading - oldHeading
        print "HEADING"
        print self.entity.headingChange
        print self.entity.desiredHeading
        print self.entity.heading 

    def updateSpeed(self, _dt):
        if self.entity.desiredSpeed < 0:
            self.entity.desiredSpeed = 0

        if self.entity.desiredSpeed > self.entity.topSpeed:
            self.entity.desiredSpeed = self.entity.topSpeed

        if( self.entity.speed < self.entity.desiredSpeed):
            self.entity.speed = self.entity.speed + (self.entity.acceleration * _dt)
            #if( self.entity.speed > self.entity.desiredSpeed):
            #    self.entity.speed = self.entity.desiredSpeed

        elif( self.entity.speed > self.entity.desiredSpeed):
            self.entity.speed = self.entity.speed - (self.entity.acceleration * _dt)
            #if( self.entity.speed < self.entity.desiredSpeed):
            #    self.entity.speed = self.entity.desiredSpeed

    def updatePos(self, _dt):
        dx = self.entity.speed*math.cos(math.radians((self.entity.heading)))*_dt
        dz = -1* self.entity.speed*math.sin(math.radians((self.entity.heading)))*_dt
        self.entity.pos = self.entity.pos + (ogre.Vector3(dx, 0, dz))
