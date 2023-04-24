import pygame
import os
from menus.Secondary_menu import Secondary_menu
from buttons.Bouton import Bouton
from effects.sound import play_sound


class Main_menu_confirm_menu(Secondary_menu):
    def __init__(self, screen_size: tuple, sfx_state: bool) -> None:
        super().__init__(screen_size)
        """Sous-classe Main_menu_confirm_menu:
        Cette classe est un menu de confirmation lorsque l'on clique sur le bouton 'main_menu' dans le menu échap
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - sfx_state: booléen correspondant à l'état actuel des sons sfx"""

        self.text = pygame.font.SysFont('arialrounded', int(
            self.image_width/27)).render("Voulez-vous retourner au menu pricipal ?", True, (0, 0, 0))
        self.yes_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "yes_button.png")).convert_alpha(),
                                                        (self.image_width/3, self.image_height/4)), self.image_x + self.image_width/8, self.image_y + self.image_height/1.8)
        self.no_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "no_button.png")).convert_alpha(),
                                (self.image_width/3, self.image_height/4)), self.image_x + self.image_width/1.8, self.image_y + self.image_height/1.8)
        self.sfx_state = sfx_state

    def draw(self, game) -> bool:
        """Méthode pour déssiner et gérer les clics du menu
        - game: objet game correspondant à la partie courante"""

        filler = pygame.Surface(self.screen_size, pygame.SRCALPHA)
        pygame.draw.rect(filler, (0, 0, 0, 128), pygame.Rect(
            0, 0, self.screen_size[0], self.screen_size[1]))

        running = 1
        while running:
            game.draw_window()
            game.window.blit(filler, (0, 0))
            game.window.blit(self.image, (self.image_x, self.image_y))
            game.window.blit(
                self.text, (self.screen_size[0]/3.2, self.screen_size[1]/2.3))
            self.yes_button.draw_and_scale(game.window)
            self.no_button.draw_and_scale(game.window)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.yes_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        return 0

                    elif self.no_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        return 1

            pygame.display.flip()
