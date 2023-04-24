import pygame
import os
from enemies.Enemy import Enemy


class Oslime(Enemy):
    def __init__(self, x: float, y: float, screen_size: tuple) -> None:
        super().__init__(x, y, screen_size)
        """Sous-classe de l'ennemi slime orange
        - x: nombre réel correspondant à la position x de la tour
        - y: nombre réel correspondant à la position y de la tour
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre"""
        self.max_speed = 6.5
        self.speed = 6.5
        self.image_path = os.path.join("assets", "enemies", "orange_slime.png")
        self.image = pygame.image.tostring(pygame.transform.scale(pygame.image.load(
            self.image_path).convert_alpha(), (self.width, self.height)), "RGBA")
        self.health = 60
        self.max_health = 60
        self.resistance = {
            "Magic": 4,
            "Physical": 4,
        }
        self.max_resistance_magic = self.resistance["Magic"]
        self.max_resistance_physic = self.resistance["Physical"]
        self.damage = 1
        self.money_value = 15
        self.type = "Slime"
