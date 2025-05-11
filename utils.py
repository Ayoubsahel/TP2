# utils.py

import csv
import json

def lire_csv(chemin):
    """
    Lire un fichier CSV et retourner la liste des lignes.
    Chaque dictionnaire correspond à une ligne du fichier.
    """
    with open(chemin, "r") as f:
        ligne = f.readlines()
    return ligne

def sauvegarder_json(data, chemin):
    """
    Sauvegarder des données dans un fichier JSON.
    - data : un objet Python (par exemple, un dictionnaire ou une liste)
    - chemin : chemin du fichier JSON à écrire
    Utiliser json.dump avec indentation pour que le fichier soit lisible.
    """
    pass

def ecrire_texte(contenu, chemin):
    """
    Écrire du texte brut dans un fichier texte (.txt).
    - contenu : texte à écrire
    - chemin : chemin du fichier texte à créer
    """
    with open(chemin,"a") as f:
        f.write(contenu)
    
