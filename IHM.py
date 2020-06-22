# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:37:06 2020

@author: Pierre-Marie EDLINGER
"""

from tkinter import *
import ProgCreationFichierCLS as Prog
import FonctionsFichier as FF

DERNIERELIGNE = 10

# définition des gestionnaires
# d'événements :

def choixFicDeTravail():
    varNomFicTravail.set(FF.getFichier())
    """
    tF = eval(champTC.get())
    varTF.set(str(tF*1.8 +32))
    """
    
def choixRepFinal():
    varNomRep.set(FF.getRepertoire())
    
def fermeTout():
    global fenPrincipale
    fenPrincipale.quit()

def creerFichierModele():
    try :
        cheminFic = ""
        cheminFic = FF.getOuEnregistrerFichier()
        if cheminFic != "":
            Prog.CreerFichierTravail(cheminFic)
            FF.messageInfo("Succès", "L'opération s'est déroulée avec succès.")
    except :
        FF.messageWarning("Erreur", "Une erreur est survenue lors de la création du fichier modèle...")

def creerFichiersCLS():
    try:
        if (varNomFicTravail.get() == ""):
            FF.messageWarning("Renseignements manquants", "Choisissez le fichier source.")
            choixFicDeTravail()
        else :
            if FF.verifieExistanceFichier(varNomFicTravail.get()):
                if (varNomRep.get() == ""):
                    FF.messageWarning("Renseignements manquants", "Choisissez un répertoire où placer le(s) fichier(s) à importer dans IBM Lotus.")
                    choixRepFinal()
                else:
                    if FF.verifieExistanceRepertoire(varNomRep.get()):
                        Prog.LanceCreationFichierCLS(varNomFicTravail.get(), varNomRep.get())
                        #FF.messageInfo("Succès", "L'opération s'est déroulée avec succès.")
                    else:
                        choixRepFinal()
            else:
                choixFicDeTravail()
    except :
        FF.messageWarning("Erreur", "Une erreur est survenue lors de la création du ou des fichier(s) à importer...")

# def pointeur(event):
#     print( "Clic détecté en X =" + str(event.x) +\
#                             ", Y =" + str(event.y))
        
#========== Programme principal =============

# Création du widget principal ("parent") :
fenPrincipale = Tk()
fenPrincipale.title("Création du fichier d'importation dans IBM Lotus")
fenPrincipale.geometry("650x130")
# fenPrincipale.bind("<Button-1>", pointeur) # Button-1 --> clic gauche; Button-2 --> clic molette; Button-3 --> clic droit
fenPrincipale.resizable(False, False)
try:
    fenPrincipale.iconbitmap('icone.ico')
except : None
"""
#Pour changer l'icone'
fenPrincipale.iconbitmap("questhead")
"""
GAUCHE = 10
LARGEURBOUTONS = 25

# création des widgets "enfants" :
# can1 = Canvas(fen1,bg='dark grey',height=250, width=250)
# can1.pack(side=LEFT, padx =5, pady =5)
#chaine.configure(text = "test") # pour changer le texte d'un label

# ---- Gestion de la zone "où enregistrer les fichiers"
# ---- Label
lblRep1 = Label(fenPrincipale, text = 'Choix du répertoire où enregistrer les fichiers de travail :')
lblRep1.place(x=GAUCHE, y = 10)

# ---- zone de texte 
varNomRep = StringVar()
entr2 = Entry(fenPrincipale, textvariable = varNomRep, width =100)
varNomRep.set("")
entr2.place(x=GAUCHE, y= 30)

# ---- Bouton ------------------
btnChoixRep = Button(fenPrincipale, text='...', width =2, command=choixRepFinal)
btnChoixRep.place(x=620, y= 30)
#*********************************************************

# ---- Gestion de la zone "fichier de travail"
# ---- Label
lblFic2 = Label(fenPrincipale, text = 'Choix du fichier de travail :')
lblFic2.place(x=GAUCHE, y=50)

# ---- zone de texte
varNomFicTravail = StringVar()
entr1 = Entry(fenPrincipale, textvariable = varNomFicTravail, width =100) #    varTC.set("")
varNomFicTravail.set("")
entr1.place(x=GAUCHE, y= 70)

# ---- Bouton ------------------
btnFicTravail = Button(fenPrincipale, text='...', width =2, command=choixFicDeTravail)
btnFicTravail.place(x=620, y= 70)
#*********************************************************

btnCreerFicTravail = Button(fenPrincipale, text='Créer un modèle', width =LARGEURBOUTONS, command=creerFichierModele)
btnCreerFicTravail.place(x=GAUCHE, y= 100)

btnCreerFichierCLS = Button(fenPrincipale, 
                            text='Créer le(s) fichier(s) à importer', 
                            width =LARGEURBOUTONS, 
                            command=creerFichiersCLS)
btnCreerFichierCLS.place(x=200, y= 100)

btnQuit = Button(fenPrincipale,text='Quitter', width =LARGEURBOUTONS, command=fermeTout)
btnQuit.place(x=400, y= 100)

# démarrage du réceptionnaire d'évènements (boucle principale) :
fenPrincipale.mainloop()

try:
    fenPrincipale.destroy()
except:
    None
