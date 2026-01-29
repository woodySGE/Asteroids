from constants import *
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import shot
import pygame
import sys

clock = pygame.time.Clock()



def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    shot.containers = (shots, drawable, updatable)
    field = AsteroidField()
    dt = 0


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Starting Asteroids with Screen width: {SCREEN_WIDTH}")
    print(f"Starting Asteroids with Screen height: {SCREEN_HEIGHT}")





    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for roids in asteroids:
            result = CircleShape.collides_with(player, roids)
            for bullay in shots:
                result2 = CircleShape.collides_with(bullay, roids)
                if result2 == True:
                    log_event("asteroid_shot")
                    #pygame.sprite.Sprite.kill(bullay)
                    #pygame.sprite.Sprite.kill(roids)         
                    Asteroid.Split(roids)           
                    print("HIIHIHIH HIT")
            if result == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for drawering in drawable:
            drawering.draw(screen)
        pygame.display.flip()
        timedstuff = clock.tick()
        dt = timedstuff / 1000


if __name__ == "__main__":
    main()
