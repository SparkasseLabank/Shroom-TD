class Projectile:
    def __init__(self, x: float, y: float, target, screen_size: tuple) -> None:
        """Classe mère projectile représentant le projectile de sa tour
        - x: nombre réel correspondant à la coordonnée x initiale du projectile
        - y: nombre réel correspondant à la coordonnée y initiale du projectile
        - target: ennemi ciblé
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre"""

        self.x = x
        self.y = y
        self.target = target
        self.screen_size = screen_size

    def handle(self, projectiles: list) -> list:
        """Méthode pour gérer les projectiles
        - projectiles: liste des projectiles présents dans le jeu
        Cette méthode calcule le coefficient directeur du vecteur entre le projectile et la cible
        et déplace le projectile en fonction de celui-ci grâce a la méthode move()"""

        vecteur = (self.target.x + self.target.width/2 - self.x,
                   self.target.y + self.target.height/2 - self.y)
        if vecteur[0] != 0:
            coef_directeur = abs(vecteur[1] / vecteur[0])
        else:
            coef_directeur = abs(vecteur[1] / 0.000000001)

        if self.target.y + self.target.height/2 >= self.y + self.target.height/2:
            if self.target.x + self.target.width/2 >= self.x + self.target.width/2:
                self.move(coef_directeur, "down_right")
            elif self.target.x + self.target.width/2 <= self.x - self.target.width/2:
                self.move(coef_directeur, "down_left")
            else:
                self.move(coef_directeur, "down")
        else:
            if self.target.x + self.target.width/2 >= self.x + self.target.width/2:
                self.move(coef_directeur, "up_right")
            elif self.target.x + self.target.width/2 <= self.x - self.target.width/2:
                self.move(coef_directeur, "up_left")
            else:
                self.move(coef_directeur, "up")

        if self.target.x <= self.x <= self.target.x + self.target.width and self.target.y <= self.y <= self.target.y + self.target.height or not self.target:
            exist = True
            self.attack()
            if hasattr(self, "creator"):
                if self.target == self.creator:
                    projectiles.remove(self)
            if hasattr(self, "return_to_sender"):
                self.target = self.creator
            elif not hasattr(self, "return_to_sender"):
                projectiles.remove(self)
                del self
                exist = False
            if exist:
                if hasattr(self, "creator"):
                    if self.target == self.creator:
                        del self

        return projectiles

    def move(self, coef_directeur: float, aim_point: str) -> None:
        """Méthode pour déplacer le projectile en fonction du coefficient directeur
        du vecteur entre le projectile et l'ennemi
        - coef_directeur: nombre réel correspondant au coefficient directeur du vecteur
        - aim_point: chaine de caractère désignant la direction dans laquelle le projectile doit se diriger"""

        if aim_point == "up_right":
            self.x += self.speed
            self.y -= coef_directeur * self.speed
        elif aim_point == "down_right":
            self.x += self.speed
            self.y += coef_directeur * self.speed
        elif aim_point == "up_left":
            self.x -= self.speed
            self.y -= coef_directeur * self.speed
        elif aim_point == "down_left":
            self.x -= self.speed
            self.y += coef_directeur * self.speed
        elif aim_point == "up":
            self.y -= self.speed
        elif aim_point == "down":
            self.y += self.speed

    def draw(self, window) -> None:
        """Méthode pour déssiner le projectile
        - window: fenêtre pygame sur laquelle le projectile sera déssiné"""
        window.blit(self.image, (self.x, self.y))

    def attack(self):
        """Méthode polymorphisme (méthode de même nom dans les sous-classes mais avec un comportement différent)"""
        raise NotImplementedError(
            "Fonction pas implémenté pour cette classe")
