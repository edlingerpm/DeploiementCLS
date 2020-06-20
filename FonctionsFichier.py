# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 2020

@author: Pierre-Marie EDLINGER
"""
import os
import tkinter
from tkinter import messagebox

#création d'un répertoire + nommage du fichier final
def creationRepertoire(nomCompletRepertoire):
    try:
        # Bloc à essayer - création du répertoire
        os.mkdir(nomCompletRepertoire)
    except:
        # Bloc qui sera exécuté en cas d'erreur
        print("Erreur lors de la création du répertoire.")
        None

def ecritTexteDansFichier(fichier, texte):        
    fichier.write ( texte + "\n" )    # écriture de la chaîne de caractères

    
    
def poseQuestion(titre, question):
    top = tkinter.Tk()

    result=messagebox.askyesno(titre, question, icon='question', parent=top)
    if result:
        top.destroy()
    else:
        top.destroy()
    
    top.mainloop()
    return result

def getRensDansFichier(nomFichier):
    matrice = []                            # création d'une liste vide,
    with open (nomFichier, "r") as fichier:  # ouverture du fichier en mode lecture
        for ligne in fichier :                   # pour toutes les lignes du fichier
            s = ligne.strip ("\n\r")       # on enlève les caractères de fin de ligne
            l = s.split (";")           # on découpe en colonnes
            matrice.append (l)             # on ajoute la ligne à la matrice
    return matrice
    
