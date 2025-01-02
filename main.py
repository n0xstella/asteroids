# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from music import MusicManager
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
    audio = MusicManager()
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

    # Start game BGM
    audio.play_bgm("game_start_bgm", loop=True)

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

        # Checks for collisions between ship shots and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    #pygame.sprite.Sprite.kill(asteroid)
                    pygame.sprite.Sprite.kill(shot)

        # Check for collisions and end game if occurs
        for obj in asteroids:
            if obj.collision(player):
                print("Game Over!")
                audio.play_bgm("game_over_bgm")

                # Wait until the game over music finishes before exiting
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10) # Check every 10ms

                exit()   # Exit the game after the music finishes
                
        # Re-renders all objects on the screen (i.e..players, asteroids etc...)
        pygame.display.flip()

        # Limit FPS to 60
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()