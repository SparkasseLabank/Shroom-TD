import pygame
import os
from buttons.Bouton import Bouton
from effects.effets import fondu_fermer
from effects.sound import play_sound, disable_music, enable_music


class Physical_towers_menu:
    def __init__(self, screen_size, sfx_state, music_state, music) -> None:
        """Classe Physical_towers_menu: elle contient les cartes descriptives
        des tours à dégâts physiques du jeu
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - sfx_state: booléen correspondant à l'état actuel des bruits sfx
        - music_state: booléen correspondant à l"état actuel de la musique
        - music: musique pygame actuelle"""

        self.screen_size = screen_size
        self.music_state = music_state
        self.music = music
        self.sfx_state = sfx_state
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

        self.details_back_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "back_button.png")).convert_alpha(),
                                                                 (self.screen_size[0]/7.68, self.screen_size[1]/10.8)),
                                          self.screen_size[0]/2.35, self.screen_size[1]/1.12)

        self.physical_towers_list = [Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "classic_shroom.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/60, self.screen_size[1]/8,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "classic_shroom.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "sniper_shroom.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/7, self.screen_size[1]/8,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "sniper_shroom.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "boom_shroom.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/3.75, self.screen_size[1]/8,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "boom_shroom.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "gangsta_shroom.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/2.56, self.screen_size[1]/8,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "gangsta_shroom.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "urchin_shroom.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/1.94, self.screen_size[1]/8,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "urchin_shroom.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "water_strider_shroom.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/1.56, self.screen_size[1]/8,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "water_strider_shroom.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "random_shroom.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/1.305, self.screen_size[1]/8,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "random_shroom.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "classic_shroom_back.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/60, self.screen_size[1]/2,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "classic_shroom_back.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "sniper_shroom_back.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/7, self.screen_size[1]/2,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "sniper_shroom_back.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "boom_shroom_back.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/3.75, self.screen_size[1]/2,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "boom_shroom_back.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "gangsta_shroom_back.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/2.56, self.screen_size[1]/2,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "gangsta_shroom_back.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "urchin_shroom_back.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/1.94, self.screen_size[1]/2,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "urchin_shroom_back.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "water_strider_shroom_back.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/1.56, self.screen_size[1]/2,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "water_strider_shroom_back.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2))),
                                     Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "random_shroom_back.png")).convert_alpha(),
                                                                   (self.screen_size[0]/8.35, self.screen_size[1]/3.13)),
                                            self.screen_size[0]/1.305, self.screen_size[1]/2,
                                            sprite=pygame.transform.scale(pygame.image.load(os.path.join("assets", "towers", "descriptifs", "random_shroom_back.png")),
                                                                          (self.screen_size[0]/3.2, self.screen_size[1]/1.2)))]

    def run_menu(self, window) -> bool:
        """Méthode pour faire tourner le menu
        - window: fenêtre pygame sur laquelle le menu sera déssiné"""
        running = 1
        while running:
            running = self.handle_clicks(window)
            self.draw_menu(window)
        return 1

    def draw_menu(self, window) -> None:
        """Méthode pour afficher le menu
        - window: fenêtre pygame sur laquelle le menu sera déssiné"""
        window.blit(self.background, (0, 0))
        self.draw_sound_buttons(window)
        self.back_button.draw_and_scale(window)
        for card in self.physical_towers_list:
            card.draw_and_scale(window, self.screen_size[0]/24)

        pygame.display.flip()

    def draw_sound_buttons(self, window) -> None:
        """Méthode pour dessiner les boutons de gestion de la musique et du son
        - window: fenêtre pygame sur laquelle le menu sera déssiné"""

        if self.music_state:
            self.music_on_button.draw_and_scale(window)
        else:
            self.music_off_button.draw_and_scale(window)

        if self.sfx_state:
            self.sfx_on_button.draw_and_scale(window)
        else:
            self.sfx_off_button.draw_and_scale(window)

    def handle_clicks(self, window) -> bool:
        """Méthode pour gérer les cliques
        - window: fenêtre pygame sur laquelle les cliques sont gérés"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_LALT]:
                        exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_music()
                for card in self.physical_towers_list:
                    if card.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        self.show_card(window, card)
                        break

                if self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                    play_sound("click.ogg", 1, self.sfx_state)
                    fondu_fermer(
                        window, (self.screen_size[0], self.screen_size[1]), 0.5, 50)
                    return 0
        return 1

    def handle_music(self) -> None:
        """Méthode pour gérer les sons"""
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

    def show_card(self, window, card) -> None:
        """Méthode permettant d'afficher une carte en grand
        - window: fenêtre pygame sur laquelle la carte sera desssinée
        - card: élément de la classe bouton dont l'image va être affichée en grand"""
        running = 1
        while running:
            window.blit(self.background, (0, 0))
            window.blit(
                card.sprite, (self.screen_size[0]/3, self.screen_size[1]/20))
            self.details_back_button.draw_and_scale(window)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.details_back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        running = 0

            pygame.display.flip()
