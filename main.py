import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')

        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print('Game over!')
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

if __name__ == '__main__':
    main()