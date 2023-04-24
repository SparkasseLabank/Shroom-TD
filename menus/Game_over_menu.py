import pygame
import os
from menus.Secondary_menu import Secondary_menu
from buttons.Bouton import Bouton
from effects.sound import play_sound, play_music


class Game_over_menu(Secondary_menu):
    def __init__(self, screen_size: tuple, sfx_state: bool, text: str, text_pos: tuple) -> None:
        super().__init__(screen_size)
        """Sous-classe Game_over_menu:
        Cette classe est un menu qui s'affiche lorsque le joueur a fini la partie (gagné ou perdu)
        et lui permet de choisir s'il veut retourner au menu ou rejouer la même partie
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        - sfx_state: booléen correspondant à l'état actuel des sons sfx
        - text: chaine de caractère correspondant au texte affiché
        - text_pos: tuple contenant les coefficients multiplicateurs permettant de positionner le texte correctement"""

        self.text = pygame.font.SysFont('arialrounded', int(
            self.image_width/20)).render(text, True, (0, 0, 0))
        self.text_pos = text_pos
        self.sfx_state = sfx_state
        self.main_menu_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "main_menu_button.png")).convert_alpha(),
                                                              (self.image_width/3, self.image_height/4)), self.image_x + self.image_width/8, self.image_y + self.image_height/1.8)
        self.restart_button = Bouton(pygame.transform.scale(pygame.image.load(os.path.join("assets", "buttons", "menu_buttons", "restart_button.png")).convert_alpha(),
                                                            (self.image_width/3, self.image_height/4)), self.image_x + self.image_width/1.8, self.image_y + self.image_height/1.8)

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
            game.window.blit(self.text, self.text_pos)
            self.main_menu_button.draw_and_scale(game.window)
            self.restart_button.draw_and_scale(game.window)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.main_menu_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        return 0

                    elif self.restart_button.rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound("click.ogg", 1, self.sfx_state)
                        self.reset_game(game)
                        return 1

            pygame.display.flip()

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
            play_music(game.map.music, game.escape_menu.music_state)
            game.map.reset_placements()
