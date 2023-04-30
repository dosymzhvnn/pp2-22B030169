from config import host , user, database ,password 
import pygame
import math
import random
import time
import sys
import psycopg2

conn = psycopg2.connect(
    host = host
    ,database = database
    ,user = user
    ,password = password
)
conn.autocommit = True
cur = conn.cursor()
with conn.cursor() as cursor:
    cur.execute("""CREATE TABLE IF NOT EXISTS user_score(
    id serial PRIMARY KEY
    ,name varchar(50)
    ,score varchar(20)
    ,level varchar(20)
    ) """)

def add_data(name, score , level):
    with conn.cursor() as cursor:
        cur.execute("""INSERT INTO user_score(name , score , level) 
                    VALUES (%s , %s, %s)
                    """ , (name , score , level))

def search_name(name):
    with conn.cursor() as cursor:
        cur.execute("SELECT * FROM user_score WHERE name ILIKE %s", (name,))
        rows = cur.fetchall()
        return rows
    
def delete_score(name):
    with conn.cursor() as cursor:
        cur.execute("DELETE FROM user_score WHERE name ILIKE %s", (name,))

# CONSTANTS
WIDTH = 640
HEIGHT = 640
BLOCK_SIZE = 20
global speed
speed = 3
SQUARES = int(WIDTH/BLOCK_SIZE)
clock = pygame.time.Clock()

# COLORS
BG1 = (156, 210, 54)
BG2 = (147, 203, 57)
RED = (255, 0, 0)
BLUE = (0, 0, 50)
BLACK = (0, 0, 0)

def game_over(screen ,name , score , level):
    go_font = pygame.font.SysFont('timesnewroman' , 50)
    go_surf = go_font.render(f'Your Score is :' + str(score) , True , BLACK)
    
    go_rect = go_surf.get_rect()
    go_rect.midtop = (HEIGHT // 2 , WIDTH // 4)
    screen.blit(go_surf , go_rect)
    add_data(name , score , level)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

class Snake:

    def __init__(self):
        self.color = BLUE
        self.headX = random.randrange(0, WIDTH, BLOCK_SIZE)
        self.headY = random.randrange(0, HEIGHT, BLOCK_SIZE)
        self.bodies = []
        self.body_color = 50
        self.state = "STOP"  # STOP, UP, DOWN, RIGHT, LEFT

    def move_head(self):
        if self.state == "UP":
            self.headY -= BLOCK_SIZE

        elif self.state == "DOWN":
            self.headY += BLOCK_SIZE

        elif self.state == "RIGHT":
            self.headX += BLOCK_SIZE

        elif self.state == "LEFT":
            self.headX -= BLOCK_SIZE

    def move_body(self):
        if len(self.bodies) > 0:
            for i in range(len(self.bodies)-1, -1, -1):
                if i == 0:
                    self.bodies[0].posX = self.headX
                    self.bodies[0].posY = self.headY
                else:
                    self.bodies[i].posX = self.bodies[i-1].posX
                    self.bodies[i].posY = self.bodies[i-1].posY

    def add_body(self):
        self.body_color += 10
        body = Body((0, 0, self.body_color), self.headX, self.headY)
        self.bodies.append(body)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.headX,
                         self.headY, BLOCK_SIZE, BLOCK_SIZE))
        if len(self.bodies) > 0:
            for body in self.bodies:
                body.draw(surface)

    def die(self):
        self.headX = random.randrange(0, WIDTH, BLOCK_SIZE)
        self.headY = random.randrange(0, HEIGHT, BLOCK_SIZE)
        self.bodies = []
        self.body_color = 50
        self.state = "STOP"


class Body:

    def __init__(self, color, posX, posY):
        self.color = color
        self.posX = posX
        self.posY = posY

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.posX,
                         self.posY, BLOCK_SIZE, BLOCK_SIZE))


class Food:

    def __init__(self):
        self.color = RED
        self.spawn()
        self.time = 50
        
    def update(self):
        if self.time == 0:
            self.time = 50
        else:
            self.time -= 1
        if self.time == 0:
            self.spawn()

    def spawn(self):
        self.posX = random.randrange(0, WIDTH, BLOCK_SIZE)
        self.posY = random.randrange(0, HEIGHT, BLOCK_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.posX,
                         self.posY, BLOCK_SIZE, BLOCK_SIZE))

class Background:

    def draw(self, surface):
        surface.fill(BG1)
        counter = 0
        for row in range(SQUARES):
            for col in range(SQUARES):
                if counter % 2 == 0:
                    pygame.draw.rect(
                        surface, BG2, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                if col != SQUARES - 1:
                    counter += 1


class Collision:

    def between_snake_and_food(self, snake, food):
        distance = math.sqrt(math.pow(
            (snake.headX - food.posX), 2) + math.pow((snake.headY - food.posY), 2))
        return distance < BLOCK_SIZE

    def between_snake_and_walls(self, snake):
        if snake.headX < 0 or snake.headX > WIDTH - BLOCK_SIZE or snake.headY < 0 or snake.headY > HEIGHT - BLOCK_SIZE:
            return True
        return False

    def between_head_and_body(self, snake):
        for body in snake.bodies:
            distance = math.sqrt(math.pow(
                (snake.headX - body.posX), 2) + math.pow((snake.headY - body.posY), 2))
            if distance < BLOCK_SIZE:
                return True
        return False


class Score:
    def __init__(self, surface):
        self.points = 0
        self.levels = 0
        self.font = pygame.font.SysFont('monospace', 30, bold=False)
        self.speed = 10

    def increase(self):
        self.randompoints = random.randint(1, 5)
        self.points += self.randompoints

    def reset(self):
        self.points = 0
        self.levels = 0
        self.speed = 10

    def boost(self):
        if self.points % 5 == 0:
            self.levels += 1
            self.speed += 10

    def show(self, surface):
        lbl = self.font.render('Score:' + str(self.points), 1, BLACK)
        surface.blit(lbl, (5, 5))
        level = self.font.render(f'Level:' + str(self.levels), 1, BLACK)
        surface.blit(level, (WIDTH - 135, 5))
        
class Wall:
    def __init__(self, level):
        self.level = level
        self.walls = []

    def create_walls(self):
        if self.level == 1:
            # создание стен для уровня 1
            self.walls.append(pygame.Rect(0, 0, BLOCK_SIZE, HEIGHT))
            self.walls.append(pygame.Rect(0, 0, WIDTH, BLOCK_SIZE))
            self.walls.append(pygame.Rect(WIDTH - BLOCK_SIZE, 0, BLOCK_SIZE, HEIGHT))
            self.walls.append(pygame.Rect(0, HEIGHT - BLOCK_SIZE, WIDTH, BLOCK_SIZE))
        elif self.level == 2:
            # создание стен для уровня 2
            self.walls.append(pygame.Rect(0, 0, BLOCK_SIZE, HEIGHT))
            self.walls.append(pygame.Rect(0, 0, WIDTH, BLOCK_SIZE))
            self.walls.append(pygame.Rect(WIDTH - BLOCK_SIZE, 0, BLOCK_SIZE, HEIGHT))
            self.walls.append(pygame.Rect(0, HEIGHT - BLOCK_SIZE, WIDTH, BLOCK_SIZE))
        # добавьте стены для других уровней здесь
        else:
            pass

    def draw(self, surface):
        for wall in self.walls:
            pygame.draw.rect(surface, BLACK, wall)
class Name():
    def __init__(self,screen,name , score):
        self.screen = screen
        self.name = name
    def enter_name(self , screen):
        font = pygame.font.SysFont(None, 100)
        input_active = True

        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.name = self.name[:-1]
                    else:
                        self.name += event.unicode

            self.screen.fill(0)
            text_surf = font.render(self.name, True, (255, 0, 0))
            self.screen.blit(text_surf, text_surf.get_rect(center=self.screen.get_rect().center))
            pygame.display.flip()

        input_active = True
        row = search_name(self.name)
        if row:
            score = row[0][1]
            font = pygame.font.SysFont(None, 40)
            while input_active:
                pressed = pygame.key.get_pressed()
                score_surf = font.render(f"Welcome back, {self.name}! Your current score is {score}.", True, (255, 0, 0))
                text_surf = font.render("Do you want to renew your scores?(Y/N)", True, (255, 0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and input_active:
                        if event.key == pygame.K_y:
                            Score.points = 0
                            delete_score(self.name)
                            input_active = False
                        if event.key == pygame.K_n:
                            quit()
                self.screen.fill(0)
                self.screen.blit(score_surf, score_surf.get_rect(center=(360, 200)))
                self.screen.blit(text_surf, text_surf.get_rect(center=self.screen.get_rect().center))
                pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SNAKE")

    # OBJECTS
    name = ""
    snake = Snake()
    food = Food()
    background = Background()
    collision = Collision()
    score = Score(screen)
    names = Name(screen, name , score.points)
    names.enter_name(screen)
    
    
    # MainLoop
    while True:
        background.draw(screen)
        snake.draw(screen)
        food.draw(screen)
        score.show(screen)
        walls = Wall(score.levels)
        walls.create_walls()
        walls.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake.state != "DOWN":
                        snake.state = "UP"

                elif event.key == pygame.K_DOWN:
                    if snake.state != "UP":
                        snake.state = "DOWN"

                elif event.key == pygame.K_RIGHT:
                    if snake.state != "LEFT":
                        snake.state = "RIGHT"

                elif event.key == pygame.K_LEFT:
                    if snake.state != "RIGHT":
                        snake.state = "LEFT"

                elif event.key == pygame.K_p:
                    snake.state = "STOP"
                    
                elif event.key == pygame.K_ESCAPE:
                    add_data(names.name, score.points , score.levels)
                    quit()
                    
        if collision.between_snake_and_food(snake, food):
            food.spawn()
            snake.add_body()
            score.increase()
            score.boost()
            food.time = 50
        else:
            food.update()
        

        # movement
        if snake.state != "STOP":
            snake.move_body()
            snake.move_head()
        
        if collision.between_snake_and_walls(snake):
            # lose
            game_over(screen ,names.name , score.points , score.levels)
            add_data(names.name , score.points , score.levels)
            snake.die()
            food.spawn()
            score.reset()
            
           

        if collision.between_head_and_body(snake):
            # lose
            game_over(screen , score.points)
            add_data(names.name , score.points , score.levels)
            snake.die()
            food.spawn()
            score.reset()
        
        clock.tick(score.speed)
        pygame.display.update()


main()
