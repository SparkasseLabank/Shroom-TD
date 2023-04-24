import pygame
import os
from buttons.Bouton import Bouton
from buttons.Tower_button import Tower_button
from towers.Cshroom import Cshroom
from towers.Sshroom import Sshroom
from towers.SNshroom import SNshroom
from towers.Bshroom import Bshroom
from towers.Wshroom import Wshroom
from towers.Gshroom import Gshroom
from towers.Rshroom import Rshroom
from towers.SPshroom import SPshroom
from towers.LPshroom import LPshroom
from towers.Ushroom import Ushroom
from towers.Ashroom import Ashroom
from towers.WSshroom import WSshroom


class Menu_bar:
    def __init__(self, screen_size: tuple, game_health: int, game_money: int, game_wave: int, difficulty: str, last_wave: int) -> None:
        """Classe Menu_bar:
        Cette classe représente la barre de menu en haut de l'écran (boutons de tours, vague, accélération et textes informatifs)
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - game_health: nombre entier correspondant au nombre de vie que le joueur possède
        - game_money: nombre netier correspondant à l'argent que le joueur possède
        - game_wave: nombre entier correspondant à la vague courante de la partie en cours
        - difficulty: chaine de caractères correspondant a un fichier json qui sera choisi pour les prix des tours et des upgrades"""

        self.menu_bar_rect = pygame.transform.scale(pygame.image.load(os.path.join(
            "assets", "other", "menu_bar_rect.png")).convert_alpha(), (screen_size[0], screen_size[1]//10))
        self.last_wave = last_wave
        self.health_text = pygame.font.SysFont("impact", self.menu_bar_rect.get_height(
        )//4).render(str(game_health), True, (255, 255, 255))
        self.money_text = pygame.font.SysFont("impact", self.menu_bar_rect.get_height(
        )//4).render(str(game_money), True, (255, 255, 255))
        self.wave_text = pygame.font.SysFont("impact", self.menu_bar_rect.get_height(
        )//4).render("Vague: " + str(game_wave), True, (255, 255, 255))
        self.health_symbol = pygame.transform.scale(pygame.image.load(os.path.join(
            "assets", "other", "hp.png")).convert_alpha(), (self.health_text.get_height()*1.4, self.health_text.get_height()*1.4))
        self.money_symbol = pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "money.png")).convert_alpha(
        ), (self.health_text.get_height()*1.4, self.health_text.get_height()*1.4))

        self.unavailable_button = pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "unavailable_play_button.png")).convert_alpha(),
                                                         (screen_size[0]/18, screen_size[0]/18))

        self.start_wave_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "available_play_button.png")).convert_alpha(),
                                                               (screen_size[0]/18, screen_size[0]/18)), screen_size[0]/1.125, -2, "start_wave")

        self.accelerate_on_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "accelerate_on_button.png")).convert_alpha(),
                                                                  (screen_size[0]/18, screen_size[0]/18)), screen_size[0]/1.06, -2, "accelerate_on")

        self.accelerate_off_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "accelerate_off_button.png")).convert_alpha(),
                                                                   (screen_size[0]/18, screen_size[0]/18)), screen_size[0]/1.06, -2, "accelerate_off")

        self.tower_buttons = [Tower_button(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "tower_buttons", "classic_shroom_button.png")).convert_alpha(),
                                                                  (screen_size[0]/30, screen_size[0]/30)), screen_size[0]/60, screen_size[1]/30,
                                           "Cshroom", pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "classic_shroom", "classic_shroom1.png")).convert_alpha(),
                                                                             (screen_size[0]/30, screen_size[0]/30)), Cshroom(-100, -100, screen_size, difficulty), screen_size),

                              Tower_button(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "tower_buttons", "stun_shroom_button.png")).convert_alpha(),
                                                                  (screen_size[0]/30, screen_size[0]/30)), screen_size[0]/16, screen_size[1]/30,
                                           "Sshroom", pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "stun_shroom", "stun_shroom.png")).convert_alpha(),
                                                                             (screen_size[0]/30, screen_size[0]/30)), Sshroom(-100, -100, screen_size, difficulty), screen_size),

                              Tower_button(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "tower_buttons", "sniper_shroom_button.png")).convert_alpha(),
                                                                  (screen_size[0]/30, screen_size[0]/30)), screen_size[0]/9.2, screen_size[1]/30,
                                           "SNshroom", pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "sniper_shroom", "sniper_shroom.png")).convert_alpha(),
                                                                              (screen_size[0]/30, screen_size[0]/30)), SNshroom(-100, -100, screen_size, difficulty), screen_size),

                              Tower_button(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "tower_buttons", "boom_shroom_button.png")).convert_alpha(),
                                                                  (screen_size[0]/30, screen_size[0]/30)), screen_size[0]/6.5, screen_size[1]/30,
                                           "Bshroom", pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "boom_shroom", "boom_shroom.png")).convert_alpha(),
                                                                             (screen_size[0]/30, screen_size[0]/30)), Bshroom(-100, -100, screen_size, difficulty), screen_size),

                              Tower_button(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "tower_buttons", "wizard_shroom_button.png")).convert_alpha(),
                                                                  (screen_size[0]/30, screen_size[0]/30)), screen_size[0]/5, screen_size[1]/30,
                                           "Wshroom", pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "wizard_shroom", "wizard_shroom.png")).convert_alpha(),
                                                                             (screen_size[0]/30, screen_size[0]/30)), Wshroom(-100, -100, screen_size, difficulty), screen_size),

                              Tower_button(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "tower_buttons", "gangsta_shroom_button.png")).convert_alpha(),
                                                                  (screen_size[0]/30, screen_size[0]/30)), screen_size[0]/4.05, screen_size[1]/30,
                                           "Gshroom", pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "gangsta_shroom", "gangsta_shroom1.png")).convert_alpha(),
                                                                             (screen_size[0]/30, screen_size[0]/30)), Gshroom(-100, -100, screen_size, difficulty), screen_size),

                              Tower_button(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "tower_buttons", "random_shroom_button.png")).convert_alpha(),
                                                                  (screen_size[0]/30, screen_size[0]/30)), screen_size[0]/3.4, screen_size[1]/30,
                                           "Rshroom", pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "random_shroom", "random_shroom.png")).convert_alpha(),
                                                                             (screen_size[0]/30, screen_size[0]/30)), Rshroom(-100, -100, screen_size, difficulty), screen_size),

                              Tower_button(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "tower_buttons", "spirit_shroom_button.png")).convert_alpha(),
                                                                  (screen_size[0]/30, screen_size[0]/30)), screen_size[0]/2.93, screen_size[1]/30,
                                           "SPshroom", pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "spirit_shroom", "spirit_shroom.png")).convert_alpha(),
                                                                              (screen_size[0]/30, screen_size[0]/30)), SPshroom(-100, -100, screen_size, difficulty), screen_size),

                              Tower_button(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "tower_buttons", "lilypad_shroom_button.png")).convert_alpha(),
                                                                  (screen_size[0]/30, screen_size[0]/30)), screen_size[0]/2.57, screen_size[1]/30,
                                           "LPshroom", pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "lilypad_shroom", "lilypad_shroom_not_placed.png")).convert_alpha(),
                                                                              (screen_size[0]/30, screen_size[0]/30)), LPshroom(-100, -100, screen_size, difficulty), screen_size),

                              Tower_button(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "tower_buttons", "urchin_shroom_button.png")).convert_alpha(),
                                                                  (screen_size[0]/30, screen_size[0]/30)), screen_size[0]/2.3, screen_size[1]/30,
                                           "Ushroom", pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "urchin_shroom", "urchin_shroom_not_placed.png")).convert_alpha(),
                                                                             (screen_size[0]/30, screen_size[0]/30)), Ushroom(-100, -100, screen_size, difficulty), screen_size),

                              Tower_button(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "tower_buttons", "algae_shroom_button.png")).convert_alpha(),
                                                                  (screen_size[0]/30, screen_size[0]/30)), screen_size[0]/2.08, screen_size[1]/30,
                                           "Ashroom", pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "algae_shroom", "algae_shroom_not_placed.png")).convert_alpha(),
                                                                             (screen_size[0]/30, screen_size[0]/30)), Ashroom(-100, -100, screen_size, difficulty), screen_size),

                              Tower_button(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "tower_buttons", "water_strider_shroom_button.png")).convert_alpha(),
                                                                  (screen_size[0]/30, screen_size[0]/30)), screen_size[0]/1.89, screen_size[1]/30,
                                           "WSshroom", pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "water_strider_shroom", "water_strider_shroom_not_placed.png")).convert_alpha(),
                                                                              (screen_size[0]/30, screen_size[0]/30)), WSshroom(-100, -100, screen_size, difficulty), screen_size)]

        self.little_money_symbol = pygame.transform.scale(
            self.money_symbol, (self.tower_buttons[0].height/2, self.tower_buttons[0].height/2))

    def draw(self, window, screen_size: tuple) -> None:
        """Méthode pour déssiner la barre de menu
        - window: fenêtre pygame sur laquelle le menu sera dessiné
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        Dans cette méthode, on dessine le rectangle noir, les textes informatifs puis les boutons"""

        window.blit(self.menu_bar_rect, (0, 0))
        window.blit(
            self.health_text, (screen_size[0]/1.07 - self.health_text.get_width() - self.start_wave_button.width, 3))
        window.blit(self.money_text, (screen_size[0]/1.07 - self.money_text.get_width(
        ) - self.start_wave_button.width, self.health_text.get_height() + 5))
        window.blit(self.health_symbol, (screen_size[0]/1.07 - self.health_text.get_width(
        ) - self.start_wave_button.width - self.health_symbol.get_width(), 0))
        window.blit(self.money_symbol, (screen_size[0]/1.07 - self.money_text.get_width(
        ) - self.start_wave_button.width - self.money_symbol.get_width(), self.health_text.get_height()))
        window.blit(self.wave_text, (screen_size[0]/1.07 - self.start_wave_button.width - self.wave_text.get_width(
        ), self.health_text.get_height() + self.money_text.get_height() + 3))

        for button in self.tower_buttons:
            button.draw_and_scale(window)
            window.blit(button.cost_text, button.cost_text_position)
            window.blit(self.little_money_symbol,
                        (button.cost_text_position[0] + button.cost_text.get_width(), 2))

    def update_texts(self, game_health: int, game_money: int, game_wave: int) -> None:
        """Méthode pour mettre à jour les textes informatifs
        - game_health: nombre entier correspondant au nombre de vie que le joueur possède
        - game_money: nombre netier correspondant à l'argent que le joueur possède
        - game_wave: nombre entier correspondant à la vague courante de la partie en cours"""

        self.health_text = pygame.font.SysFont("impact", self.menu_bar_rect.get_height(
        )//4).render(str(game_health), True, (255, 255, 255))
        self.money_text = pygame.font.SysFont("impact", self.menu_bar_rect.get_height(
        )//4).render(str(game_money), True, (255, 255, 255))
        self.wave_text = pygame.font.SysFont("impact", self.menu_bar_rect.get_height(
        )//4).render("Vague: " + str(game_wave) + "/" + str(self.last_wave), True, (255, 255, 255))
