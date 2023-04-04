import pygame
import time
pygame.init()
pygame.mixer.init()
height , width = 500 , 500
screen = pygame.display.set_mode((height , width))
running = True

current_music = 0
songs = ["musics/1.ogg" , "musics/2.ogg" , "musics/3.ogg"]
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
        current_music = (current_music - 1) % len(songs)
        pygame.mixer.music.load(songs[current_music])
        pygame.mixer.music.play()
        time.sleep(0.5)
    # next music
    elif pressed[pygame.K_RIGHT]:
        current_music = (current_music + 1) % len(songs)
        pygame.mixer.music.load(songs[current_music])
        pygame.mixer.music.play()
        time.sleep(0.5)
    # stop music
    elif pressed[pygame.K_SPACE]:
        pygame.mixer.music.pause()
        time.sleep(0.5)
    # play music
    elif pressed[pygame.K_RETURN]:
        pygame.mixer.music.load(songs[current_music])
        pygame.mixer.music.play(0)
        time.sleep(0.5)
    screen.fill((225,225,225))
    pygame.display.flip()
    


