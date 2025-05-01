import pygame
from circleshape import CircleShape
from constants import *
import random

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
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_1.velocity = self.velocity.rotate(angle) * 1.2
            asteroid_2.velocity = self.velocity.rotate(-angle) * 1.2

