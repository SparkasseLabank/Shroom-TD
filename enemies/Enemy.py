import pygame


class Enemy:
    def __init__(self, x: float, y: float, screen_size: tuple) -> None:
        """Classe mère représentant un ennemi
        - x: nombre réel correspondant à la position x de la tour
        - y: nombre réel correspondant à la position y de la tour
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre"""
        self.x = x
        self.y = y
        self.width = screen_size[0]/19.2
        self.height = screen_size[1]/10.8
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.destinations_checked = []
        self.distance_travelled = 0
        self.converted_image = None
        self.status = []

    def where_to_go(self, destinations: list):
        """Méthode pour choisir le prochain point vers lequel se diriger
        - destinations: liste des points désignant le chemin parcourut par les ennemis"""
        if len(self.destinations_checked) < len(destinations):
            if (self.x, self.y) == destinations[len(self.destinations_checked)]:
                self.destinations_checked.append(True)

            if len(self.destinations_checked) < len(destinations):
                self.forward(destinations[len(self.destinations_checked)])

    def forward(self, destination: tuple):
        """Méthode pour faire avancer l'ennemi vers un point
        - destination: point vers lequel va avancer l'ennemi"""
        diff_x = destination[0] - self.x
        diff_y = destination[1] - self.y

        if diff_x > 0:
            self.x += min(diff_x, self.speed)
        elif diff_x < 0:
            self.x -= min(abs(diff_x), self.speed)

        if diff_y > 0:
            self.y += min(diff_y, self.speed)
        elif diff_y < 0:
            self.y -= min(abs(diff_y), self.speed)

        self.distance_travelled += self.speed

    def draw(self, window):
        """Méthode pour afficher l'ennemi
        - window: fenêtre pygame sur laquelle l'ennemi sera dessiné"""
        if self.converted_image is None:
            self.converted_image = pygame.transform.scale(pygame.image.load(
                self.image_path).convert_alpha(), (self.width, self.height))

        window.blit(self.converted_image, (self.x, self.y))
        self.draw_health_bar(window)
        if self.type == "Boss":
            self.draw_shield_bar(window)

    def draw_health_bar(self, window):
        """Méthode pour afficher la barre de vie de l'ennemi
        - window: fenêtre pygame sur laquell la barre de vie sera dessinée"""
        BAR_LENGTH = 50
        BAR_HEIGHT = 5
        fill = (self.health / self.max_health) * BAR_LENGTH
        border_rect = pygame.Rect(
            self.x + self.width/7, self.y - self.height/15, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(self.x + self.width/7,
                                self.y - self.height/15, fill, BAR_HEIGHT)
        pygame.draw.rect(window, (50, 50, 50), border_rect)
        if self.health > self.max_health / 2:
            # enemi avec tout sa vie vert
            pygame.draw.rect(window, (0, 255, 0), fill_rect)
        elif self.health > self.max_health / 4:
            pygame.draw.rect(window, (255, 100, 0), fill_rect)
        else:
            pygame.draw.rect(window, (255, 0, 0), fill_rect)

    def draw_shield_bar(self, window):
        """Méthode pour afficher la barre de bouclier de l'ennemi
        - window: fenêtre pygame sur laquelle sera dessinée la barre de bouclier"""
        BAR_LENGTH = 50
        BAR_HEIGHT = 5
        fill_boss = (self.bouclier / self.max_bouclier) * BAR_LENGTH
        border_rect_boss = pygame.Rect(
            self.x + self.width/7, self.y - self.height/8, BAR_LENGTH, BAR_HEIGHT)
        fill_rect_boss = pygame.Rect(
            self.x + self.width/7, self.y - self.height/8, fill_boss, BAR_HEIGHT)
        pygame.draw.rect(window, (50, 50, 50), border_rect_boss)
        # enemi avec tout sa vie vert
        pygame.draw.rect(window, (150, 0, 255), fill_rect_boss)

    def check_status(self):
        """Méthode pour infliger les états à l'ennemi"""
        for element in self.status:
            status = element[0]
            duration = element[1]
            modifier = element[2]

            if status == "slowed":
                if duration == 0:
                    self.speed = self.max_speed
                    self.status.remove(element)

                else:
                    self.speed = int(round(self.max_speed*modifier))
                    element[1] -= 1

            elif status == "M.res debuff":
                if duration == 0:
                    self.resistance["Magic"] = self.max_resistance_magic
                    self.status.remove(element)

                elif self.resistance["Magic"] >= int(round(self.max_resistance_magic * modifier)):
                    self.resistance["Magic"] = int(
                        round(self.max_resistance_magic * modifier))
                    element[1] -= 1

            elif status == "P.res debuff":
                if duration == 0:
                    self.resistance["Physical"] = self.max_resistance_physic
                    self.status.remove(element)

                elif self.resistance["Physical"] >= int(round(self.max_resistance_physic * modifier)):
                    self.resistance["Physical"] = int(
                        round(self.max_resistance_physic * modifier))
                    element[1] -= 1

    def is_dead(self):
        """Méthode pour retourner si l'ennemi est mort (points de vie < 0)"""
        return self.health <= 0

    def is_out(self, out_pos):
        """Méthode pour retourner si l'ennemi est arrivé à la fin du chemin"""
        return (self.x, self.y) == out_pos

    def Bresistance(self):
        """Méthode polymorphisme (dans chaque sous-classe, une méthode du même nom
        est présente mais possède un comportement different)"""
        pass

    def bar_switch(self):
        """Méthode polymorphisme (dans chaque sous-classe, une méthode du même nom
        est présente mais possède un comportement different)"""
        pass
