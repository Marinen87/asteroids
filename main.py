import pygame
import sys
import player
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player1 = player.Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.Surface.fill(screen, color=(0, 0, 0))
        player1.update(dt)
        player1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
