import pygame
from circleshape import CircleShape
from constants import *

# Base class for game objects
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, center = self.position, color="white", radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def check_collision(self, circle):
        if self.position.distance_to(circle.position) > self.radius + circle.radius:
            return False
        else:
            return True