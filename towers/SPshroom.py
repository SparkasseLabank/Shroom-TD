import pygame
import os
from towers.Tower import Tower
from towers.projectiles.SPshroom_projectile import SPshroom_projectile


class SPshroom(Tower):
    def __init__(self, x: float, y: float, screen_size: tuple, difficulty: str) -> None:
        super().__init__(x, y, screen_size, difficulty)
        """Sous-classe de la tour Spirit shroom
        - x: nombre réel correspondant à la position x de la tour
        - y: nombre réel correspondant à la position y de la tour
        screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - difficulty: chaine de caractère correspondant au fichier json des prix de la tour et upgrade"""

        self.name = "Spirit Shroom"
        self.images = [pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "spirit_shroom", "spirit_shroom.png")).convert_alpha(), (self.width, self.height)),
                       pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "spirit_shroom", "spirit_shroom2.png")).convert_alpha(), (self.width, self.height))]
        self.image = self.images[0]
        self.cost = self.upgrades[self.name]["base"]["cost"]
        self.value = self.cost
        self.attack_type = "Magic"
        self.placement_type = "Ground"
        self.orb = True
        self.enemy_damaged = []
        self.range = self.screen_size[0]/5.75
        self.range_circle = pygame.Surface(
            (self.range*2, self.range*2), pygame.SRCALPHA).convert_alpha()
        pygame.draw.circle(self.range_circle, (50, 50, 50, 128),
                           (self.range, self.range), self.range)
        self.attack_value = self.upgrades[self.name]["base"]["attack_value"]
        self.projectile_speed = self.upgrades[self.name]["base"]["projectile_speed"]
        self.upgrade_cost = [self.upgrades[self.name]["0"][str(
            self.level[0]+1)]["upgrade_cost"], self.upgrades[self.name]["1"][str(self.level[1]+1)]["upgrade_cost"]]
        self.sell_cost = int(self.value*0.8)

    def reset_sprite(self):
        self.image = self.images[0]

    def main_attack(self, target, enemies=None, current_tick=0, projectiles=None) -> list:
        """Gestion de tir de la tour, renvoie le projectile crée par le tir de la tour
        - target: ennemi ciblé
        - enemies: liste des ennemis ciblés
        - current_tick: entier correspondant au tick auquel la méthode est appelée afin de gérer l'intervalle de tir
        - projectiles: liste des projectiles à laquelle on ajoutera le projectile renvoyé"""

        if self.orb:
            self.current_target = target
            self.enemy_damaged = []
            self.shooted = SPshroom_projectile(self.x + self.width*0.25, self.y + self.height/2,
                                               self.current_target, self.screen_size, self.attack_value, self.attack_type, self, self.projectile_speed)
            projectiles.append(self.shooted)
            self.last_shot_time = current_tick
            self.orb = False
            self.image = self.images[1]

        for enemy in enemies:
            if self.shooted.enemy_check(enemy) and (enemy not in self.enemy_damaged) and (enemy != self.current_target):
                self.enemy_damaged.append(enemy)
                enemy.health -= int(round(self.attack_value /
                                    enemy.resistance[self.attack_type]))

        if self.orb == False and self.shooted.checked():
            self.image = self.images[0]
            self.enemy_damaged = []
            self.orb = True

        return projectiles
