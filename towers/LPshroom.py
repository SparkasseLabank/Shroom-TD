import pygame
import os
from towers.Tower import Tower
from towers.projectiles.LPshroom_projectile import LPshroom_projectile


class LPshroom(Tower):
    def __init__(self, x: float, y: float, screen_size: tuple, difficulty: str) -> None:
        super().__init__(x, y, screen_size, difficulty)
        """Sous-classe de la tour Lilypad shroom
        - x: nombre réel correspondant à la position x de la tour
        - y: nombre réel correspondant à la position y de la tour
        screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - difficulty: chaine de caractère correspondant au fichier json des prix de la tour et upgrade"""

        self.name = "Lilypad Shroom"
        self.images = [pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "lilypad_shroom", "lilypad_shroom1.png")).convert_alpha(), (self.width, self.height)),
                       pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "lilypad_shroom", "lilypad_shroom2.png")).convert_alpha(), (self.width, self.height)),
                       pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "lilypad_shroom", "lilypad_shroom3.png")).convert_alpha(), (self.width, self.height)),
                       pygame.transform.scale(pygame.image.load(os.path.join(
                        "assets", "towers", "lilypad_shroom", "lilypad_shroom4.png")).convert_alpha(), (self.width, self.height))]
        self.image_index = 0
        self.image = self.images[round(self.image_index)]
        self.anim_speed = 0.4
        self.animating = False
        self.cost = self.upgrades[self.name]["base"]["cost"]
        self.value = self.cost
        self.attack_type = "Magic"
        self.placement_type = "Water"
        self.shooted = False
        self.range = self.screen_size[0]/9.6
        self.range_circle = pygame.Surface(
            (self.range*2, self.range*2), pygame.SRCALPHA).convert_alpha()
        pygame.draw.circle(self.range_circle, (50, 50, 50, 128),
                           (self.range, self.range), self.range)
        self.attack_value = self.upgrades[self.name]["base"]["attack_value"]
        self.shoot_interval = self.upgrades[self.name]["base"]["shoot_interval"]
        self.upgrade_cost = [self.upgrades[self.name]["0"][str(
            self.level[0]+1)]["upgrade_cost"], self.upgrades[self.name]["1"][str(self.level[1]+1)]["upgrade_cost"]]
        self.sell_cost = int(self.value*0.8)

    def main_attack(self, target, enemies=None, current_tick=0, projectiles=None) -> list:
        """Gestion de tir de la tour, renvoie le projectile crée par le tir de la tour
        - target: ennemi ciblé
        - enemies: liste des ennemis ciblés
        - current_tick: entier correspondant au tick auquel la méthode est appelée afin de gérer l'intervalle de tir
        - projectiles: liste des projectiles à laquelle on ajoutera le projectile renvoyé"""

        if current_tick - self.last_shot_time > self.shoot_interval and self.shooted == False:
            self.animating = True
            projectiles.append(LPshroom_projectile(self.x + self.width*0.20, self.y +
                               self.height*0.4, target, self.screen_size, self.attack_value, self.attack_type))
            self.shooted = True

        if current_tick - self.last_shot_time > self.shoot_interval + (self.shoot_interval*0.33):
            projectiles.append(LPshroom_projectile(self.x + self.width*0.85, self.y +
                               self.height*0.33, target, self.screen_size, self.attack_value, self.attack_type))
            self.last_shot_time = current_tick
            self.shooted = False

        return projectiles
