import pygame
import os
from towers.Tower import Tower
from random import randint, choice, uniform
from towers.projectiles.Rshroom_projectile import Rshroom_projectile


class Rshroom(Tower):
    def __init__(self, x: float, y: float, screen_size: tuple, difficulty: str) -> None:
        super().__init__(x, y, screen_size, difficulty)
        """Sous-classe de la tour Random shroom
        - x: nombre réel correspondant à la position x de la tour
        - y: nombre réel correspondant à la position y de la tour
        screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - difficulty: chaine de caractère correspondant au fichier json des prix de la tour et upgrade"""

        self.name = "Random Shroom"
        self.images = [pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "random_shroom", "random_shroom.png")).convert_alpha(), (self.width, self.height)),
                       pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "random_shroom", "random_shroom2.png")).convert_alpha(), (self.width, self.height)),
                       pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "random_shroom", "random_shroom3.png")).convert_alpha(), (self.width, self.height)),
                       pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "random_shroom", "random_shroom2.png")).convert_alpha(), (self.width, self.height))]
        self.image_index = 0
        self.image = self.images[round(self.image_index)]
        self.animating = False
        self.anim_speed = 0.3
        self.cost = self.upgrades[self.name]["base"]["cost"]
        self.value = self.cost
        self.attack_type_value = ["Physical", "Magic"]
        self.attack_type = "Random"
        self.placement_type = "Ground"
        self.range = self.screen_size[0]/9.6
        self.range_circle = pygame.Surface(
            (self.range*2, self.range*2), pygame.SRCALPHA).convert_alpha()
        pygame.draw.circle(self.range_circle, (50, 50, 50, 128),
                           (self.range, self.range), self.range)
        self.attack_value = self.upgrades[self.name]["base"]["attack_value"]
        self.shoot_interval = self.upgrades[self.name]["base"]["shoot_interval"]
        self.shoot_reload_time = randint(
            self.shoot_interval-10, self.shoot_interval+10)
        self.upgrade_cost = [self.upgrades[self.name]["0"][str(
            self.level[0]+1)]["upgrade_cost"], self.upgrades[self.name]["1"][str(self.level[1]+1)]["upgrade_cost"]]
        self.sell_cost = int(self.value*0.8)

    def main_attack(self, target, enemies=None, current_tick=0, projectiles=None) -> list:
        """Gestion de tir de la tour, renvoie le projectile crée par le tir de la tour
        - target: ennemi ciblé
        - enemies: liste des ennemis ciblés
        - current_tick: entier correspondant au tick auquel la méthode est appelée afin de gérer l'intervalle de tir
        - projectiles: liste des projectiles à laquelle on ajoutera le projectile renvoyé"""

        if enemies != []:
            if current_tick - self.last_shot_time > self.shoot_interval:
                level1, level2 = 0, 0
                self.animating = True
                target = choice(enemies)
                self.shoot_reload_time = randint(
                    self.shoot_interval-5, self.shoot_interval+5)
                self.range = self.screen_size[0]/uniform(5.5, 9.6)
                self.range_circle = pygame.Surface(
                    (self.range*2, self.range*2), pygame.SRCALPHA).convert_alpha()
                pygame.draw.circle(
                    self.range_circle, (50, 50, 50, 128), (self.range, self.range), self.range)
                if self.level[0] == "max":
                    level1 = 5
                else:
                    level1 = self.level[0]
                if self.level[1] == "max":
                    level2 = 5
                else:
                    level2 = self.level[1]
                attack = int(round(4*randint(self.attack_value -
                             (3+level1+level2), self.attack_value+(3+level1+level2))))
                projectiles.append(Rshroom_projectile(self.x + self.width//2, self.y + self.height //
                                   2, target, self.screen_size, attack, choice(self.attack_type_value)))
                self.last_shot_time = current_tick

        return projectiles
