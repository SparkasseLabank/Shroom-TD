import pygame
import os
from towers.Tower import Tower


class Sshroom(Tower):
    def __init__(self, x: float, y: float, screen_size: tuple, difficulty: str) -> None:
        super().__init__(x, y, screen_size, difficulty)
        """Sous-classe de la tour Stun shroom
        - x: nombre réel correspondant à la position x de la tour
        - y: nombre réel correspondant à la position y de la tour
        screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - difficulty: chaine de caractère correspondant au fichier json des prix de la tour et upgrade"""

        self.name = "Stun Shroom"
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            "assets", "towers", "stun_shroom", "stun_shroom.png")), (self.width, self.height))
        self.cost = self.upgrades[self.name]["base"]["cost"]
        self.value = self.cost
        self.attack_type = "Magic"
        self.placement_type = "Ground"
        self.shot = False
        self.range = self.screen_size[0]/10.2
        self.range_circle = pygame.Surface(
            (self.range*2, self.range*2), pygame.SRCALPHA).convert_alpha()
        pygame.draw.circle(self.range_circle, (50, 50, 50, 128),
                           (self.range, self.range), self.range)
        self.attack_value = self.upgrades[self.name]["base"]["attack_value"]
        self.shoot_interval = self.upgrades[self.name]["base"]["shoot_interval"]
        self.stun_time = self.upgrades[self.name]["base"]["stun_time"]
        self.upgrade_cost = [self.upgrades[self.name]["0"][str(
            self.level[0]+1)]["upgrade_cost"], self.upgrades[self.name]["1"][str(self.level[1]+1)]["upgrade_cost"]]
        self.sell_cost = int(self.value*0.8)

    def main_attack(self, target=None, enemies=None, current_tick=0, projectiles: list = None) -> list:
        """Gestion de tir de la tour, renvoie le projectile crée par le tir de la tour
        - target: ennemi ciblé
        - enemies: liste des ennemis ciblés
        - current_tick: entier correspondant au tick auquel la méthode est appelée afin de gérer l'intervalle de tir
        - projectiles: liste des projectiles à laquelle on ajoutera le projectile renvoyé"""

        if current_tick - self.last_shot_time > self.shoot_interval:
            for enemy_to_stun in enemies:
                if not enemy_to_stun.Bresistance():
                    enemy_to_stun.speed = 0
                    if not self.shot:
                        enemy_to_stun.health -= int(
                            round(self.attack_value / enemy_to_stun.resistance[self.attack_type]))
            self.shot = True
            if current_tick - self.last_shot_time > self.shoot_interval + self.stun_time:
                for enemy_to_stun in enemies:
                    enemy_to_stun.speed = enemy_to_stun.max_speed
                self.last_shot_time = current_tick
                self.shot = False
