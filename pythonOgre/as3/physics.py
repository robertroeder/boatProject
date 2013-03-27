import math

class Physics:
	"""A Physics Aspect Class"""
	def __init__(self, _entity):
		self.entity = _entity
		
	def update(self, _dt):
		#For now all we do is update position
        self.updateHeading(_dt)
        self.updateSpeed(_dt)
		self.updatePos(_dt)
		
    def updateHeading(self, _dt):
        pastHeading = self.entity.heading
        if( self.entity.heading < self.entity.desiredHeading):
            self.entity.heading = self.entity.heading + (self.entity.turningRate * _dt)
            if( self.entity.heading > self.entity.desiredHeading):
                self.entity.heading = self.entity.desiredHeading

        if( self.entity.heading > self.entity.desiredHeading):
            self.entity.heading = self.entity.heading - (self.entity.turningRate * _dt)
            if( self.entity.heading < self.entity.desiredHeading):
                self.entity.heading = self.entity.desiredHeading

        self.entity.headingChange = self.entity.heading - pastHeading

    def updateSpeed(self, _dt):
        if( self.entity.speed < self.entity.desiredSpeed):
            self.entity.speed = self.entity.speed + (self.entity.acceleration * _dt)
            if( self.entity.speed > self.entity.desiredSpeed):
                self.entity.speed = self.entity.desiredSpeed

        if( self.entity.speed > self.entity.desiredSpeed):
            self.entity.speed = self.entity.speed - (self.entity.acceleration * _dt)
            if( self.entity.speed < self.entity.desiredSpeed):
                self.entity.speed = self.entity.desiredSpeed

	def updatePos(self, _dt):
        dx = self.entity.speed*math.cos(self.entity.heading)*_dt
        dy = self.entity.speed*math.sin(self.entity.heading)*_dt
		self.entity.position = self.entity.position + (ogre.Vector3(dx, dy, 0))
