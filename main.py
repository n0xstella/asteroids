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
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    # Allow for the closing of a window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set the screen fill color to black and force it to refresh    
        screen.fill(color="black")

        # Sets the delta time to a value of 60 (60k ms) and converts it to seconds.
        # Essentially this is the FPS (frames per second)
        dt = fps.tick(60) / 1000

        # Update players current position on screen
        player.update(dt)

        # Renders the player onto screen to match each frame
        player.draw(screen)
        
        # Re-renders all objects on the screen (i.e..players, asteroids etc...)
        pygame.display.flip()





if __name__ == "__main__":
    main()