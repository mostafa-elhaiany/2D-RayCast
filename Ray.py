import numpy as np 
import utils
from Boundary import Boundary

class Ray:

    def __init__(self, start_pos, angle,color=(255,255,255), dist=500):
        self.pos = np.array(start_pos)
        self.dist = dist
        self.angle = angle
        self.dir = utils.dir_from_angle(angle)
        self.end_pos = self.pos + self.dir * self.dist
        self.color = color

    def set_pos(self, pos):
        self.pos = np.array(pos)
        self.end_pos = self.pos + self.dir * self.dist


    def rotate(self, rotate_by):
        self.angle+=rotate_by
        self.dir = utils.dir_from_angle(self.angle)
        self.end_pos = self.pos + self.dir * self.dist

    
    def draw(self, pygame, screen):
        pygame.draw.line(screen, self.color, self.pos, self.end_pos) 


    def cast(self, bound: Boundary):
        """
        implements the raycast operation from this ray onto a certain boundary object 
        calculates t and u then checks
        0 < t < 1 ( line intersects on bound)  &
        0 < u < 1 ( line intersects on Ray  )
        then returns an intersection points if it exists
        """
        y1,x1 = self.pos
        y2,x2 = self.end_pos

        y3,x3 = bound.a
        y4,x4 = bound.b


        denom = (x1 - x2) * (y3 - y4) - (y1- y2) * (x3-x4)
        if denom == 0:
            return None
        
        t = ( (x1-x3) * (y3-y4) - (y1-y3) * (x3 - x4) ) / denom
        u = - ( (x1-x2) * (y1-y3) - (y1-y2) * (x1 - x3) ) / denom

        if(0<=t<=1 and 0<=u<=1):
            point = (y1 + t*(y2-y1),
                     x1 + t*(x2 - x1)
                     )
            return point
        else:
            return None
        