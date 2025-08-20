import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)
    Shot.containers = (shot_group, updatable_group, drawable_group)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT) / 2)
    asteroidfield = AsteroidField()

    while True: #infinite loop
        screen.fill("black")
        for drawable in drawable_group:
            drawable.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable_group.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for asteroid in asteroid_group:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

if __name__ == "__main__":
    main()
