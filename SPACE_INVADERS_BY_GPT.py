#This code is copied from the chat GPT, need to understand the code properly.


#install pygame
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_SPEED = 5
ALIEN_SIZE = 40
ALIEN_SPEED = 2
BULLET_SPEED = 8
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load images
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (PLAYER_SIZE, PLAYER_SIZE))
alien_img = pygame.image.load("alien.png")
alien_img = pygame.transform.scale(alien_img, (ALIEN_SIZE, ALIEN_SIZE))

# Initialize player position
player_x = (WIDTH - PLAYER_SIZE) // 2
player_y = HEIGHT - PLAYER_SIZE

# Create lists to store aliens and bullets
aliens = []
bullets = []

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Game over flag
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                player_x += PLAYER_SPEED
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + PLAYER_SIZE // 2 - 2
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])

    # Move aliens
    for alien in aliens:
        alien[1] += ALIEN_SPEED

    # Remove off-screen aliens
    aliens = [alien for alien in aliens if alien[1] < HEIGHT]

    # Move bullets
    for bullet in bullets:
        bullet[1] -= BULLET_SPEED

    # Remove off-screen bullets
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # Check for collisions between bullets and aliens
    collisions = pygame.sprite.spritecollideany(player, aliens)
    if collisions:
        game_over = True

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the player
    window.blit(player_img, (player_x, player_y))

    # Draw the aliens
    for alien in aliens:
        window.blit(alien_img, (alien[0], alien[1]))

    # Draw the bullets
    for bullet in bullets:
        pygame.draw.rect(window, YELLOW, [bullet[0], bullet[1], 4, 10])

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
