import pygame
from buttons.Bouton import Bouton


class Tower_button(Bouton):
    def __init__(self, image, x: float, y: float, name: str, sprite, assigned_tower, screen_size: tuple) -> None:
        super().__init__(image, x, y, name, sprite, assigned_tower)
        """Sous-classe de Bouton Tower_button
        - image: image pygame du bouton
        - x: nombre réel correspondant à la coordonnée x du bouton
        - y: nombre réel correspondant à la coordonnée y du bouton
        - name: nom du bouton
        - sprite: image pygame correspondant à ce qui apparaitra si on clique dessus
        - assigned_tower: objet Tower correspondant au bouton
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre
        Cette classe représente un bouton clicable correspondant à une tour"""

        self.cost_text = pygame.font.SysFont(
            'impact', screen_size[1]//50).render(str(self.assigned_tower.cost), True, (255, 255, 255))
        self.cost_text_position = (self.x + self.width/8, 5)
        self.placement_type = assigned_tower.placement_type
