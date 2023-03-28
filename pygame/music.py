import random
import pygame


pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play(0) 
#-1 - playing song infinitely
# 0 - playing song once
pygame.mixer.music.queue('next_song.mp3')

# Stopping song
pygame.mixer.music.stop()

effect = pygame.mixer.Sound('beep.wav')
effect.play()
      
      
def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()
    

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
    

_sound_library = {}
def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()