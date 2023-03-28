import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

running = True
x = 30
y = 30

clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
            
            
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 3
    elif pressed[pygame.K_DOWN]:
        y += 3
    elif pressed[pygame.K_RIGHT]:
        x += 3
    elif pressed[pygame.K_LEFT]:
        x -= 3
    
    screen.fill((0, 0, 0))
    
    pygame.draw.line(screen , (225,225 ,225) , (100 , 100) , (200 , 200 ) , width= 10)
    pygame.draw.rect(screen ,(225 , 0 , 0),pygame.Rect(x,y,20,20))
    pygame.draw.circle(screen ,(225 , 220 , 140) , (50 , 50) , 10 , width=5)
    pygame.draw.polygon(screen , (0 , 0 , 225) , ((20 , 20), (40 , 40) , (20 , 40)))
    
    
    pygame.display.flip()
    clock.tick(60)
            