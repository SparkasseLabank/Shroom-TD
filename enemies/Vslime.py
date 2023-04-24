import pygame
import os
from enemies.Enemy import Enemy


class Vslime(Enemy):
    def __init__(self, x: float, y: float, screen_size: tuple) -> None:
        super().__init__(x, y, screen_size)
        """Sous-classe de l'ennemi slime violet
        - x: nombre réel correspondant à la position x de la tour
        - y: nombre réel correspondant à la position y de la tour
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre"""
        self.max_speed = 7
        self.speed = 7
        self.image_path = os.path.join("assets", "enemies", "violet_slime.png")
        self.image = pygame.image.tostring(pygame.transform.scale(pygame.image.load(
            self.image_path).convert_alpha(), (self.width, self.height)), "RGBA")
        self.health = 100
        self.max_health = 100
        self.resistance = {
            "Magic": 1000,
            "Physical": 4,
        }
        self.max_resistance_magic = self.resistance["Magic"]
        self.max_resistance_physic = self.resistance["Physical"]
        self.damage = 5
        self.money_value = 30
        self.type = "Slime"
