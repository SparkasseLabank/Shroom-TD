import pygame
import json
import os
from effects.sound import play_sound


class Tower:
    def __init__(self, x: float, y: float, screen_size: tuple, difficulty: str) -> None:
        """Classe mère Tower représentant une tour
        - x: nombre réel correspondant à la position x de la tour
        - y: nombre réel correspondant à la position y de la tour
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - difficulty: chaine de caractère correspondant au fichier json des prix de la tour et upgrade"""

        self.screen_size = screen_size
        self.x = x
        self.y = y
        self.width = screen_size[0]/19.2
        self.height = screen_size[1]/10.8
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.last_shot_time = 0
        self.level = [0, 0]

        with open(os.path.join("data", difficulty), "r") as upgrades_file:
            self.upgrades = json.load(upgrades_file)

    def draw(self, window) -> None:
        """Méthode pour afficher et animer la tour
        - window: fenêtre pygame sur laquelle la tour sera dessinée"""

        if hasattr(self, "animating"):
            if self.animating:
                self.image_index += self.anim_speed

                if self.image_index >= len(self.images) - 1:
                    self.image_index = 0
                    self.animating = False

                self.image = self.images[round(self.image_index)]
                window.blit(self.image, (self.x, self.y))

            else:
                window.blit(self.image, (self.x, self.y))
        else:
            window.blit(self.image, (self.x, self.y))

    def get_distance(self, target) -> float:
        """Méthode qui renvoie la distance entre la tour et l'ennemi
        - target: ennemi ciblé"""

        x_distance = target.x - self.x
        y_distance = target.y - self.y
        return (x_distance ** 2 + y_distance ** 2) ** 0.5

    def can_shoot(self, target) -> bool:
        """Méthode qui renvoie True si l'ennemi est dans la range de la tour, False sinon"""
        return self.get_distance(target) <= self.range

    def upgrade(self, current_money: int, state: bool, path: int) -> int:
        """Méthode d'amélioration de la tour (gestion de la monnaie et du niveau maximial)
        - current_money: nombre entier correspondant à la monnaie ingame possédée au moment de l'upgrade
        - state: booléen correspondant à l'état des sons sfx actuel
        - path: nombre entier correspondant au chemin d'amélioration choisi"""

        if self.level[path] != "max" and not self.locked_path(path):
            if current_money >= self.upgrade_cost[path]:
                play_sound("upgrade.ogg", 0.3, state)
                current_money -= self.upgrade_cost[path]
                self.value += self.upgrade_cost[path]
                self.sell_cost = int(self.value*0.8)
                self.level[path] += 1

                if "attack_value" in self.upgrades[self.name][str(path)][str(self.level[path])].keys():
                    self.attack_value += self.upgrades[self.name][str(
                        path)][str(self.level[path])]["attack_value"]

                if "range" in self.upgrades[self.name][str(path)][str(self.level[path])].keys():
                    self.range *= self.upgrades[self.name][str(
                        path)][str(self.level[path])]["range"]

                if hasattr(self, "shoot_interval"):
                    if "shoot_interval" in self.upgrades[self.name][str(path)][str(self.level[path])].keys():
                        self.shoot_interval -= self.upgrades[self.name][str(
                            path)][str(self.level[path])]["shoot_interval"]

                if hasattr(self, "aoe"):
                    if "aoe" in self.upgrades[self.name][str(path)][str(self.level[path])].keys():
                        self.aoe += self.upgrades[self.name][str(
                            path)][str(self.level[path])]["aoe"]

                if hasattr(self, "stun_time"):
                    if "stun_time" in self.upgrades[self.name][str(path)][str(self.level[path])].keys():
                        self.stun_time += self.upgrades[self.name][str(
                            path)][str(self.level[path])]["stun_time"]

                if hasattr(self, "max_hit"):
                    if "max_hit" in self.upgrades[self.name][str(path)][str(self.level[path])].keys():
                        self.max_hit += self.upgrades[self.name][str(
                            path)][str(self.level[path])]["max_hit"]

                if hasattr(self, "projectile_speed"):
                    if "projectile_speed" in self.upgrades[self.name][str(path)][str(self.level[path])].keys():
                        self.projectile_speed += self.upgrades[self.name][str(
                            path)][str(self.level[path])]["projectile_speed"]

                if hasattr(self, "speed_modifier"):
                    if "speed_modifier" in self.upgrades[self.name][str(path)][str(self.level[path])].keys():
                        self.speed_modifier -= self.upgrades[self.name][str(
                            path)][str(self.level[path])]["speed_modifier"]

                if hasattr(self, "resistance_modifier"):
                    if "resistance_modifier" in self.upgrades[self.name][str(path)][str(self.level[path])].keys():
                        self.resistance_modifier = self.upgrades[self.name][str(
                            path)][str(self.level[path])]["resistance_modifier"]

                if self.level[path] == 5:
                    self.level[path] = "max"
                    self.upgrade_cost[path] = "max"
                elif "upgrade_cost" in self.upgrades[self.name][str(path)][str(self.level[path]+1)].keys():
                    self.upgrade_cost[path] = self.upgrades[self.name][str(
                        path)][str(self.level[path]+1)]["upgrade_cost"]

        return current_money

    def sell(self, current_money: int, liste_tours: list, liste_emplacements: list) -> int:
        """Méthode de vente de la tour (gestion de la monnaie et de la libération des emplacements de la map)
        - current_money: nombre entier correspondant à la monnaie ingame possédée au moment de la vente
        - liste_tours: liste des tours existantes sur la map
        - liste_emplacements: liste des emplacements libres sur la map"""

        current_money += self.sell_cost
        liste_tours.remove(self)
        liste_emplacements.append((self.x, self.y))
        del self
        return int(current_money)

    def main_attack(self):
        """Méthode polymorphisme (dans chaque sous-classe, une méthode du même nom
        est présente mais possède un comportement different)"""
        raise NotImplementedError(
            "La méthode n'est pas défini pour cette classe")

    def get_other_path(self, path: int) -> int:
        """Méthode renvoyant l'entier correspondant à l'autre chemin"""

        if path == 1:
            return 0
        else:
            return 1

    def locked_path(self, path: int) -> bool:
        """Méthode renvoyant un booléen indiquant si le chemin 'path' est bloqué ou non"""
        if isinstance(self.level[self.get_other_path(path)], int):
            return self.level[self.get_other_path(path)] >= 3 and self.level[path] == 2
        else:
            return self.level[self.get_other_path(path)] == "max" and self.level[path] == 2
