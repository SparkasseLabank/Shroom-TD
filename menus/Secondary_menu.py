import pygame
import os


class Secondary_menu:
    def __init__(self, screen_size: tuple) -> None:
        """Classe mère Secondary_menu:
        Cette classe représente un menu secondaire
        - screen_size: tuple contenant la largeur et la hauteur de l'écran"""

        self.screen_size = screen_size
        self.image_x = self.screen_size[0]/4.1
        self.image_y = self.screen_size[1]/4
        self.image_width = self.screen_size[0]/2
        self.image_height = self.screen_size[1]/2
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            "assets", "other", "panneau.png")).convert_alpha(), (self.image_width, self.image_height))
