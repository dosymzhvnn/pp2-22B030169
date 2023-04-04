import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Coin Collector")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
score = 0
# Set up the font
FONT = pygame.font.SysFont('Verdana', 36)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > WINDOW_HEIGHT:
            self.kill()

# Set up the game clock
clock = pygame.time.Clock()

# Set up the sprites
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()

# Set up the player
player_rect = pygame.Rect(WINDOW_WIDTH // 2 - 25, WINDOW_HEIGHT - 100, 50, 50)

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game
    all_sprites.update()

    # Add coins to the game
    if random.randint(1, 50) == 1:
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

    # Detect collisions between the player and the coins
    for coin in pygame.sprite.spritecollideany(player_rect, coins):
        score += 1

    # Draw the game
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, player_rect)
    all_sprites.draw(window)
    score_text = FONT.render("Score: {}".format(score), True, WHITE)
    window.blit(score_text, (10, 10))
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
