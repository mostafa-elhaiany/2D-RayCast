import numpy as np 
import utils

class Ray:

    def __init__(self, start_pos, angle,color=(255,255,255), dist=50):
        self.pos = np.array(start_pos)
        self.angle = angle%360
        self.dir = utils.dir_from_angle(angle)
        self.color = color
        self.dist = dist

    def rotate(self, rotate_by):
        self.angle+=rotate_by
        self.angle %= 360
        self.dir = utils.dir_from_angle(self.angle)

    
    def draw(self, pygame, screen):
        end_pos = self.pos + self.dir * self.dist
        pygame.draw.line(screen, self.color, self.pos, end_pos) 
