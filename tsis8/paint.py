import pygame

WIDTH , HEIGHT = 800 , 800
SCREEN = pygame.display.set_mode((WIDTH , HEIGHT))
WHITE = (255 , 255 , 255)
BLACK = (0 , 0 , 0)
class GameObject:
    def draw(self):
        raise NotImplementedError

    def handle(self):
        raise NotImplementedError


# если ты фигуру изволишь изменить - то унаследуй (pygame.sprite.Sprite)
class Button:
    def __init__(self):
        # super().__init__() и вот это раскомментируй
        self.rect0 = pygame.draw.rect(
            SCREEN,
            WHITE,
            (WIDTH // 2 , 20, 40, 40)
        )
        self.rect = pygame.draw.rect(
            SCREEN,
            WHITE,
            (WIDTH // 2 - 20, 20, 40, 40)
        )

    def draw(self):
        self.rect0 = pygame.draw.rect(
            SCREEN,
            WHITE,
            (WIDTH // 2 + 50, 20, 40, 40)
        )
        self.rect = pygame.draw.rect(
            SCREEN,
            WHITE,
            (WIDTH // 2, 20, 40, 40)
        )

class Pen(GameObject):
    def __init__(self, *args, **kwargs):
        self.points = []  # [(x1, y1), (x2, y2)]

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            pygame.draw.line(
                SCREEN,
                WHITE,
                start_pos=point,  # self.points[idx]
                end_pos=self.points[idx + 1],
                width=5,
            )

    def handle(self, mouse_pos):
        self.points.append(mouse_pos)


class Rectangle(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(
            SCREEN,
            WHITE,
            (
                start_pos_x,
                start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos


class Square(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        # Get the dimensions of the square
        square_size = min(end_pos_x - start_pos_x, end_pos_y - start_pos_y)

        # Calculate the starting position for the square so that it is centered
        square_start_pos_x = start_pos_x + \
            (end_pos_x - start_pos_x - square_size) // 2
        square_start_pos_y = start_pos_y + \
            (end_pos_y - start_pos_y - square_size) // 2

        pygame.draw.rect(
            SCREEN,
            WHITE,
            (
                square_start_pos_x,
                square_start_pos_y,
                square_size,
                square_size
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

        
def main():
    running = True
    active_obj = None
    button = Button()
    objects = [
        button
    ]
    clock = pygame.time.Clock()
    current_shape = 'pen'

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'rectangle'
                elif button.rect0.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'pen'
                else:
                    if current_shape == 'pen':
                        active_obj = Pen(start_pos=event.pos)
                    elif current_shape == 'rectangle':
                        active_obj = Rectangle(start_pos=event.pos)
                    
            if event.type == pygame.MOUSEMOTION and active_obj is not None:
                # active_obj.points.append(pygame.mouse.get_pos())
                active_obj.handle(mouse_pos=pygame.mouse.get_pos())
                # active_obj.points => raise
                active_obj.draw()

            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
                objects.append(active_obj)
                active_obj = None

        for obj in objects:
            obj.draw()

        clock.tick(30)
        pygame.display.flip()


if __name__ == '__main__':
    main()
