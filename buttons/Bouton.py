import pygame


class Bouton:
    def __init__(self, image, x: float, y: float, name: str = None, sprite=None, assigned_tower=None) -> None:
        """Classe mère bouton
        - image: image pygame du bouton
        - x: nombre réel correspondant à la coordonnée x du bouton
        - y: nombre réel correspondant à la coordonnée y du bouton
        - name: nom du bouton (facultatif)
        - sprite: image pygame correspondant à ce qui apparaitra si on clique dessus (pour les tower buttons, donc on pourra déplacer ce paramètre pour alléger le code)
        - assigned_tower: objet Tower correspondant au bouton (pour les tower buttons donc pareil que pour le sprite)
        Cette classe représente une image pygame clicable"""

        self.image = image
        self.sprite = sprite
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.name = name
        self.scaled = False
        self.scaled_image = pygame.transform.scale(
            self.image, (self.width*1.1, self.height*1.1))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.assigned_tower = assigned_tower

    def draw_and_scale(self, window, offset=0) -> None:
        """Méthode pour déssiner et aggrandir le bouton si il est survolé par le curseur"""
        self.rect = pygame.Rect(self.x + offset, self.y,
                                self.width, self.height)

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.scaled = True
        else:
            self.scaled = False

        if self.scaled:
            window.blit(self.scaled_image, (self.x - self.width *
                        0.06 + offset, self.y - self.height*0.06))
        else:
            window.blit(self.image, (self.x + offset, self.y))
