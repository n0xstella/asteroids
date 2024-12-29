# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print('"Starting asteroids!"')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    
    # Unique groups for game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Adding game objects to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Object creation
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()

    # Allow for the closing of a window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set the screen fill color to black and force it to refresh    
        screen.fill(color="black")

        # Update players current position on screen
        for obj in updatable:
            obj.update(dt)

        # Renders the player onto screen to match each frame
        for obj in drawable:
            obj.draw(screen)

        # Check for collisions
        for obj in asteroids:
            if obj.collision(player):
                print("Game Over!")
                exit()
                
        # Re-renders all objects on the screen (i.e..players, asteroids etc...)
        pygame.display.flip()

        # Limit FPS to 60
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()