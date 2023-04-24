import pygame
import os
from menus.Secondary_menu import Secondary_menu
from buttons.Bouton import Bouton
from effects.sound import play_sound


class Difficulty_menu(Secondary_menu):
    def __init__(self, screen_size: tuple, sfx_state: bool) -> None:
        super().__init__(screen_size)
        """Sous-classe Difficulty_menu:
        Cette sous classe représente le menu de difficulté qui s'affiche lorsque
        l'on clique sur une map dans le menu
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - sfx_state: booléen correspondant à l'état actuel des sons sfx"""

        self.text = pygame.font.SysFont('arialrounded', int(
            self.image_width/24)).render("Choisissez la difficulté", True, (0, 0, 0))
        self.easy_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "easy_button.png")).convert_alpha(),
                                                         (self.image_width/4, self.image_height/5)), self.image_x + self.image_width/9, self.image_y + self.image_height/2.4)

        self.medium_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "medium_button.png")).convert_alpha(),
                                                           (self.image_width/4, self.image_height/5)), self.image_x + self.image_width/2.65, self.image_y + self.image_height/2.4)

        self.hard_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "hard_button.png")).convert_alpha(),
                                                         (self.image_width/4, self.image_height/5)), self.image_x + self.image_width/1.55, self.image_y + self.image_height/2.4)

        self.back_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "back_button.png")).convert_alpha(),
                                                         (self.image_width/3.4, self.image_height/4.5)), self.image_x + self.image_width/2.8, self.image_y + self.image_height/1.6)
        self.sfx_state = sfx_state

    def draw(self, menu) -> bool:
        """Méthode pour déssiner et gérer les clics sur ce menu-
        - menu: objet menu correspondant au menu du jeu"""

        filler = pygame.Surface(self.screen_size, pygame.SRCALPHA)
        pygame.draw.rect(filler, (0, 0, 0, 128), pygame.Rect(
            0, 0, self.screen_size[0], self.screen_size[1]))

        running = 1
        while running:
            menu.draw_menu()
            menu.window.blit(filler, (0, 0))
            menu.window.blit(self.image, (self.image_x, self.image_y))
            menu.window.blit(
                self.text, (self.screen_size[0]/2.6, self.screen_size[1]/2.55))
            self.easy_button.draw_and_scale(menu.window)
            self.medium_button.draw_and_scale(menu.window)
            self.hard_button.draw_and_scale(menu.window)
            self.back_button.draw_and_scale(menu.window)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.easy_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        return "easy_upgrades.json"

                    elif self.medium_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        return "medium_upgrades.json"

                    elif self.hard_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        return "hard_upgrades.json"

                    elif self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        return None

            pygame.display.flip()
