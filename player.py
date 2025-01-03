import pygame
from constants import *
from shot import Shot
from circleshape import CircleShape
from music import MusicManager

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

    # In the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        sound = MusicManager()

        # Decrease fire rate cooldown timer
        if self.shot_cooldown_timer > 0:
            self.shot_cooldown_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        # Handle shooting logic
        if keys[pygame.K_SPACE] and self.shot_cooldown_timer <= 0:
            self.shoot()
            sound.play_sound("firing_laser_sfx")
            self.shot_cooldown_timer = PLAYER_DEFAULT_SHOT_COOLDOWN_TIMER  # Reset cooldown

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        x, y = self.position.x, self.position.y
        shot = Shot(x, y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

