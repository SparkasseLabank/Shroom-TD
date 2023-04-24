import pygame
import os
from towers.Tower import Tower
from towers.projectiles.SNshroom_projectile import SNshroom_projectile


class SNshroom(Tower):
    def __init__(self, x: float, y: float, screen_size: tuple, difficulty: str) -> None:
        super().__init__(x, y, screen_size, difficulty)
        """Sous-classe de la tour Sniper shroom
        - x: nombre réel correspondant à la position x de la tour
        - y: nombre réel correspondant à la position y de la tour
        screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - difficulty: chaine de caractère correspondant au fichier json des prix de la tour et upgrade"""

        self.name = "Sniper Shroom"
        self.images = [pygame.transform.scale(pygame.image.load(os.path.join(
                            "assets", "towers", "sniper_shroom", "sniper_shroom.png")).convert_alpha(), (self.width, self.height)),
                       pygame.transform.scale(pygame.image.load(os.path.join(
                           "assets", "towers", "sniper_shroom", "sniper_shroom2.png")).convert_alpha(), (self.width, self.height)),
                       pygame.transform.scale(pygame.image.load(os.path.join(
                           "assets", "towers", "sniper_shroom", "sniper_shroom3.png")).convert_alpha(), (self.width, self.height)),
                       pygame.transform.scale(pygame.image.load(os.path.join(
                            "assets", "towers", "sniper_shroom", "sniper_shroom2.png")).convert_alpha(), (self.width, self.height))]
        self.cost = self.upgrades[self.name]["base"]["cost"]
        self.value = self.cost
        self.image_index = 0
        self.image = self.images[round(self.image_index)]
        self.animating = False
        self.anim_speed = 0.3
        self.attack_type = "Physical"
        self.placement_type = "Ground"
        self.range = self.screen_size[0]/3.84
        self.range_circle = pygame.Surface(
            (self.range*2, self.range*2), pygame.SRCALPHA).convert_alpha()
        pygame.draw.circle(self.range_circle, (50, 50, 50, 128),
                           (self.range, self.range), self.range)
        self.attack_value = self.upgrades[self.name]["base"]["attack_value"]
        self.shoot_interval = self.upgrades[self.name]["base"]["shoot_interval"]
        self.resistance_modifier = self.upgrades[self.name]["base"]["resistance_modifier"]
        self.upgrade_cost = [self.upgrades[self.name]["0"][str(
            self.level[0]+1)]["upgrade_cost"], self.upgrades[self.name]["1"][str(self.level[1]+1)]["upgrade_cost"]]
        self.sell_cost = int(self.value*0.8)

    def main_attack(self, target, enemies=None, current_tick=0, projectiles=None) -> list:
        """Gestion de tir de la tour, renvoie le projectile crée par le tir de la tour
        - target: ennemi ciblé
        - enemies: liste des ennemis ciblés
        - current_tick: entier correspondant au tick auquel la méthode est appelée afin de gérer l'intervalle de tir
        - projectiles: liste des projectiles à laquelle on ajoutera le projectile renvoyé"""

        if current_tick - self.last_shot_time > self.shoot_interval:
            self.animating = True
            projectiles.append(SNshroom_projectile(self.x + self.width/2, self.y + self.height/2,
                               target, self.screen_size, self.attack_value, self.attack_type, self.resistance_modifier))
            self.last_shot_time = current_tick

        return projectiles
