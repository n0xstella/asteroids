# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    print('"Starting asteroids!"')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers(updatable, drawable)

    # Player activity
    Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    # Allow for the closing of a window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set the screen fill color to black and force it to refresh    
        screen.fill(color="black")

        # Limit FPS to 60
        dt = fps.tick(60) / 1000

        # Update players current position on screen
        updatable.update(dt)

        # Renders the player onto screen to match each frame
        drawable.draw(screen)
        
        # Re-renders all objects on the screen (i.e..players, asteroids etc...)
        pygame.display.flip()

if __name__ == "__main__":
    main()