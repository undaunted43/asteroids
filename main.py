import pygame
import player
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =  pygame.time.Clock()
    dt = 0

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player_ = player.Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
        pygame.display.flip()
        value_ = clock.tick(60)
        dt = value_/1000
        player_.draw(screen)

    

if __name__ == "__main__":
    main()
