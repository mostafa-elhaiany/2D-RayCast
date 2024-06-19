import numpy as np
from Ray import Ray
class Particle:

    def __init__(self, pos, angle_increments=10, dist=50):
        self.pos = np.array(pos)
        self.rays = []
        self.increments = max(0.2, min(angle_increments, 36))
        a = 0
        while a < 360: 
            self.rays.append(Ray(pos, a, dist=dist))
            a+=angle_increments
        print(self.increments, angle_increments, len(self.rays))
    
    def set_pos(self, pos):
        self.pos = np.array(pos)
        for ray in self.rays:
            ray.set_pos(pos)


    def draw(self, pygame, screen):
        pygame.draw.circle(screen, (255,255,255), self.pos, 2) 

    def cast(self, bounds, pygame, screen):
        for r in self.rays:
            closest_dist = np.inf
            closest = None
            for bound in bounds:
                point = r.cast(bound)
                if(point is not None):
                    distance = np.linalg.norm(point-self.pos)
                    if(distance<closest_dist):
                        closest_dist = distance
                        closest = point
                
            if(closest is not None):
                pygame.draw.line(screen, (0,255,0), r.pos, closest) 
            else:
                pygame.draw.line(screen, (175,0,0), r.pos, r.end_pos) 