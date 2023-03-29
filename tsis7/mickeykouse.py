import pygame
import datetime

pygame.init()
height = 600
width = 600

sc = pygame.display.set_mode((height , width))
pygame.display.set_caption('MICKEY MOUSE CLOCK', 'timesnewroman')

def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

background = pygame.image.load('images/main_clock.png') 
right = pygame.image.load('images/right_hand.png')
left = pygame.image.load('images/left_hand.png')

background = pygame.transform.scale(background , (600 , 600))
right = pygame.transform.scale(right , (300 , 300))
left = pygame.transform.scale(left , (300 , 300))
left = pygame.transform.flip(left , 180 , 180)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    sec = datetime.datetime.now().second
    min = datetime.datetime.now().minute
    
    x = (-6*min)%360
    y = ((-1)*sec * 6)%360
    
    rot_right , x = rot_center(right , x , 300 , 300)
    rot_left , y = rot_center(left , y , 300 , 300)
    
    sc.blit(background, (0 , 0))
    sc.blit(rot_right , x)
    sc.blit(rot_left , y)
    
    pygame.display.update()