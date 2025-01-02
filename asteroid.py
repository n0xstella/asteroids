import pygame
from constants import *
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Splitting asteroid into two smaller asteroids with faster movement speeds
        random_split_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position.x, self.position.y

        asteroid_1 = Asteroid(x, y, new_radius)
        asteroid_2 = Asteroid(x, y, new_radius)
        
        asteroid_1.velocity = pygame.Vector2(x, y).rotate(random_split_angle) *  1.2
        asteroid_2.velocity = pygame.Vector2(x, y).rotate(-random_split_angle) * 1.2


        
