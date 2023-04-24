import pygame
import os
from towers.projectiles.Projectile import Projectile


class SPshroom_projectile(Projectile):
    def __init__(self, x: float, y: float, target, screen_size: tuple, attack_value: int, attack_type: str, creator, speed: int) -> None:
        super().__init__(x, y, target, screen_size)
        """Sous-classe du projectile du Spirit_shroom
        - x: nombre réel correspondant à la coordonnée x de départ du projectile
        - y: nombre réel correspondant à la coordonnée y de départ du projectile
        - target: ennemi ciblé
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - attack_value: nombre entier correspondant aux dégats infligés à la cible
        - attack_type: chaine de caractère désignant le type d'attaque (Physique ou Magique)
        - creator: spirit shroom ayant créé le projectile
        - speed: nombre entier correspondant à la vitesse du projectile"""

        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            "assets", "towers", "projectiles", "spshroom_projectile.png")).convert_alpha(), (screen_size[0]/60, screen_size[0]/60))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = speed
        self.attack_value = attack_value
        self.attack_type = attack_type
        self.creator = creator
        self.return_to_sender = True

    def attack(self) -> None:
        """Méthode pour attaquer la cible
        (Retirer du bouclier ou de la vie)"""

        if self.target != self.creator:
            if self.target.Bresistance():
                self.target.bouclier -= int(round(self.attack_value /
                                            self.target.resistance[self.attack_type]))

            else:
                self.target.health -= int(round(self.attack_value /
                                          self.target.resistance[self.attack_type]))

    def checked(self) -> bool:
        """Méthode qui renvoie True si la cible est le créateur du projectile et si le projectile est en collision avec son créateur"""
        return self.target.x <= self.x <= self.target.x + self.target.width and self.target.y <= self.y <= self.target.y + self.target.height and self.target == self.creator

    def enemy_check(self, enemy) -> bool:
        """Méthode qui renvoie True si le projectile est en collision avec l'ennemi ciblé"""
        return enemy.x <= self.x <= enemy.x + enemy.width and enemy.y <= self.y <= enemy.y + enemy.height
