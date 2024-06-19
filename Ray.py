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
        """
        Allows for moving the start position of the ray
        self.pos can be easier passed on as reference for less memory usage
        However, end pos needs to be re-calculated 
        This can also be removed if there is no end point but the ray is infinite
        """
        self.pos = np.array(pos)
        self.end_pos = self.pos + self.dir * self.dist


    def rotate(self, rotate_by):
        """
        Allows for rotation of individual rays changing their direction and end point
        """
        self.angle+=rotate_by
        self.dir = utils.dir_from_angle(self.angle)
        self.end_pos = self.pos + self.dir * self.dist

    
    def draw(self, pygame, screen):
        """
        Visualization
        """
        pygame.draw.line(screen, self.color, self.pos, self.end_pos) 


    def cast(self, bound: Boundary):
        """
        implements the raycast operation from this ray onto a certain boundary object 
        calculates t and u then checks
        0 < t < 1 ( line intersects on bound)  &
        0 < u < 1 ( line intersects on Ray  )

        where t =   ( (x1-x3) * (y3-y4) - (y1-y3) * (x3 - x4) ) / (x1 - x2) * (y3 - y4) - (y1- y2) * (x3-x4)
        and   u = - ( (x1-x2) * (y1-y3) - (y1-y2) * (x1 - x3) ) / (x1 - x2) * (y3 - y4) - (y1- y2) * (x3-x4)

        Returns the intersection point if it exists
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
        