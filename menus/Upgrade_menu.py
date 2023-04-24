import pygame
import os
from buttons.Bouton import Bouton


class Upgrade_menu:
    def __init__(self, selected_tower, screen_size: tuple) -> None:
        """Classe Upgrade_menu:
        Cette classe représente le menu d'amélioration se situant au même endroit que l'objet 'Menu_bar'.
        Elle contient les informations de la tour séléctionnée et les boutons pour l'améliorer ou la vendre
        - selected_tower: objet Tower correspondant à la tour séléctionnée et dont on affichera les informations
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre"""

        self.screen_size = screen_size
        self.rect = pygame.transform.scale(pygame.image.load(os.path.join(
            "assets", "other", "upgrade_rect.png")).convert_alpha(), (self.screen_size[0]/1.3, self.screen_size[1]/10))
        self.selected_tower = selected_tower
        self.info = False

        self.name_text = pygame.font.SysFont('arialrounded', self.screen_size[1]//30)\
            .render(str(self.selected_tower.name), True, (255, 255, 255))

        self.level_text = pygame.font.SysFont('arialrounded', self.screen_size[1]//30)\
            .render('Level: ' + str(self.selected_tower.level[0]) + '-' + str(self.selected_tower.level[1]), True, (255, 255, 255))

        self.sell_cost_text = pygame.font.SysFont('impact', self.screen_size[1]//45) \
            .render(str(self.selected_tower.sell_cost), True, (255, 255, 255))

        if self.selected_tower.locked_path(0):
            self.first_upgrade_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "upgrade_icons", "path_locked.png")).convert_alpha(),
                                                                      (self.screen_size[0]/12.8, self.screen_size[1]/14.4)),
                                               self.rect.get_width()/2.5, self.rect.get_height()/20)

        elif self.selected_tower.level[0] != "max":
            self.first_upgrade_button = Bouton(pygame.transform.scale(pygame.image.load(
                os.path.join("assets", "upgrade_icons", self.selected_tower.upgrades[self.selected_tower.name]["0"][str(self.selected_tower.level[0]+1)]["icon"])).convert_alpha(),
                (self.screen_size[0]/12.8, self.screen_size[1]/14.4)),
                self.rect.get_width()/2.5, self.rect.get_height()/20)
        else:
            self.first_upgrade_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "upgrade_icons", "maxed.png")).convert_alpha(),
                                                                      (self.screen_size[0]/12.8, self.screen_size[1]/14.4)),
                                               self.rect.get_width()/2.5, self.rect.get_height()/20)

        if self.selected_tower.locked_path(1):
            self.second_upgrade_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "upgrade_icons", "path_locked.png")).convert_alpha(),
                                                                       (self.screen_size[0]/12.8, self.screen_size[1]/14.4)),
                                                self.first_upgrade_button.x + self.first_upgrade_button.width*1.4, self.first_upgrade_button.y)

        elif self.selected_tower.level[1] != "max":
            self.second_upgrade_button = Bouton(pygame.transform.scale(pygame.image.load(
                os.path.join("assets", "upgrade_icons", self.selected_tower.upgrades[self.selected_tower.name]["1"][str(self.selected_tower.level[1]+1)]["icon"])).convert_alpha(),
                (self.screen_size[0]/12.8, self.screen_size[1]/14.4)),
                self.first_upgrade_button.x + self.first_upgrade_button.width*1.4, self.first_upgrade_button.y)
        else:
            self.second_upgrade_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "upgrade_icons", "maxed.png")).convert_alpha(),
                                                                       (self.screen_size[0]/12.8, self.screen_size[1]/14.4)),
                                                self.first_upgrade_button.x + self.first_upgrade_button.width*1.4, self.first_upgrade_button.y)

        self.sell_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "sell_button.png")).convert_alpha(),
                                                         (self.screen_size[0]/26.4, self.screen_size[1]/14.4)),
                                  self.second_upgrade_button.x + self.second_upgrade_button.width*1.7, self.second_upgrade_button.y)

        if self.selected_tower.locked_path(0) or self.selected_tower.level[0] == "max":
            self.first_upgrade_cost_text = pygame.font.SysFont('impact', self.screen_size[1]//45) \
                .render("", True, (255, 255, 255))
        else:
            self.first_upgrade_cost_text = pygame.font.SysFont('impact', self.screen_size[1]//45) \
                .render(str(self.selected_tower.upgrade_cost[0]), True, (255, 255, 255))

        if self.selected_tower.locked_path(1) or self.selected_tower.level[1] == "max":
            self.second_upgrade_cost_text = pygame.font.SysFont('impact', self.screen_size[1]//45) \
                .render("", True, (255, 255, 255))
        else:
            self.second_upgrade_cost_text = pygame.font.SysFont('impact', self.screen_size[1]//45) \
                .render(str(self.selected_tower.upgrade_cost[1]), True, (255, 255, 255))

        self.little_money_symbol = pygame.transform.scale(pygame.image.load(os.path.join(
            "assets", "other", "money.png")).convert_alpha(), (self.rect.get_height()/3.3, self.rect.get_height()/3.3))
        self.first_upgrade_available = False
        self.second_upgrade_available = False
        self.available_rect = pygame.transform.scale(pygame.image.load(os.path.join("assets", "upgrade_icons", "available_rect.png")).convert_alpha(),
                                                     (self.first_upgrade_button.width*1.1, self.first_upgrade_button.height))

        self.unavailable_rect = pygame.transform.scale(pygame.image.load(os.path.join("assets", "upgrade_icons", "unavailable_rect.png")).convert_alpha(),
                                                       (self.first_upgrade_button.width*1.1, self.first_upgrade_button.height))

    def draw(self, window, current_money) -> None:
        """Méthode pour déssiner le menu d'amélioration
        - window: fenêtre pygame sur laquelle le menu sera déssiné"""

        window.blit(self.rect, (0, 0))
        window.blit(self.selected_tower.image, (0, 0))
        window.blit(self.name_text, (self.selected_tower.width*1.1, 0))
        window.blit(self.level_text, (self.selected_tower.width *
                    1.1, self.name_text.get_height()*1.1))
        self.sell_button.draw_and_scale(window)
        window.blit(self.first_upgrade_cost_text, (self.first_upgrade_button.x + self.first_upgrade_button.width/3,
                                                   self.first_upgrade_button.y + self.first_upgrade_button.height/1.05))

        window.blit(self.second_upgrade_cost_text, (self.second_upgrade_button.x + self.second_upgrade_button.width/3,
                                                    self.second_upgrade_button.y + self.second_upgrade_button.height/1.05))

        window.blit(self.sell_cost_text, (self.sell_button.x + self.sell_button.width/16,
                                          self.sell_button.y + self.sell_button.height/1.05))

        window.blit(self.little_money_symbol, (self.sell_button.x + self.sell_button.width/16 + self.sell_cost_text.get_width(),
                                               self.sell_button.y + self.sell_button.height/1.05))

        if not self.selected_tower.locked_path(0) and self.selected_tower.level[0] != "max":
            if self.first_upgrade_available and current_money >= self.selected_tower.upgrade_cost[0]:
                window.blit(
                    self.available_rect, (self.first_upgrade_button.x, self.first_upgrade_button.y))
            else:
                window.blit(
                    self.unavailable_rect, (self.first_upgrade_button.x, self.first_upgrade_button.y))

            window.blit(self.little_money_symbol, (self.first_upgrade_button.x + self.first_upgrade_button.width/3 + self.first_upgrade_cost_text.get_width(),
                                                   self.first_upgrade_button.y + self.first_upgrade_button.height/1.05))

        if not self.selected_tower.locked_path(1) and self.selected_tower.level[1] != "max":
            if self.second_upgrade_available and current_money >= self.selected_tower.upgrade_cost[1]:
                window.blit(
                    self.available_rect, (self.second_upgrade_button.x, self.second_upgrade_button.y))
            else:
                window.blit(
                    self.unavailable_rect, (self.second_upgrade_button.x, self.second_upgrade_button.y))

            window.blit(self.little_money_symbol, (self.second_upgrade_button.x + self.second_upgrade_button.width/3 + self.second_upgrade_cost_text.get_width(),
                                                   self.second_upgrade_button.y + self.second_upgrade_button.height/1.05))

        self.first_upgrade_button.draw_and_scale(window)
        self.second_upgrade_button.draw_and_scale(window)

    def update(self, selected_tower) -> None:
        """Méthode pour mettre à jour les textes du menu d'amélioration:
        Cette méthode sert à actualiser le menu lors de l'amélioration de la tour ou d'un change de tour séléctionnée
        - selected_tower: objet Tower séléctionné par le joueur"""

        self.selected_tower = selected_tower

        self.name_text = pygame.font.SysFont('arialrounded', self.screen_size[1]//30)\
            .render(str(self.selected_tower.name), True, (255, 255, 255))

        self.level_text = pygame.font.SysFont('arialrounded', self.screen_size[1]//30)\
            .render('Niveau: ' + str(self.selected_tower.level[0]) + '-' + str(self.selected_tower.level[1]), True, (255, 255, 255))

        self.sell_cost_text = pygame.font.SysFont('impact', self.screen_size[1]//45) \
            .render(str(self.selected_tower.sell_cost), True, (255, 255, 255))

        self.selected_tower.range_circle = pygame.Surface(
            (self.selected_tower.range*2, self.selected_tower.range*2), pygame.SRCALPHA).convert_alpha()
        pygame.draw.circle(self.selected_tower.range_circle, (50, 50, 50, 128), (
            self.selected_tower.range, self.selected_tower.range), self.selected_tower.range)

        if self.selected_tower.locked_path(0) or self.selected_tower.level[0] == "max":
            self.first_upgrade_cost_text = pygame.font.SysFont('impact', self.screen_size[1]//45) \
                .render("", True, (255, 255, 255))
        else:
            self.first_upgrade_cost_text = pygame.font.SysFont('impact', self.screen_size[1]//45) \
                .render(str(self.selected_tower.upgrade_cost[0]), True, (255, 255, 255))

        if self.selected_tower.locked_path(1) or self.selected_tower.level[1] == "max":
            self.second_upgrade_cost_text = pygame.font.SysFont('impact', self.screen_size[1]//45) \
                .render("", True, (255, 255, 255))
        else:
            self.second_upgrade_cost_text = pygame.font.SysFont('impact', self.screen_size[1]//45) \
                .render(str(self.selected_tower.upgrade_cost[1]), True, (255, 255, 255))

        if self.selected_tower.locked_path(0):
            self.first_upgrade_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "upgrade_icons", "path_locked.png")).convert_alpha(),
                                                                      (self.screen_size[0]/12.8, self.screen_size[1]/14.4)),
                                               self.rect.get_width()/2.5, self.rect.get_height()/20)

        elif self.selected_tower.level[0] != "max":
            self.first_upgrade_button = Bouton(pygame.transform.scale(pygame.image.load(
                os.path.join("assets", "upgrade_icons", self.selected_tower.upgrades[self.selected_tower.name]["0"][str(self.selected_tower.level[0]+1)]["icon"])).convert_alpha(),
                (self.screen_size[0]/12.8, self.screen_size[1]/14.4)),
                self.rect.get_width()/2.5, self.rect.get_height()/20)
        else:
            self.first_upgrade_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "upgrade_icons", "maxed.png")).convert_alpha(),
                                                                      (self.screen_size[0]/12.8, self.screen_size[1]/14.4)),
                                               self.rect.get_width()/2.5, self.rect.get_height()/20)
        if self.selected_tower.locked_path(1):
            self.second_upgrade_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "upgrade_icons", "path_locked.png")).convert_alpha(),
                                                                       (self.screen_size[0]/12.8, self.screen_size[1]/14.4)),
                                                self.first_upgrade_button.x + self.first_upgrade_button.width*1.4, self.first_upgrade_button.y)

        elif self.selected_tower.level[1] != "max":
            self.second_upgrade_button = Bouton(pygame.transform.scale(pygame.image.load(
                os.path.join("assets", "upgrade_icons", self.selected_tower.upgrades[self.selected_tower.name]["1"][str(self.selected_tower.level[1]+1)]["icon"])).convert_alpha(),
                (self.screen_size[0]/12.8, self.screen_size[1]/14.4)),
                self.first_upgrade_button.x + self.first_upgrade_button.width*1.4, self.first_upgrade_button.y)
        else:
            self.second_upgrade_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "upgrade_icons", "maxed.png")).convert_alpha(),
                                                                       (self.screen_size[0]/12.8, self.screen_size[1]/14.4)),
                                                self.first_upgrade_button.x + self.first_upgrade_button.width*1.4, self.first_upgrade_button.y)
