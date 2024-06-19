import numpy as np
class Boundary:
    def __init__(self, point_a, point_b, color=(255,255,255)):
        self.a = np.array(point_a)
        self.b = np.array(point_b)
        self.color = color
    

    def draw(self,pygame, screen, ):
        pygame.draw.line(screen, self.color, self.a, self.b) 