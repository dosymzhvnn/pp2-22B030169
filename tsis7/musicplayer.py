import pygame
pygame.init()
height , width = 500 , 500
screen = pygame.display.set_mode((height , width))
running = True

clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        
        
    pressed = pygame.key.get_pressed()
    # previous music
    if pressed[pygame.K_LEFT]:    
        pass
    # next music
    elif pressed[pygame.K_RIGHT]:
        pass
    # stop music
    elif pressed[pygame.K_SPACE]:
        pass
    # play music
    elif pressed[pygame.K_KP_ENTER]:
        pass
    
    screen.fill((225,225,225))
    pygame.display.flip()
    clock.tick(60)
    


