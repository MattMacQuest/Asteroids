import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    # Initialize Pygame modules
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    
    # Creates the screen with size WIDTH and HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
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
        
        # Update player
        player.update(dt)
        
        # Draw player
        player.draw(screen)
        
        # Updates all elements on the screen
        pygame.display.flip()
        
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
