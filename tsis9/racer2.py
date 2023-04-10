import random
import time
import pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Street Racer v0')
background = pygame.image.load("./images/AnimatedStreet.png")
score_font = pygame.font.SysFont("Verdana", 30)
FONT = pygame.font.Font(None, 36)
# scorecoin = 0
# score = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('images/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(0, WIDTH - self.rect.width), 0
        )
        self.score = 0
        self.cntcoin = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.score += 1
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            # self.rect.y = random.randint()

            if self.cntcoin % 3 == 0 and self.cntcoin > 0:
                self.speed += 10


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('images/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)
        self.scorecoin = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x >= self.speed:
            self.rect.x -= self.speed
        if pressed[pygame.K_RIGHT] and self.rect.x + self.rect.width + self.speed <= WIDTH:
            self.rect.x += self.speed
        if pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        if pressed[pygame.K_DOWN]:
            self.rect.y += self.speed

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('images/coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(0, WIDTH - self.rect.width), 0
        )
        self.scorecoin = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH - self.rect.width)

    def spawn(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = 0


def main():
    running = True
    player = Player()
    enemy = Enemy()
    coin = Coin()

    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    coins = pygame.sprite.Group()
    coins.add(coin)

    pygame.mixer.music.load('musics/background.wav')
    pygame.mixer.music.play(-1)
    while running:
        SCREEN.blit(background, (0, 0))
       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        enemy.update()
        coin.update()

        player.draw(SCREEN)
        enemy.draw(SCREEN)
        coin.draw(SCREEN)

        score1 = score_font.render(
            f" Your Score: {str(enemy.score)}", True, BLACK)
        SCREEN.blit(score1, (0, 0))
        score2 = score_font.render(
            f"Coins: {str(player.scorecoin)}", True, BLACK)
        SCREEN.blit(score2, (WIDTH - 155, 0))

        if pygame.sprite.spritecollideany(player, coins):
            weightofcoin = random.randint(0, 10)
            player.scorecoin += weightofcoin
            enemy.cntcoin += 1
            coin.spawn()

        if pygame.sprite.spritecollideany(player, enemies):
            pygame.mixer.Sound('musics/crash.wav').play(0)
            time.sleep(0.6)

            SCREEN.fill(RED)
            font = pygame.font.SysFont('Verdana', 60)
            game_over = font.render('GAME OVER', True, BLACK)
            SCREEN.blit(game_over, (30, 250))
            running = False

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()