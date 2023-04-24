import pygame
import os
from random import choice


try:
    pygame.mixer.init()
except pygame.error:
    sound_initialized = False
else:
    sound_initialized = True
    

def play_sound(sound, volume:float, state:bool) -> None:
    """Fonction pour jouer un son si le son est initialisé
    - sound: son pygame joué
    - volume: nombre réel correspondant au volume voulu pour le son joué
    - state: booléen correspondant à l'état du son actuel qui décide donc si le son sera joué ou non"""

    if sound_initialized and state:
        if isinstance(sound, list):
            given_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "sound_effects", choice(sound)))
            given_sound.set_volume(volume)
            given_sound.play()
        else:
            given_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "sound_effects", sound))
            given_sound.set_volume(volume)
            given_sound.play()


def create_music(music):
    """Fonction qui crée une musique si le son est bien initialisé
    - music: musique créée"""

    if sound_initialized:
        return music
    return None


def stop_music(music) -> None:
    """Fonction qui arrête la musique si elle existe
    - music: musique arrêtée"""

    if music is not None:
        music.stop()


def play_music(music, state:bool) -> None:
    """Fonction qui joue la musique si elle existe et si le son est activée
    - music: musique jouée
    - state: booléen correspondant à l'état du son actuel qui décide donc si le son sera joué ou non"""

    if music is not None and state:
        music.set_volume(0.05)
        music.play(-1)


def disable_music(music) -> None:
    """Fonction qui désactive la musique si elle existe
    - music: musique désactivée"""

    if music is not None:
        music.set_volume(0)


def enable_music(music) -> None:
    """Fonction qui active la musique si elle existe
    - music: musique activée"""

    if music is not None:
        music.set_volume(0.05)