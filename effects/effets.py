import pygame


def fondu_fermer(window, screen_size:tuple, speed:float, interval:float) -> None:
    """Fonction d'animation de fondu (obscurcissement de la fenêtre)
    - window: fenêtre sur laquelle l'animation est appliquée
    - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
    - speed: nombre réel représentant la vitesse à laquelle l'écran devient noir
    - interval: nombre réel représentant la fluidité à laquelle l'écran devient noir
    (plus l'intervalle est petite, plus l'animation sera fluide, mais il faudra donc réduire la vitesse)"""

    last_fill = 0
    current_opacity = 0
    filler = pygame.Surface(screen_size, pygame.SRCALPHA)
    while current_opacity <= interval:
        current_time = pygame.time.get_ticks()
        if current_time - last_fill >= 10:
            pygame.draw.rect(filler, (0, 0, 0, current_opacity), pygame.Rect(0, 0, screen_size[0], screen_size[1]))
            window.blit(filler, (0, 0))
            pygame.display.flip()
            current_opacity += speed
            last_fill = current_time


def fondu_ouvrir(window, pos:tuple, image) -> bool:
    """Fonction d'animation de fondu (éclaircissmeent d'une image),
    elle renvoie un booléen qui sert à passer l'animation complète au lancement de jeu
    - window: fenêtre sur laquelle l'animation est appliquée
    - pos: position de l'image qui sera animée
    - image: image qui sera animée"""

    last_fill = 0
    current_opacity = 10
    while current_opacity >= 0:
        current_time = pygame.time.get_ticks()
        if current_time - last_fill >= 10: #intervalle
            image.set_alpha(current_opacity)
            window.blit(image, (pos[0], pos[1]))
            pygame.display.flip()
            current_opacity -= 0.1
            last_fill = current_time
    image.set_alpha(255)


def balayage_haut(window, max_height:float, image, image_pos:list, game) -> float:
    """Fonction d'animation de balayage vers le haut qui renvoie
    la position y de l'image à la fin de l'animation
    - window: fenêtre sur laquelle l'animation est appliquée
    - max_height: nombre réel représentant la coordonnée y à laquelle l'image s'arrêtera
    - image: image qui sera animée
    - image_pos: liste contenant les coordonnées de l'image qui sera animée
    - game: objet game permettant de continuer à dessiner les éléments derrière le menu"""

    while image_pos[1] >= max_height:
        game.draw_window()
        image_pos[1] -= 25 #speed
        window.blit(image, (image_pos[0], image_pos[1]))
        pygame.display.flip()
    return image_pos[1]


def balayage_bas(window, min_height:float, image, image_pos:list, game) -> float:
    """Fonction d'animation de balayage vers le bas qui renvoie
    la position y de l'image à la fin de l'animation
    - window: fenêtre sur laquelle l'animation est appliquée
    - max_height: nombre réel représentant la coordonnée y à laquelle l'image s'arrêtera
    - image: image qui sera animée
    - image_pos: liste contenant les coordonnées de l'image qui sera animée
    - game: objet game permettant de continuer à dessiner les éléments derrière le menu"""

    while image_pos[1] <= min_height:
        game.draw_window()
        image_pos[1] += 25 #speed
        window.blit(image, (image_pos[0], image_pos[1]))
        pygame.display.flip()
    return image_pos[1]

