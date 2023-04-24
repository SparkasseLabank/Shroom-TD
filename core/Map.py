import pygame
import os
import json


class Map:
    def __init__(self, nom_map: str, screen_size: tuple) -> None:
        """Classe représentant la map
        - nom_map: chaine de caractères correspondant au nom de la map choisie
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre"""

        self.width = screen_size[0]
        self.height = screen_size[1]
        self.unit = (self.height - (self.height//10)) // 8
        self.unitL = self.width / 14
        self.nom_map = nom_map

        with open("data/Maps.json", "r") as maps_file:
            self.maps = json.load(maps_file)

        self.convert_json_maps()
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join(
            "assets", "maps", self.maps[nom_map]["asset"])).convert(), (self.width, self.height*0.9))
        self.start = self.maps[nom_map]["start"]
        self.path = self.maps[nom_map]["path"]
        self.tower_places = self.maps[nom_map]["tower_placement"]
        self.water_places = self.maps[nom_map]["water_placement"]
        try:
            self.music = pygame.mixer.Sound(os.path.join(
                "assets", "sounds", "musics", self.maps[nom_map]["music"]))
        except pygame.error:
            self.music = None

    def convert_json_maps(self) -> None:
        """Méthode pour convertir le fichier Maps.json et d'assigner toutes ses données dans les attributs de la classe"""

        for map_name, mapdata in self.maps.items():
            for data_name, data_value in mapdata.items():
                if data_name == "start":
                    self.maps[map_name]["start"] = (
                        data_value[0]*self.unitL, data_value[1]*self.unit)
                if data_name == "path":
                    for coord in data_value:
                        if self.nom_map == "meadow":
                            self.maps[map_name]["path"][self.maps[map_name]["path"].index(
                                coord)] = (coord[0]*self.unitL, coord[1]*self.unit)
                        else:
                            self.maps[map_name]["path"][self.maps[map_name]["path"].index(coord)] = (
                                coord[0]*self.unitL + (self.unitL*0.15), coord[1]*self.unit)
                if data_name == "tower_placement":
                    if data_value != [[]]:
                        for coord in data_value:
                            if self.nom_map == "meadow":
                                self.maps[map_name]["tower_placement"][self.maps[map_name]["tower_placement"].index(
                                    coord)] = (coord[0]*self.unitL, coord[1]*self.unit)
                            else:
                                self.maps[map_name]["tower_placement"][self.maps[map_name]["tower_placement"].index(
                                    coord)] = (coord[0]*self.unitL + (self.unitL*0.15), coord[1]*self.unit)
                if data_name == "water_placement":
                    if data_value != [[]]:
                        for coord in data_value:
                            if self.nom_map == "meadow":
                                self.maps[map_name]["water_placement"][self.maps[map_name]["water_placement"].index(
                                    coord)] = (coord[0]*self.unitL, coord[1]*self.unit)
                            else:
                                self.maps[map_name]["water_placement"][self.maps[map_name]["water_placement"].index(
                                    coord)] = (coord[0]*self.unitL + (self.unitL*0.15), coord[1]*self.unit)

    def reset_placements(self) -> None:
        """Méthode pour réinitialiser tous les emplacements de la map (Terre et Eau)"""

        with open("data/Maps.json", "r") as maps_file:
            self.maps = json.load(maps_file)
        self.convert_json_maps()
        self.tower_places = self.maps[self.nom_map]["tower_placement"]
        self.water_places = self.maps[self.nom_map]["water_placement"]
