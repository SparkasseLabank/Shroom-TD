import pygame
import os
from towers.projectiles.Projectile import Projectile


class Cshroom_projectile(Projectile):
    def __init__(
        self,
        x: float,
        y: float,
        target,
        screen_size: tuple,
        attack_value: int,
        attack_type: str,
    ) -> None:
        super().__init__(x, y, target, screen_size)
        """Sous-classe du projectile du Classic shroom
        - x: nombre réel correspondant à la coordonnée x de départ du projectile
        - y: nombre réel correspondant à la coordonnée y de départ du projectile
        - target: ennemi ciblé
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - attack_value: nombre entier correspondant aux dégats infligés à la cible
        - attack_type: chaine de caractère désignant le type d'attaque (Physique ou Magique)"""

        self.image = pygame.transform.scale(
            pygame.image.load(
                os.path.join(
                    "assets", "towers", "projectiles", "cshroom_projectile.png"
                )
            ).convert_alpha(),
            (screen_size[0] / 120, screen_size[0] / 120),
        )
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 15
        self.attack_value = attack_value
        self.attack_type = attack_type

    def attack(self) -> None:
        """Méthode pour attaquer la cible
        (Retirer du bouclier ou de la vie)"""

        if self.target.Bresistance():
            self.target.bouclier -= int(
                round(self.attack_value / self.target.resistance[self.attack_type])
            )

        else:
            self.target.health -= int(
                round(self.attack_value / self.target.resistance[self.attack_type])
            )
