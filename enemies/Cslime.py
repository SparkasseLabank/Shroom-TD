import pygame
import os
from enemies.Enemy import Enemy


class Cslime(Enemy):
    def __init__(self, x: float, y: float, screen_size: tuple) -> None:
        super().__init__(x, y, screen_size)
        """Sous-classe de l'ennemi slime cyan
        - x: nombre réel correspondant à la position x de la tour
        - y: nombre réel correspondant à la position y de la tour
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre"""
        self.max_speed = 15
        self.speed = 15
        self.image_path = os.path.join("assets", "enemies", "cyan_slime.png")
        self.image = pygame.image.tostring(pygame.transform.scale(pygame.image.load(
            self.image_path).convert_alpha(), (self.width, self.height)), "RGBA")
        self.health = 75
        self.max_health = 75
        self.resistance = {
            "Magic": 5,
            "Physical": 3,
        }
        self.max_resistance_magic = self.resistance["Magic"]
        self.max_resistance_physic = self.resistance["Physical"]
        self.damage = 7
        self.money_value = 30
        self.type = "Slime"
