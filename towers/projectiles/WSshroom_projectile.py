import pygame
import os
from towers.projectiles.Projectile import Projectile


class WSshroom_projectile(Projectile):
    def __init__(self, x: float, y: float, target, screen_size: tuple, attack_value: int, attack_type: str, speed_modifier: float) -> None:
        super().__init__(x, y, target, screen_size)
        """Sous-classe du projectile du Water Strider Shroom
        - x: nombre réel correspondant à la coordonnée x de départ du projectile
        - y: nombre réel correspondant à la coordonnée y de départ du projectile
        - target: ennemi ciblé
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - attack_value: nombre entier correspondant aux dégats infligés à la cible
        - attack_type: chaine de caractère désignant le type d'attaque (Physique ou Magique)
        - speed_modifier: nombre réel correspondant au ralentissement que la cible subi"""

        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            "assets", "towers", "projectiles", "wsshroom_projectile.png")).convert_alpha(), (screen_size[0]/120, screen_size[0]/120))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 15
        self.attack_value = attack_value
        self.attack_type = attack_type
        self.speed_modifier = speed_modifier

    def attack(self) -> None:
        """Méthode pour attaquer la cible
        (Retirer du bouclier ou de la vie ainsi que la ralentir)"""

        if self.target.Bresistance():
            self.target.bouclier -= int(round(self.attack_value /
                                        self.target.resistance[self.attack_type]))

        else:
            self.target.health -= int(round(self.attack_value /
                                      self.target.resistance[self.attack_type]))
            for status in self.target.status:
                if status[0] == "slowed" and status[1] <= 120:
                    self.target.status[self.target.status.index(
                        status)][1] = 120
                    if status[2] > self.speed_modifier:
                        self.target.status[self.target.status.index(
                            status)][2] = self.speed_modifier
                    return
            self.target.status.append(["slowed", 120, self.speed_modifier])
