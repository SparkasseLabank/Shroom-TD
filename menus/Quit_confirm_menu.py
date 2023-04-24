import pygame
import os
from buttons.Bouton import Bouton
from menus.Secondary_menu import Secondary_menu
from effects.sound import play_sound


class Quit_confirm_menu(Secondary_menu):
    def __init__(self, screen_size: tuple, sfx_state: bool) -> None:
        super().__init__(screen_size)
        """Sous-classe Quit_confirm_menu:
        Cette classe représente le petit menu de confirmation lors d'un clic sur le bouton 'Quit'
        - screen_size: tuple contenant la largeur et la hauteur de l'écran
        - sfx_state: booléen correspondant à l'état actuel des sons sfx"""

        self.text = pygame.font.SysFont('arialrounded', int(
            self.image_width/24)).render("Voulez-vous vraiment quitter le jeu ?", True, (0, 0, 0))
        self.yes_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "yes_button.png")).convert_alpha(),
                                                        (self.image_width/3, self.image_height/4)), self.image_x + self.image_width/8, self.image_y + self.image_height/1.8)
        self.no_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "no_button.png")).convert_alpha(),
                                (self.image_width/3, self.image_height/4)), self.image_x + self.image_width/1.8, self.image_y + self.image_height/1.8)
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
                self.text, (self.screen_size[0]/3.15, self.screen_size[1]/2.3))
            self.yes_button.draw_and_scale(menu.window)
            self.no_button.draw_and_scale(menu.window)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.yes_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        return 0

                    elif self.no_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        return 1

            pygame.display.flip()
