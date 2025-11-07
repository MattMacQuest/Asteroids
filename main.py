import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    # Initialize Pygame modules
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    
    # Create groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Create new static Player containers
    Player.containers = (updatable, drawable)
    
    # Create new static Asteroid containers
    Asteroid.containers = (asteroids, updatable, drawable)
    
    # Create new static AsteroidField container
    AsteroidField.containers = (updatable)
    
    # Create new static shots container
    Shot.containers = (shots, drawable, updatable)
    
    # Creates the screen with size WIDTH and HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Create asteroidfield object
    asteroidfield = AsteroidField()
    
    # Game loop
    while True:
        # Log current game state
        log_state()
        
        # Checks for quit event and returns if found
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fill the screen with a single color (black in this case)
        pygame.Surface.fill(screen, (0, 0, 0))
        
        # Update objects
        updatable.update(dt)
        
        # Check for collisions
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.is_colliding(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()
        
        # Draw player
        # player.draw(screen)
        for item in drawable:
            item.draw(screen)
        
        # Updates all elements on the screen
        pygame.display.flip()
        
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
