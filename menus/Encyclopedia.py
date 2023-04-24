import pygame
import os
from buttons.Bouton import Bouton
from effects.effets import fondu_fermer
from effects.sound import play_sound, disable_music, enable_music
from menus.Enemies_menu import Enemies_menu
from menus.Physical_towers_menu import Physical_towers_menu
from menus.Magical_towers_menu import Magical_towers_menu


class Encyclopedia:
    def __init__(self, screen_size, sfx_state, music_state, music) -> None:
        """Classe Encyclopedia: elle comprend les boutons pour accéder
        aux differentes parties de l'encyclopédie (tours et ennemis)
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - sfx_state: booléen correspondant à l'état actuel des bruits sfx
        - music_state: booléen correspondant à l"état actuel de la musique
        - music: musique pygame actuelle"""

        self.screen_size = screen_size
        self.sfx_state = sfx_state
        self.music_state = music_state
        self.music = music
        self.current_window = "home"
        self.background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "other", "background.png")).convert_alpha(),
                                                 self.screen_size)
        self.music_on_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "music_on.png")).convert_alpha(),
                                                             (self.screen_size[0]/20, self.screen_size[0]/20)),
                                      self.screen_size[0]/1.07, 0)

        self.music_off_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "music_off.png")).convert_alpha(),
                                                              (self.screen_size[0]/20, self.screen_size[0]/20)),
                                       self.screen_size[0]/1.07, 0)

        self.sfx_on_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "sfx_on.png")).convert_alpha(),
                                                           (self.screen_size[0]/20, self.screen_size[0]/20)),
                                    self.screen_size[0]/1.13, 0)

        self.sfx_off_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "other_buttons", "sfx_off.png")).convert_alpha(),
                                                            (self.screen_size[0]/20, self.screen_size[0]/20)),
                                     self.screen_size[0]/1.13, 0)

        self.back_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "back_button.png")).convert_alpha(),
                                                         (self.screen_size[0]/7.68, self.screen_size[1]/10.8)),
                                  self.screen_size[0]/50, self.screen_size[1]/1.12)

        self.towers_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "towers_button.png")).convert_alpha(),
                                                           (self.screen_size[0]/2.56, self.screen_size[1]/3.6)),
                                    self.screen_size[0]/20, self.screen_size[1]/2.8)

        self.enemies_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "enemies_button.png")).convert_alpha(),
                                                            (self.screen_size[0]/2.56, self.screen_size[1]/3.6)),
                                     self.screen_size[0]/1.8, self.towers_button.y)

        self.physical_towers_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "physical_button.png")).convert_alpha(),
                                                                    (self.screen_size[0]/2.56, self.screen_size[1]/3.6)),
                                             self.screen_size[0]/20, self.towers_button.y)

        self.magical_towers_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "magical_button.png")).convert_alpha(),
                                                                   (self.screen_size[0]/2.56, self.screen_size[1]/3.6)),
                                            self.screen_size[0]/1.8, self.towers_button.y)

        self.encyclopedia_text = pygame.font.SysFont(
            'arialrounded', self.screen_size[1]//10).render('Encyclopedie', True, (0, 0, 0))

    def draw_encyclopedia(self, window) -> None:
        """Méthode permettant de lancer, faire tourner et dessiner le menu de l'encyclopédie"""

        running = 1
        while running:
            running = self.handle_click(window)
            window.blit(self.background, (0, 0))
            self.draw_sound_buttons(window)
            window.blit(self.encyclopedia_text,
                        (self.screen_size[0]/3.1, self.screen_size[1]/10))

            if self.current_window == "home":
                self.towers_button.draw_and_scale(window)
                self.enemies_button.draw_and_scale(window)
                self.back_button.draw_and_scale(window)

            elif self.current_window == "tower_choice":
                self.physical_towers_button.draw_and_scale(window)
                self.magical_towers_button.draw_and_scale(window)
                self.back_button.draw_and_scale(window)

            pygame.display.flip()

    def draw_sound_buttons(self, window) -> None:
        """Méthode pour dessiner les boutons de gestion de la musique et du son"""

        if self.music_state:
            self.music_on_button.draw_and_scale(window)
        else:
            self.music_off_button.draw_and_scale(window)

        if self.sfx_state:
            self.sfx_on_button.draw_and_scale(window)
        else:
            self.sfx_off_button.draw_and_scale(window)

    def handle_click(self, window) -> bool:
        """Méthode pour gérer les clics dans le menu de l'encyclopédie
        et renvoyant un booléen décidant si le menu doit se fermer ou non"""

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_LALT]:
                        exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                self.handle_music()

                if self.current_window == "home":
                    if self.towers_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        fondu_fermer(window, self.screen_size, 0.5, 50)
                        self.current_window = "tower_choice"

                    if self.enemies_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        fondu_fermer(window, self.screen_size, 0.5, 50)
                        enemies_menu = Enemies_menu(
                            self.screen_size, self.sfx_state, self.music_state, self.music)
                        return enemies_menu.run_menu(window)

                    if self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        fondu_fermer(window, self.screen_size, 0.5, 50)
                        return 0

                elif self.current_window == "tower_choice":
                    if self.physical_towers_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        fondu_fermer(window, self.screen_size, 0.5, 50)
                        physical_towers_menu = Physical_towers_menu(
                            self.screen_size, self.sfx_state, self.music_state, self.music)
                        return physical_towers_menu.run_menu(window)

                    if self.magical_towers_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        fondu_fermer(window, self.screen_size, 0.5, 50)
                        magical_towers_menu = Magical_towers_menu(
                            self.screen_size, self.sfx_state, self.music_state, self.music)
                        return magical_towers_menu.run_menu(window)

                    if self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        fondu_fermer(window, self.screen_size, 0.5, 50)
                        self.current_window = "home"

        return 1

    def handle_music(self) -> None:
        """Méthode pour gérer la musique dans le menu de l'encyclopédie"""

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
