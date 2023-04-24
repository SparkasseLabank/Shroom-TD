import pygame
import os
from towers.projectiles.Projectile import Projectile


class Bshroom_projectile(Projectile):
    def __init__(self, x: float, y: float, target, screen_size: tuple, attack_value: int, attack_type: str, enemies: list, aoe: int) -> None:
        super().__init__(x, y, target, screen_size)
        """Sous-classe du projectile du Boom shroom
        - x: nombre réel correspondant à la coordonnée x de départ du projectile
        - y: nombre réel correspondant à la coordonnée y de départ du projectile
        - target: ennemi ciblé
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - attack_value: nombre entier correspondant aux dégats infligés à la cible
        - attack_type: chaine de caractère désignant le type d'attaque (Physique ou Magique)
        - enemies: liste des ennemis présents sur la map
        - aoe: nombre entier correspondant au rayon du cercle de portée de l'explosion de la tour"""

        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            "assets", "towers", "projectiles", "bshroom_projectile.png")).convert_alpha(), (screen_size[0]/60, screen_size[0]/60))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 15
        self.attack_value = attack_value
        self.attack_type = attack_type
        self.enemies = enemies
        self.aoe = aoe

    def attack(self) -> None:
        """Méthode pour attaquer la cible
        (Retirer du bouclier ou de la vie a toutes les cibles dans la portée de l'explosion de la tour)"""

        for enemy in self.enemies:
            if self.target.x + self.aoe >= enemy.x >= self.target.x - self.aoe and self.target.y + self.aoe >= enemy.y >= self.target.y - self.aoe:
                if enemy.Bresistance():
                    enemy.bouclier -= int(round(self.attack_value /
                                          enemy.resistance[self.attack_type]))

                else:
                    enemy.health -= int(round(self.attack_value /
                                        enemy.resistance[self.attack_type]))
