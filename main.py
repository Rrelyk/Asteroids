import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    a_field = AsteroidField()

    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")
        #loop groups
        for obj in drawable:
            obj.draw(screen)
        for obj in updateable:
            obj.update(dt)
        for obj in asteroids:
            if obj.collision(p1) == True:
                print("Game Over")
                exit()
            for shot in shots:
                if obj.collision(shot) == True:
                    obj.split()
                    shot.kill()       

        pygame.display.flip()

        dt = clock.tick(60) /1000


if __name__ == "__main__":
    main()
