import pygame
from menus.Menu import Menu


def run() -> None:
    """Méthode pour initialiser les éléments de pygame
    et pour lancer le jeu"""

    pygame.init()
    pygame.font.init()

    menu = Menu()
    menu.run()


if __name__ == "__main__":
    run()
