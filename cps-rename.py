#!/usr/bin/env python3

# Programme de nettoyage des noms des vidéos de C'est pas sorcier téléchargées
# sur la chaîne officielle : http://www.youtube.com/user/cestpassorcierftv.
#
# Les fichires sont de la forme :
#
#     C'est pas sorcier - LE TITRE de la Vidéo -I8e_8DT9.mp4
#
# Le but est d'obtenir :
#
#     le titre de la vidéo.mp4
#
# Il peut ou non y avoir des espaces autour des tirets et la casse n'est pas
# garantie. L'extension peut varier. Dans certains cas, le bout de chaîne qui
# doit représenter un id contient un trait d'union et le nouveau fichier aura
# donc un mauvais nom. On signale donc à l'utilisateur qu'un nom de fichier
# contenant encore un trait d'union après le renommage est à vérifier, et
# éventuellement à corriger manuellement (ce qui devrait être rare).
#
# ------------------------------------------------------------------------------
#               LICENCE PUBLIQUE RIEN À BRANLER
#                     Version 1, Mars 2009
#
# Copyright (C) 2014 - 2015 Thomas Duchesne
#
# La copie et la distribution de copies exactes de cette licence sont
# autorisées, et toute modification est permise à condition de changer
# le nom de la licence. 
# 
#         CONDITIONS DE COPIE, DISTRIBUTON ET MODIFICATION
#               DE LA LICENCE PUBLIQUE RIEN À BRANLER
#
#  0. Faites ce que vous voulez, j’en ai RIEN À BRANLER.
# ------------------------------------------------------------------------------

import sys
import os

nombre_de_fichiers_a_renommer = 0
nombre_de_fichiers_a_verifier = 0

def renommage(dossier=".", fichiers_exclus=[]):
    global nombre_de_fichiers_a_verifier
    global nombre_de_fichiers_a_renommer

    fichiers_a_renommer = [fichier for fichier in os.listdir("./" + dossier) if fichier not in fichiers_exclus]

    nombre_de_fichiers_a_renommer = len(fichiers_a_renommer)

    for fichier in fichiers_a_renommer:
        # La partie intéressante est entre le tout premier tiret et le tout
        # dernier. On liste la position des tirets dans le nom du fichier pour
        # découper plus facilement celui-ci.
        tirets = []
        for position, caractere in enumerate(fichier):
            if caractere == "-":
                tirets.append(position)

        try:
            extension = os.path.splitext(os.path.basename(fichier))[1]

            # On ne garde que les caractères entre les deux tirets extrêmes et
            # on ajoute l'extension.
            nouveau_fichier = fichier[tirets[0] + 1:tirets[-1]].strip() + extension

            # On supprime les espaces multiples.
            nouveau_fichier = " ".join(nouveau_fichier.split())

            nouveau_fichier = nouveau_fichier.lower()

            try:
                os.rename("./" + dossier + "/" + fichier, "./" + dossier + "/" + nouveau_fichier)

                # S'il reste des tirets dans le nom, c'est peut-être le signe
                # qu'il y a un tiret dans l'espèce d'id aléatoire en fin de nom
                # de fichier.
                if "-" in nouveau_fichier:
                    print(nouveau_fichier + " comporte encore des tirets.")
                    nombre_de_fichiers_a_verifier += 1

            except PermissionError:
                print("Erreur : vous n'avez pas la permission de rennomer " + fichier)
            except FileNotFoundError:
                print("Erreur : " + fichier + " n'existe pas.")

        except IndexError:
            print("Erreur : " + fichier + " ne peut pas être renommé.")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        try:
            renommage(sys.argv[1], sys.argv[2:])
            print("--------------------------------")
            print("Fichiers renommés : " + str(nombre_de_fichiers_a_renommer))
            print("Fichiers à vérifier : " + str(nombre_de_fichiers_a_verifier) + " (" + str(int((nombre_de_fichiers_a_verifier / nombre_de_fichiers_a_renommer) * 100)) + " %)")
        except NotADirectoryError:
            print("Erreur : " + sys.argv[1] + " n'est pas un dossier.")
    else:
        print("Utilisation : " + os.path.basename(__file__) + " dossier fichier_exclus_1 fichier_exclus_2 ...")
