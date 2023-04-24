import pygame
import os
import ctypes
import json
from buttons.Bouton import Bouton
from effects.effets import fondu_fermer, fondu_ouvrir
from menus.Quit_confirm_menu import Quit_confirm_menu
from menus.Difficulty_menu import Difficulty_menu
from menus.Encyclopedia import Encyclopedia
from core.Game import Game
from effects.sound import *


class Menu:
    def __init__(self) -> None:
        """Classe Menu:
        Cette classe représente le menu de jeu avant la partie: elle comporte 2 parties: le menu principal et le menu pour choisir la map"""

        pygame.display.set_icon(pygame.image.load(
            os.path.join("assets", "other", "icon.png")))

        try:
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                os.path.join("assets", "other", "icon.png"))
        except AttributeError:
            pass

        self.window = pygame.display.set_mode(
            flags=pygame.FULLSCREEN | pygame.DOUBLEBUF)
        pygame.display.set_caption("ShroomTD")
        self.width = self.window.get_width()
        self.height = self.window.get_height()
        self.background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "background.png")).convert_alpha(),
                                                 (self.width, self.height))
        self.logo = pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "logo.png")).convert_alpha(),
                                           (self.width/2.3, self.height/2.25))

        fondu_ouvrir(self.window, (self.width/3.55,
                     self.height/3.7), self.logo)
        fondu_fermer(self.window, (self.width, self.height), 0.1, 15)

        self.current_window = "main"
        self.music_state = True
        self.sfx_state = True
        self.bronze_medal = pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "bronze_medal.png")).convert_alpha(),
                                                   (self.width/38.4, self.height/15.43))

        self.silver_medal = pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "silver_medal.png")).convert_alpha(),
                                                   (self.width/38.4, self.height/15.43))

        self.gold_medal = pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "gold_medal.png")).convert_alpha(),
                                                 (self.width/38.4, self.height/15.43))

        self.music_on_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "music_on.png")).convert_alpha(),
                                                             (self.width/20, self.width/20)),
                                      self.width/1.07, 0)

        self.music_off_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "music_off.png")).convert_alpha(),
                                                              (self.width/20, self.width/20)),
                                       self.width/1.07, 0)

        self.sfx_on_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "sfx_on.png")).convert_alpha(),
                                                           (self.width/20, self.width/20)),
                                    self.width/1.13, 0)

        self.sfx_off_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "sfx_off.png")).convert_alpha(),
                                                            (self.width/20, self.width/20)),
                                     self.width/1.13, 0)

        self.available_maps = [Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "choice_map_prairie.png")).convert(),
                                                             (self.width/4, self.height/4)),
                                      self.width/25, self.height/5, "meadow"),

                               Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "choice_map_neige.png")).convert(),
                                                             (self.width/4, self.height/4)),
                                      self.width/2.65, self.height/5, "snow"),

                               Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "choice_map_plage.png")).convert(),
                                                             (self.width/4, self.height/4)),
                                      self.width/1.4, self.height/5, "beach"),

                               Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "choice_map_air.png")).convert(),
                                                             (self.width/4, self.height/4)),
                                      self.width/25, self.height/1.8, "floating_islands"),

                               Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "choice_map_marecage.png")).convert(),
                                                             (self.width/4, self.height/4)),
                                      self.width/2.65, self.height/1.8, "swamp"),

                               Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "choice_islands_map_WIP.png")).convert(),
                                                             (self.width/4, self.height/4)),
                                      self.width/1.4, self.height/1.8, "islands"),
                               ]

        self.play_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "play_button.png")).convert_alpha(),
                                                         (self.width/3.84, self.height/5.4)),
                                  self.width/2.7, self.height/2.55)

        self.encyclopedia_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "encyclopedie_button.png")).convert_alpha(),
                                                                 (self.width/3.84, self.height/5.4)),
                                          self.play_button.x, self.height/1.7)

        self.quit_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "quit_button.png")).convert_alpha(),
                                                         (self.width/3.84, self.height/5.4)),
                                  self.play_button.x, self.height/1.27)

        self.back_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "back_button.png")).convert_alpha(),
                                                         (self.width/7.68, self.height/10.8)),
                                  self.width/50, self.height/1.12)

        self.map_choice_text = pygame.font.SysFont(
            'arialrounded', self.height//11).render('Choisissez une carte', True, (0, 0, 0))

        with open(os.path.join("data", "medals.json"), "r") as medals_file:
            self.medals = json.load(medals_file)

        try:
            self.music = create_music(pygame.mixer.Sound(
                os.path.join("assets", "sounds", "musics", "groovy_tower.mp3")))
        except pygame.error:
            self.music = None

    def run(self) -> None:
        """Méthode pour faire tourner le menu: on affiche tout les éléments en boucle"""

        running = 1
        play_music(self.music, self.music_state)

        while running:
            self.draw_menu()
            running = self.handle_clicks()
            self.draw_sound_buttons()

            pygame.display.flip()

        fondu_fermer(self.window, (self.width, self.height), 0.1, 15)
        exit()

    def handle_music(self) -> None:
        """Méthode pour gérer la musique et les sons:
        On change l'état de la musique et des sons si le joueur clique sur le bouton correspondant"""

        if self.music_on_button.rect.collidepoint(pygame.mouse.get_pos()):
            if self.music_state:
                play_sound("click.ogg", 1, self.sfx_state)
                disable_music(self.music)
                self.music_state = False
            else:
                self.music_state = True
                enable_music(self.music)
                play_sound("click.ogg", 1, self.sfx_state)

        elif self.sfx_on_button.rect.collidepoint(pygame.mouse.get_pos()):
            if self.sfx_state:
                play_sound("click.ogg", 1, self.sfx_state)
                self.sfx_state = False
            else:
                self.sfx_state = True
                play_sound("click.ogg", 1, self.sfx_state)

    def draw_sound_buttons(self) -> None:
        """Méthode pour dessiner les boutons de gestion de la musique et du son"""

        if self.music_state:
            self.music_on_button.draw_and_scale(self.window)
        else:
            self.music_off_button.draw_and_scale(self.window)

        if self.sfx_state:
            self.sfx_on_button.draw_and_scale(self.window)
        else:
            self.sfx_off_button.draw_and_scale(self.window)

    def handle_clicks(self) -> bool:
        """Méthode pour gérer les entrées utilisateur:
        Selon la partie du menu dans laquelle on se trouve, la gestion des clics s'adapte"""

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_LALT]:
                        exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_music()

                if self.current_window == "main":
                    if self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        quit_confirm_menu = Quit_confirm_menu(
                            (self.width, self.height), self.sfx_state)
                        return quit_confirm_menu.draw(self)

                    if self.play_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        fondu_fermer(
                            self.window, (self.width, self.height), 0.5, 50)
                        self.current_window = "map_choice"

                    if self.encyclopedia_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        fondu_fermer(
                            self.window, (self.width, self.height), 0.5, 50)
                        encyclopedia = Encyclopedia(
                            (self.width, self.height), self.sfx_state, self.music_state, self.music)
                        encyclopedia.draw_encyclopedia(self.window)

                elif self.current_window == "map_choice":
                    for choice_map in self.available_maps:
                        if choice_map.rect.collidepoint(pygame.mouse.get_pos()):
                            play_sound("click.ogg", 1, self.sfx_state)
                            difficulty_menu = Difficulty_menu(
                                (self.width, self.height), self.sfx_state)
                            difficulty = difficulty_menu.draw(self)
                            if difficulty is not None:
                                stop_music(self.music)
                                fondu_fermer(
                                    self.window, (self.width, self.height), 0.5, 50)
                                game = Game(self, choice_map.name, difficulty)
                                game.run()
                            break

                    if self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        fondu_fermer(
                            self.window, (self.width, self.height), 0.5, 50)
                        self.current_window = "main"

        return 1

    def draw_menu(self) -> None:
        """Méthode pour dessiner le menu:
        Selon la partie du menu dans laquelle on se trouve, les éléments à dessiner sont différents"""

        self.window.blit(self.background, (0, 0))

        if self.current_window == "main":
            self.window.blit(self.logo, (self.width/3.55, self.height/30))
            self.play_button.draw_and_scale(self.window)
            self.encyclopedia_button.draw_and_scale(self.window)
            self.quit_button.draw_and_scale(self.window)

        elif self.current_window == "map_choice":
            self.update_medals()
            self.window.blit(self.map_choice_text,
                             (self.width/4.2, self.height/20))
            self.back_button.draw_and_scale(self.window)

            for choice_map in self.available_maps:
                choice_map.draw_and_scale(self.window)
                if self.medals[choice_map.name]["easy"]:
                    self.window.blit(self.bronze_medal, (choice_map.x +
                                     choice_map.width / 15, choice_map.y + choice_map.height*1.03))
                if self.medals[choice_map.name]["medium"]:
                    self.window.blit(self.silver_medal, (choice_map.x +
                                     choice_map.width / 5, choice_map.y + choice_map.height*1.03))
                if self.medals[choice_map.name]["hard"]:
                    self.window.blit(
                        self.gold_medal, (choice_map.x + choice_map.width / 3, choice_map.y + choice_map.height*1.03))

    def update_medals(self):
        """Méthode pour mettre à jour les médailles"""
        with open(os.path.join("data", "medals.json"), "r") as medals_file:
            self.medals = json.load(medals_file)
