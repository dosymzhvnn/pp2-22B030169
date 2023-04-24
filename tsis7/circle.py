import pygame

pygame.init()
width , height = 600 , 600
screen = pygame.display.set_mode((width , height))


running = True
x = 50
y = 50
radius = 25


clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
           
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 20
    elif pressed[pygame.K_DOWN]:
        y += 20
    elif pressed[pygame.K_LEFT]:
        x -= 20
    elif pressed[pygame.K_RIGHT]:
        x += 20
    
    if x - radius< 0:
        x = radius
    elif x + radius > width:
        x = width - radius
    if y - radius < 0:
        y = radius
    elif y + radius > height:
        y = height - radius
    
    screen.fill((225, 225,225))

    pygame.draw.circle(screen ,(225 , 0 , 0) , (x , y) , radius)
    pygame.display.flip()
    clock.tick(30)   
               
     
     
     
     
     
     
     
     
     
     
     
     
     
 
 