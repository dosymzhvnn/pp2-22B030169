import pygame


pygame.init()
pygame.display.set_caption("WELCOME!!!")
screen = pygame.display.set_mode((600 , 500))

clock = pygame.time.Clock()

running  = True

font = pygame.font.SysFont("timesnewroman" , 50)
text = font.render("YOU CAN DO IT" , True , (0, 100 , 115))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        
        screen.fill((255,255,255))
        screen.blit(text , (
            320 - text.get_width() // 2,
            240 - text.get_width() // 2,))
        
    pygame.display.flip()
    clock.tick(144)
        