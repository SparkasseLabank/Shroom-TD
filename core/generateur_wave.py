import json


def wave(current_wave: int) -> list:
    """Fonction permettant de convertir le fichier json et revoie
    la liste des ennemis de la vague
    - current_wave: entier correspondant au numéro de la vague"""

    with open("data/waves.json", "r") as enemy_file:
        vague = json.load(enemy_file)
    list_enemy = []
    for i in range(len(vague[str(current_wave)])):
        for y in range(int(vague[str(current_wave)][i][2])):
            list_enemy.append(vague[str(current_wave)][i][:2])

    return (list_enemy)
