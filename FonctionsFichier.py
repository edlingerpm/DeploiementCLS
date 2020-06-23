# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 2020

@author: Pierre-Marie EDLINGER
"""
import os
import os.path
import tkinter

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# Vérifie si un fichier existe ou non
def verifieExistanceFichier(Fic):
    if os.path.isfile(Fic):
        return True
    else:
        messageWarning("Fichier inconnu", "Le fichier "+Fic+" n'existe pas!")
        return False

# Vérifie si un répertoire existe ou non
def verifieExistanceRepertoire(Rep):
    if os.path.isdir(Rep):
        return True
    else:
        messageWarning("Répertoire inconnu", "Le répertoire "+Rep+" n'existe pas!")
        return False
    
#création d'un répertoire + nommage du fichier final
def creationRepertoire(nomCompletRepertoire):
    try:
        # Bloc à essayer - création du répertoire
        os.mkdir(nomCompletRepertoire)
    except:
        # Bloc qui sera exécuté en cas d'erreur
        print("Erreur lors de la création du répertoire.")
        messageWarning("Erreur", "Erreur lors de la création du répertoire "+nomCompletRepertoire+".")
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

def messageWarning(titre = "Titre", texte = "Avertissement"):
    top = tkinter.Tk()
    top.withdraw()
    messagebox.showwarning(titre, texte, icon='warning', parent=top)

def messageInfo(titre = "Titre", texte = "Information"):
    top = tkinter.Tk()
    top.withdraw()
    messagebox.showinfo(titre, texte, icon='info', parent=top)
"""

    showinfo()
    showwarning()
    showerror ()
    askquestion()
    askokcancel()
    askyesno ()
    askretrycancel ()

"""
    
def getRensDansFichier(nomFichier):
    matrice = []                            # création d'une liste vide,
    with open (nomFichier, "r") as fichier:  # ouverture du fichier en mode lecture
        for ligne in fichier :                   # pour toutes les lignes du fichier
            s = ligne.strip ("\n\r")       # on enlève les caractères de fin de ligne
            l = s.split (";")           # on découpe en colonnes
            matrice.append (l)             # on ajoute la ligne à la matrice
    return matrice
    

def getFichier(repInit = "./", 
               titre = "Choix d'un fichier", 
               typeExtensions = {("Fichiers ODS","*.ods"),("Fichiers CSV","*.csv"),("Tous","*.*")}):
    """ Fenêtre pour choisir un fichier
        ENTREE : - le répertoire initial où chercher ex: "D:/"
                 - le titre de la fenêtre ex : "Choix du fichier"
                 - les extensions des fichiers à rechercher ex: {("Fichier ODS","*.ods"),("Fichier CSV","*.csv"),("Tous","*.*")}
        SORTIE : chemin complet du fichier selectionné ou chaine vide si aucun n'est selectionné """
        
    fen = Tk()
    
    fen.withdraw()
    fen.filename =  filedialog.askopenfilename(initialdir = repInit,
                                               title = titre,
                                               filetypes = typeExtensions
                                               )
    fichierChoisi = fen.filename
    fen.destroy
    return fichierChoisi

def getRepertoire(repInit = "./", titre = "Choix d'un répertoire"):
    """ Fenêtre pour choisir un répertoire
        ENTREE : - le répertoire initial où chercher ex: "D:/"
                 - le titre de la fenêtre ex : "Choix du fichier"
        SORTIE : chemin complet du répertoire selectionné ou chaine vide si aucun n'est selectionné """
        
    fen = Tk()
    fen.withdraw()
    fen.filename =  filedialog.askdirectory(initialdir = repInit,
                                            title = "Choix du répertoire")
    repChoisi = fen.filename
    #fen.destroy
    fen.quit
    return repChoisi

def getOuEnregistrerFichier(repInit = "./", 
                            titre = "Enregistrer un fichier", 
                            typeExtensions = {("Fichiers ODS","*.ods"),("Fichiers CSV","*.csv"),("Tous","*.*")}):
    """ Fenêtre pour choisir où enregistrer un fichier et demande de confirmation s'il existe déjà
        ENTREE : - le répertoire initial où chercher ex: "D:/"
                 - le titre de la fenêtre ex : "Choix du fichier"
                 - les extensions à appliquer ex: {("Fichier ODS","*.ods"),("Fichier CSV","*.csv"),("Tous","*.*")}
        SORTIE : chemin complet du répertoire selectionné ou chaine vide si aucun n'est selectionné """
        
    fen = Tk()
    fen.withdraw()
    fen.filename =  filedialog.asksaveasfilename(initialdir = repInit,
                                                 title = titre,
                                                 filetypes = typeExtensions,
                                                 defaultextension=True)
    #,addextension = True
    repChoisi = fen.filename
    fen.destroy
    return repChoisi
