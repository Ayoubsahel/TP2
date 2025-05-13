# utils.py

import csv
import json

def lire_csv(chemin):
    """
    Lire un fichier CSV et retourner la liste des lignes.
    Chaque dictionnaire correspond à une ligne du fichier.
    """
    liste = []
    with open(chemin, "r", newline=" ", encoding="utf-8") as f:
        ligne = csv.reader(f)
        for i in ligne:
            j = {i[0]: i[1]}
            liste.append(j)
    return liste

def sauvegarder_json(data, chemin):
    """
    Sauvegarder des données dans un fichier JSON.
    - data : un objet Python (par exemple, un dictionnaire ou une liste)
    - chemin : chemin du fichier JSON à écrire
    Utiliser json.dump avec indentation pour que le fichier soit lisible.
    """
    with open(chemin, "w") as f:
        json.dump(data)


def ecrire_texte(contenu, chemin):
    """
    Écrire du texte brut dans un fichier texte (.txt).
    - contenu : texte à écrire
    - chemin : chemin du fichier texte à créer
    """
    with open(chemin,"a") as f:
        f.write(contenu)
    
