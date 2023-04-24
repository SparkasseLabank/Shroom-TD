import pygame
import os
from buttons.Bouton import Bouton
from menus.Main_menu_confirm_menu import Main_menu_confirm_menu
from effects.effets import balayage_haut, balayage_bas
from effects.sound import play_sound, enable_music, disable_music


class Escape_menu:
    def __init__(self, screen_size: tuple, music) -> None:
        """Classe Escape_menu:
        Cette classe contient tous les éléments du menu échap
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - music: musique actuellement jouée"""

        self.music_state = True
        self.sfx_state = True
        self.music = music

        self.screen_size = screen_size
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            "assets", "other", "escape_menu_rect.png")).convert_alpha(), (self.screen_size[0]/2, self.screen_size[1]/1.2))
        self.image_x = self.screen_size[0]/3.8
        self.image_y = screen_size[1]

        self.upgrade_volume = 1
        self.click_volume = 1
        self.death_volume = 0.3
        self.sell_volume = 0.3

        self.resume_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "resume_button.png")).convert_alpha(),
                                                           (self.screen_size[0]/4, self.screen_size[1]/6)),
                                    self.image.get_width()/1.3, self.image.get_height()/4)

        self.restart_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "restart_button.png")).convert_alpha(),
                                                            (self.screen_size[0]/4, self.screen_size[1]/6)),
                                     self.image.get_width()/1.3, self.image.get_height()/2.1)

        self.main_menu_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "main_menu_button.png")).convert_alpha(),
                                                              (self.screen_size[0]/4, self.screen_size[1]/6)),
                                       self.image.get_width()/1.3, self.image.get_height()/1.42)

        self.music_on_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "music_on.png")).convert_alpha(),
                                                             (screen_size[0]/20, screen_size[0]/20)),
                                      self.image.get_width()*1.25, self.image.get_height()/1.08)

        self.music_off_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "music_off.png")).convert_alpha(),
                                                              (screen_size[0]/20, screen_size[0]/20)),
                                       self.image.get_width()*1.25, self.image.get_height()/1.08)

        self.sfx_on_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "sfx_on.png")).convert_alpha(),
                                                           (screen_size[0]/20, screen_size[0]/20)),
                                    self.image.get_width()*0.69, self.image.get_height()/1.08)

        self.sfx_off_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "sfx_off.png")).convert_alpha(),
                                                            (screen_size[0]/20, screen_size[0]/20)),
                                     self.image.get_width()*0.69, self.image.get_height()/1.08)

    def draw_menu(self, game) -> bool:
        """Méthode pour déssiner le menu
        - game: objet game correspondant à la partie courante
        Cette méthode gère l'affichage,b les clics efféctués par le joueur ainsi que l'animation du menu"""

        filler = pygame.Surface(self.screen_size, pygame.SRCALPHA)
        pygame.draw.rect(filler, (0, 0, 0, 128), pygame.Rect(
            0, 0, self.screen_size[0], self.screen_size[1]))
        self.image_y = balayage_haut(
            game.window, self.screen_size[1]/9, self.image, [self.image_x, self.image_y], game)

        running = 1
        while running:
            game.draw_window()
            game.window.blit(filler, (0, 0))
            game.window.blit(self.image, (self.image_x, self.image_y))
            self.resume_button.draw_and_scale(game.window)
            self.restart_button.draw_and_scale(game.window)
            self.main_menu_button.draw_and_scale(game.window)
            self.draw_sound_buttons(game.window)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_sound()
                    if self.resume_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        running = 0

                    if self.restart_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        self.reset_game(game)
                        running = 0

                    if self.main_menu_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        main_menu_confirm_menu = Main_menu_confirm_menu(
                            self.screen_size, self.sfx_state)
                        return main_menu_confirm_menu.draw(game)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = 0

            pygame.display.flip()

        balayage_bas(game.window, self.screen_size[1], self.image, [
                     self.image_x, self.image_y], game)
        self.image_y = self.screen_size[1]

        return 1

    def handle_sound(self) -> None:
        """Méthode pour gérer les sons et la musique
        Cette méthode permet d'activer ou de désactiver la musique ou les sons sfx"""

        if self.music_on_button.rect.collidepoint(pygame.mouse.get_pos()):
            if self.music_state:
                play_sound("click.ogg", 1, self.sfx_state)
                disable_music(self.music)
                self.music_state = False
            else:
                play_sound("click.ogg", 1, self.sfx_state)
                enable_music(self.music)
                self.music_state = True

        elif self.sfx_on_button.rect.collidepoint(pygame.mouse.get_pos()):
            if self.sfx_state:
                play_sound("click.ogg", 1, self.sfx_state)
                self.sfx_state = False
            else:
                self.sfx_state = True
                play_sound("click.ogg", 1, self.sfx_state)

    def draw_sound_buttons(self, window) -> None:
        """Méthode pour déssiner les boutons de sons
        - window: fenêtre pygame sur laquelle les boutons sont déssinés
        Cette méthode affiche les boutons en vert ou en rouge selon l'état de la musique et des sons sfx"""

        if self.music_state:
            self.music_on_button.draw_and_scale(window)
        else:
            self.music_off_button.draw_and_scale(window)

        if self.sfx_state:
            self.sfx_on_button.draw_and_scale(window)
        else:
            self.sfx_off_button.draw_and_scale(window)

    def reset_game(self, game) -> None:
        """Méthode pour reset la game pour pouvoir restart
        - game: objet game correspondant à la partie à reset"""

        game.fps = 60
        game.enemies = []
        game.towers = []
        game.projectiles = []
        game.selected_tower = None
        game.health = 50
        game.money = 250
        game.current_wave = 0
        game.enemy_index = 0
        game.time_since_last_enemy = 0
        game.wave_running = False
        game.available_wave = True
        game.menu.current_window = "main"
        if game.map is not None:
            game.map.reset_placements()
