import pygame
import os
import copy
import json
import towers
from core.Map import Map
from core.generateur_wave import wave
from menus.Escape_menu import Escape_menu
from menus.Menu_bar import Menu_bar
from menus.Upgrade_menu import Upgrade_menu
from menus.Game_over_menu import Game_over_menu
from effects.effets import fondu_fermer
from effects.sound import play_sound, play_music, stop_music

from enemies.Bslime import Bslime
from enemies.Gslime import Gslime
from enemies.Oslime import Oslime
from enemies.Wslime import Wslime
from enemies.GOslime import GOslime
from enemies.Yslime import Yslime
from enemies.Pslime import Pslime
from enemies.Rslime import Rslime
from enemies.Cslime import Cslime
from enemies.GYslime import GYslime
from enemies.Vslime import Vslime
from enemies.BBoss import Bboss
from enemies.GBoss import Gboss
from enemies.WBoss import Wboss


class Game:
    def __init__(self, menu, nom_map: str, difficulty: str) -> None:
        """Classe représentant une partie
        - menu: objet menu permettant d'y retourner après la partie
        - nom_map: chaine de caractères permettant de connaître la
        map choisie par le joueur
        - difficulty: chaine de caractères correspondant a un fichier json qui
        sera choisi pour les prix des tours et des upgrades"""

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(
            flags=pygame.FULLSCREEN | pygame.DOUBLEBUF)
        self.width = self.window.get_width()
        self.height = self.window.get_height()
        self.enemies = []
        self.towers = []
        self.projectiles = []
        self.selected_tower = None
        self.upgrade_menu = None
        self.health = 50
        self.money = 250
        self.current_wave = 0
        self.enemy_index = 0
        self.time_since_last_enemy = 0
        self.wave_running = False
        self.available_wave = True
        self.menu = menu
        self.tower_on_cursor = None
        self.difficulty = difficulty
        if self.difficulty == "easy_upgrades.json":
            self.last_wave = 50
        elif self.difficulty == "medium_upgrades.json":
            self.last_wave = 75
        else:
            self.last_wave = 100
        self.menu_bar = Menu_bar((self.width, self.height), self.health,
                                 self.money, self.current_wave, self.difficulty, self.last_wave)
        self.current_tick = 0
        self.map = None
        self.nom_map = nom_map
        self.map = Map(nom_map, (self.width, self.height))
        self.convert_waves = {
            "blue_slime": Bslime(self.map.start[0], self.map.start[1], (self.width, self.height)),
            "green_slime": Gslime(self.map.start[0], self.map.start[1], (self.width, self.height)),
            "orange_slime": Oslime(self.map.start[0], self.map.start[1], (self.width, self.height)),
            "white_slime": Wslime(self.map.start[0], self.map.start[1], (self.width, self.height)),
            "golden_slime": GOslime(self.map.start[0], self.map.start[1], (self.width, self.height)),

            "yellow_slime": Yslime(self.map.start[0], self.map.start[1], (self.width, self.height)),
            "pink_slime": Pslime(self.map.start[0], self.map.start[1], (self.width, self.height)),
            "cyan_slime": Cslime(self.map.start[0], self.map.start[1], (self.width, self.height)),
            "red_slime": Rslime(self.map.start[0], self.map.start[1], (self.width, self.height)),
            "grey_slime": GYslime(self.map.start[0], self.map.start[1], (self.width, self.height)),
            "violet_slime": Vslime(self.map.start[0], self.map.start[1], (self.width, self.height)),

            "Boss_blue": Bboss(self.map.start[0], self.map.start[1], (self.width, self.height)),
            "Boss_green": Gboss(self.map.start[0], self.map.start[1], (self.width, self.height)),
            "Boss_white": Wboss(self.map.start[0], self.map.start[1], (self.width, self.height))
        }

        self.escape_menu = Escape_menu(
            (self.width, self.height), self.map.music)
        play_music(self.map.music, self.escape_menu.music_state)

    def run(self) -> None:
        """Méthode pour lancer, faire tourner le jeu
        Cette méthode comprends:
        - La gestion des ennemis/vagues et ses boutons
        - La gestion des clics à l'aide de la méthode handle_clicks()
        - La gestion de fin de jeu
        - La gestion de tirs des tours et projectiles
        - L'affichage de tous les éléments graphiques de la partie"""

        menu = self.menu

        running = 1
        while running:
            self.clock.tick(self.fps)
            self.current_tick += 1

            # Trier la liste des ennemis pour que les tours tirent sur le dernier ennemi
            self.enemies.sort(
                key=lambda enemy: enemy.distance_travelled, reverse=True)

            # Remettre le bouton en vert à la fin des vagues
            if not self.available_wave:
                if not self.enemies and not self.wave_running:
                    self.available_wave = True

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Clic gauche
                    if event.button == 1:
                        self.handle_clicks()

                    # Clic droit
                    elif event.button == 3:
                        self.selected_tower = None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = self.escape_menu.draw_menu(self)

                    if event.key == pygame.K_F4:
                        key = pygame.key.get_pressed()
                        if key[pygame.K_LALT]:
                            exit()

            if self.health <= 0:
                running = self.game_over()

            if self.current_wave == self.last_wave and self.available_wave == True:
                running = self.win()

            # Gerer les ennemis
            if self.enemies:
                for enemy in self.enemies:
                    enemy.check_status()
                    enemy.where_to_go(self.map.path)
                    enemy.bar_switch()

                    if enemy.is_out(self.map.path[len(self.map.path)-1]):
                        self.enemies.remove(enemy)
                        self.health -= enemy.damage
                        del enemy

                    elif enemy.is_dead():
                        play_sound(["mort1.ogg", "mort2.ogg", "mort3.ogg",
                                   "mort4.ogg", "mort5.ogg"], 0.3, self.escape_menu.sfx_state)
                        self.enemies.remove(enemy)
                        self.money += enemy.money_value
                        del enemy

            # Tir des tours
            if self.towers:
                for tower in self.towers:
                    if self.enemies:

                        targetable_enemies = []
                        for enemy in self.enemies:
                            if tower.can_shoot(enemy):
                                targetable_enemies.append(enemy)
                        if targetable_enemies != []:
                            if tower.name == "Gangsta Shroom" or tower.name == "Random Shroom" or tower.name == "Stun Shroom" or tower.name == "Urchin Shroom":
                                tower.main_attack(target=None, enemies=targetable_enemies,
                                                  current_tick=self.current_tick, projectiles=self.projectiles)
                            elif tower.name == "Spirit Shroom":
                                tower.main_attack(target=targetable_enemies[len(
                                    targetable_enemies)//2], enemies=targetable_enemies, current_tick=self.current_tick, projectiles=self.projectiles)
                            else:
                                tower.main_attack(
                                    target=targetable_enemies[0], enemies=self.enemies, current_tick=self.current_tick, projectiles=self.projectiles)
                        elif tower.name == "Spirit Shroom":
                            tower.reset_sprite()
                    elif tower.name == "Spirit Shroom":
                        tower.reset_sprite()

            if self.projectiles:
                for projectile in self.projectiles:
                    self.projectiles = projectile.handle(self.projectiles)

            if self.wave_running:
                self.run_wave()

            if self.upgrade_menu is not None and self.selected_tower is not None:
                if self.selected_tower.level[0] != "max" and self.selected_tower.level[1] != "max":
                    self.upgrade_menu.first_upgrade_available = self.money >= self.selected_tower.upgrades[self.selected_tower.name]["0"][str(
                        self.selected_tower.level[0]+1)]["upgrade_cost"]
                    self.upgrade_menu.second_upgrade_available = self.money >= self.selected_tower.upgrades[self.selected_tower.name]["1"][str(
                        self.selected_tower.level[1]+1)]["upgrade_cost"]

            self.draw_window()
            pygame.display.flip()

        stop_music(self.map.music)
        fondu_fermer(self.window, (self.width, self.height), 0.5, 50)
        del self
        menu.run()

    def draw_window(self) -> None:
        """Méthode pour dessiner, actualiser la fenêtre
        (Map, ennemis, tours, projectiles, tour séléctionnée,
        barre en haut de l'écran et menu d'amélioration)"""

        self.window.blit(
            self.map.bg, (0, self.menu_bar.menu_bar_rect.get_height()))

        for enemy in self.enemies:
            enemy.draw(self.window)

        for tower in self.towers:
            tower.draw(self.window)

        for projectile in self.projectiles:
            projectile.draw(self.window)

        if self.selected_tower != None:
            self.window.blit(self.selected_tower.range_circle, (self.selected_tower.x + self.selected_tower.width//2 - self.selected_tower.range,
                                                                self.selected_tower.y + self.selected_tower.height//2 - self.selected_tower.range))
            self.window.blit(self.selected_tower.image,
                             (self.selected_tower.x, self.selected_tower.y))

        self.menu_bar.update_texts(self.health, self.money, self.current_wave)
        self.menu_bar.draw(self.window, (self.width, self.height))
        self.draw_upgrade_menu()

        if self.available_wave:
            self.menu_bar.start_wave_button.draw_and_scale(self.window)
        else:
            self.window.blit(self.menu_bar.unavailable_button,
                             (self.menu_bar.start_wave_button.x, self.menu_bar.start_wave_button.y))

        if self.fps == 60:
            self.menu_bar.accelerate_off_button.draw_and_scale(self.window)
        else:
            self.menu_bar.accelerate_on_button.draw_and_scale(self.window)

    def draw_upgrade_menu(self) -> None:
        """Méthode pour dessiner le menu d'amélioration
        On utilise ici la classe Upgrade_menu ainsi que sa méthode draw"""

        if self.selected_tower is not None:
            if self.upgrade_menu is None:
                self.upgrade_menu = Upgrade_menu(
                    self.selected_tower, (self.width, self.height))

            self.upgrade_menu.draw(self.window, self.money)

        else:
            self.upgrade_menu = None

    def start_wave(self) -> None:
        """Méthode pour lancer une vague"""

        if not self.wave_running and not self.enemies:
            self.wave_running = True
            self.available_wave = False
            self.current_wave += 1

    def run_wave(self) -> None:
        """Méthode pour envoyer les ennemis de la vague lancée"""

        if self.current_tick - self.time_since_last_enemy >= wave(self.current_wave)[self.enemy_index][1]:
            if self.current_wave != 101:
                self.enemies.append(copy.deepcopy(
                    self.convert_waves[wave(self.current_wave)[self.enemy_index][0]]))
                self.time_since_last_enemy = self.current_tick
                self.enemy_index += 1
                if self.enemy_index == len(wave(self.current_wave)):
                    self.wave_running = False
                    self.enemy_index = 0
            else:
                pass

    def select_placement(self, placement_type: str):
        """Méthode pour permettre au joueur de choisir l'emplacement de sa nouvelle tour
        - placement_type: chaine de caractères précisant le type d'emplacement (Terre ou eau)
        Elle affiche les emplacements disponibles pour la tour séléctionnée et la dessine sur le curseur
        Lorsqu'un clic est effectué sur un emplacement, la tour se place et l'emplacement n'est plus libre"""

        selected_square = []
        place_circle = pygame.transform.scale(pygame.image.load(os.path.join(
            "assets", "other", "emplacement.png")).convert_alpha(), (self.width/38.4, self.height/21.6))

        while selected_square == []:
            self.draw_window()

            if placement_type == "Ground" and self.map.tower_places != [[]]:
                for place in self.map.tower_places:
                    if self.nom_map == "prairie":
                        self.window.blit(
                            place_circle, (place[0]+self.map.unitL/3.2, place[1]+self.map.unit/3.2))
                    else:
                        self.window.blit(
                            place_circle, (place[0]+self.map.unitL/6.4, place[1]+self.map.unit/6.4))

            elif placement_type == "Water" and self.map.water_places != [[]]:
                for place in self.map.water_places:
                    if self.nom_map == "prairie":
                        self.window.blit(
                            place_circle, (place[0]+self.map.unitL/3.2, place[1]+self.map.unit/3.2))
                    else:
                        self.window.blit(
                            place_circle, (place[0]+self.map.unitL/6.4, place[1]+self.map.unit/6.4))

            for available_tower in self.menu_bar.tower_buttons:
                if self.tower_on_cursor == available_tower.name:
                    circle = pygame.Surface((available_tower.assigned_tower.range*2,
                                            available_tower.assigned_tower.range*2), pygame.SRCALPHA).convert_alpha()
                    pygame.draw.circle(circle, (50, 50, 50, 128), (available_tower.assigned_tower.range,
                                       available_tower.assigned_tower.range), available_tower.assigned_tower.range)
                    self.window.blit(circle, (pygame.mouse.get_pos()[
                                     0]-circle.get_width()/2, pygame.mouse.get_pos()[1]-circle.get_height()/2))
                    self.window.blit(available_tower.sprite, (pygame.mouse.get_pos()[
                                     0]-available_tower.width/2, pygame.mouse.get_pos()[1]-available_tower.height/2))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        selected_square = None

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    selected_square = None

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if placement_type == "Ground" and self.map.tower_places != [[]]:
                        for place in self.map.tower_places:
                            if place[0] <= mouse[0] <= place[0]+self.map.unitL and place[1] <= mouse[1] <= place[1]+self.map.unit:
                                selected_square = place

                    elif placement_type == "Water" and self.map.water_places != [[]]:
                        for place in self.map.water_places:
                            if place[0] <= mouse[0] <= place[0]+self.map.unitL and place[1] <= mouse[1] <= place[1]+self.map.unit:
                                selected_square = place

        return selected_square

    def handle_clicks(self) -> None:
        """Méthode pour gérer les clics efféctués par le joueur
        (Boutons de vague, accélération, amélioration, vente
        (gère aussi la libération des emplacements lors de la vente) et selection de tour)"""

        if self.upgrade_menu is None:
            for available_tower in self.menu_bar.tower_buttons:
                self.buy_tower(available_tower)

        elif self.upgrade_menu.first_upgrade_button.rect.collidepoint(pygame.mouse.get_pos()):
            self.money = self.selected_tower.upgrade(
                self.money, self.escape_menu.sfx_state, 0)
            self.upgrade_menu.update(self.selected_tower)

        elif self.upgrade_menu.second_upgrade_button.rect.collidepoint(pygame.mouse.get_pos()):
            self.money = self.selected_tower.upgrade(
                self.money, self.escape_menu.sfx_state, 1)
            self.upgrade_menu.update(self.selected_tower)

        elif self.upgrade_menu.sell_button.rect.collidepoint(pygame.mouse.get_pos()):
            play_sound("money.ogg", 0.3, self.escape_menu.sfx_state)

            if self.selected_tower.placement_type == "Ground":
                self.money = self.selected_tower.sell(
                    self.money, self.towers, self.map.tower_places)

            elif self.selected_tower.placement_type == "Water":
                self.money = self.selected_tower.sell(
                    self.money, self.towers, self.map.water_places)

            self.selected_tower = None

        if self.menu_bar.start_wave_button.rect.collidepoint(pygame.mouse.get_pos()):
            self.start_wave()

        # Détecte si une tour à été cliqué, si oui la selectionne
        else:
            for tower in self.towers:
                if tower.rect.collidepoint(pygame.mouse.get_pos()):
                    self.selected_tower = tower
                    if self.upgrade_menu is not None:
                        self.upgrade_menu.update(self.selected_tower)

        for tower in self.towers:
            if tower.rect.collidepoint(pygame.mouse.get_pos()):
                self.selected_tower = tower

        if self.fps == 60:
            if self.menu_bar.accelerate_off_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.fps = 120
        else:
            if self.menu_bar.accelerate_on_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.fps = 60

    def buy_tower(self, element) -> None:
        """Méthode pour permettre au joueur d'acheter une tour si il clique sur un bouton
        - element: Bouton d'achat de tour (menu d'achat en haut de l'écran)
        (Vérifie si le joueur a assez d'argent et enlève l'emplacement de la liste des
        emplacements libres au moment de l'achat)"""

        if element.rect.collidepoint(pygame.mouse.get_pos()):
            if self.money >= element.assigned_tower.cost and self.map.tower_places:
                self.tower_on_cursor = element.name
                self.selected_tower = None
                placement = self.select_placement(element.placement_type)
                if placement is not None:
                    if element.name == "Cshroom":
                        self.towers.append(towers.Cshroom.Cshroom(
                            placement[0], placement[1], (self.width, self.height), self.difficulty))
                    elif element.name == "Sshroom":
                        self.towers.append(towers.Sshroom.Sshroom(
                            placement[0], placement[1], (self.width, self.height), self.difficulty))
                    elif element.name == "SNshroom":
                        self.towers.append(towers.SNshroom.SNshroom(
                            placement[0], placement[1], (self.width, self.height), self.difficulty))
                    elif element.name == "Bshroom":
                        self.towers.append(towers.Bshroom.Bshroom(
                            placement[0], placement[1], (self.width, self.height), self.difficulty))
                    elif element.name == "Wshroom":
                        self.towers.append(towers.Wshroom.Wshroom(
                            placement[0], placement[1], (self.width, self.height), self.difficulty))
                    elif element.name == "Gshroom":
                        self.towers.append(towers.Gshroom.Gshroom(
                            placement[0], placement[1], (self.width, self.height), self.difficulty))
                    elif element.name == "Rshroom":
                        self.towers.append(towers.Rshroom.Rshroom(
                            placement[0], placement[1], (self.width, self.height), self.difficulty))
                    elif element.name == "SPshroom":
                        self.towers.append(towers.SPshroom.SPshroom(
                            placement[0], placement[1], (self.width, self.height), self.difficulty))
                    elif element.name == "LPshroom":
                        self.towers.append(towers.LPshroom.LPshroom(
                            placement[0], placement[1], (self.width, self.height), self.difficulty))
                    elif element.name == "Ushroom":
                        self.towers.append(towers.Ushroom.Ushroom(
                            placement[0], placement[1], (self.width, self.height), self.difficulty))
                    elif element.name == "Ashroom":
                        self.towers.append(towers.Ashroom.Ashroom(
                            placement[0], placement[1], (self.width, self.height), self.difficulty))
                    elif element.name == "WSshroom":
                        self.towers.append(towers.WSshroom.WSshroom(
                            placement[0], placement[1], (self.width, self.height), self.difficulty))

                    if element.placement_type == "Ground":
                        self.map.tower_places.remove(placement)
                    elif element.placement_type == "Water":
                        self.map.water_places.remove(placement)
                    self.money -= element.assigned_tower.cost

    def game_over(self) -> bool:
        """Méthode créant le menu de fin de partie et renvoyant un booléen décidant
        si la partie se relance ou si le joueur revient au menu principal"""

        stop_music(self.map.music)
        menu = Game_over_menu((self.width, self.height), self.escape_menu.sfx_state,
                              "Dommage ! Tu as perdu !", (self.width/2.8, self.height/2.5))
        return menu.draw(self)

    def win(self) -> bool:
        """Méthode créant le menu de fin de partie et ajoutant la médaille associée
        à la difficulté de la partie gagnée, la méthode renvoie un booléen décidant
        si la partie se relance ou si le joueur revient au menu principal"""

        stop_music(self.map.music)

        with open(os.path.join("data", "medals.json"), "r") as medals_file:
            medals = json.load(medals_file)
            medals[self.nom_map][self.difficulty.replace(
                "_upgrades.json", "")] = True

        with open(os.path.join("data", "medals.json"), "w") as medals_file:
            json.dump(medals, medals_file, indent=4)

        menu = Game_over_menu((self.width, self.height), self.escape_menu.sfx_state,
                              "Félicitations ! Tu as gagné !", (self.width/2.95, self.height/2.5))
        return menu.draw(self)
