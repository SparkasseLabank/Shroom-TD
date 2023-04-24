import pygame
import os
from towers.Tower import Tower
from towers.projectiles.Wshroom_projectile import Wshroom_projectile


class Wshroom(Tower):
    def __init__(self, x: float, y: float, screen_size: tuple, difficulty: str) -> None:
        super().__init__(x, y, screen_size, difficulty)
        """Sous-classe de la tour Wizard shroom
        - x: nombre réel correspondant à la position x de la tour
        - y: nombre réel correspondant à la position y de la tour
        screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - difficulty: chaine de caractère correspondant au fichier json des prix de la tour et upgrade"""

        self.name = "Wizard Shroom"
        self.images = [pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "wizard_shroom", "wizard_shroom.png")).convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "wizard_shroom", "wizard_shroom2.png")).convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "wizard_shroom", "wizard_shroom3.png")).convert_alpha(), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "wizard_shroom", "wizard_shroom4.png")).convert_alpha(), (self.width, self.height))]
        self.image_index = 0
        self.image = self.images[round(self.image_index)]
        self.animating = False
        self.anim_speed = 0.4
        self.cost = self.upgrades[self.name]["base"]["cost"]
        self.value = self.cost
        self.attack_type = "Magic"
        self.placement_type = "Ground"
        self.range = self.screen_size[0]/7.68
        self.range_circle = pygame.Surface(
            (self.range*2, self.range*2), pygame.SRCALPHA).convert_alpha()
        pygame.draw.circle(self.range_circle, (50, 50, 50, 128),
                           (self.range, self.range), self.range)
        self.attack_value = self.upgrades[self.name]["base"]["attack_value"]
        self.shoot_interval = self.upgrades[self.name]["base"]["shoot_interval"]
        self.max_hit = self.upgrades[self.name]["base"]["max_hit"]
        self.aoe = self.upgrades[self.name]["base"]["aoe"]
        self.upgrade_cost = [self.upgrades[self.name]["0"][str(
            self.level[0]+1)]["upgrade_cost"], self.upgrades[self.name]["1"][str(self.level[1]+1)]["upgrade_cost"]]
        self.sell_cost = int(0.8*self.value)

    def main_attack(self, target, enemies=None, current_tick=0, projectiles=None) -> list:
        """Gestion de tir de la tour, renvoie le projectile crée par le tir de la tour
        - target: ennemi ciblé
        - enemies: liste des ennemis ciblés
        - current_tick: entier correspondant au tick auquel la méthode est appelée afin de gérer l'intervalle de tir
        - projectiles: liste des projectiles à laquelle on ajoutera le projectile renvoyé"""

        hit = 0
        if current_tick - self.last_shot_time > self.shoot_interval:
            self.damaged_enemies = []
            while hit < self.max_hit and target != None:
                start_target = target
                enemy_number = 0
                self.animating = True
                projectiles.append(Wshroom_projectile(self.x + self.width*0.8, self.y + self.height *
                                   0.5, target, self.screen_size, self.attack_value, self.attack_type))
                hit += 1
                self.last_shot_time = current_tick
                for enemy in reversed(enemies):
                    if target != None:
                        if target.x+self.aoe >= enemy.x >= target.x-self.aoe and target.y + self.aoe >= enemy.y >= target.y - self.aoe:
                            if enemy_number == 0 and enemy != start_target and (enemy not in self.damaged_enemies):
                                target = enemy
                                self.damaged_enemies.append(enemy)
                                enemy_number += 1
                if target == start_target:
                    target = None

        return projectiles
