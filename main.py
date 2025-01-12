import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    p1 = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    updatable.add(p1)
    drawable.add(p1)

    p1.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.Surface.fill(screen, color=(0, 0, 0))
        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
