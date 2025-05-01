import pygame
from circleshape import CircleShape
from constants import *

# Base class for game objects
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, center = self.position, color="white", radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def check_collision(self, circle):
        if self.position.distance_to(circle.position) > self.radius + circle.radius:
            return False
        else:
            return True
        