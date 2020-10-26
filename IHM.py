# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:37:06 2020

@author: Pierre-Marie EDLINGER
"""

from tkinter import *
from tkinter.ttk import *

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
   
def choixFicCaisse():
    varNomFicCaisses.set(FF.getFichier())
    
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
        FF.messageWarning("Erreur", "Une erreur est survenue lors de la création du ou des fichier(s) à importer.... Vérifiez qu'il n'y ait pas un Alt+Tab dans un des fichiers.")

def creerFichierSupprimeCaisse():
    try:
        if (varNomFicTravail.get() == ""):
            FF.messageWarning("Renseignements manquants", "Choisissez le fichier de travail.")
            choixFicDeTravail()
        else :
            if FF.verifieExistanceFichier(varNomFicTravail.get()):
                if (varNomRep.get() == ""):
                    FF.messageWarning("Renseignements manquants", "Choisissez un répertoire où placer le(s) fichier(s) à importer dans IBM Lotus.")
                    choixRepFinal()
                else:
                    if FF.verifieExistanceRepertoire(varNomRep.get()):
                        
                        if (varNomFicCaisses.get() == ""):
                            FF.messageWarning("Renseignements manquants", "Choisissez le fichier des caisses à rendre inactives.")
                            choixFicCaisse()
                        else :
                            if FF.verifieExistanceFichier(varNomFicCaisses.get()):
                                Prog.LanceCreationFichierSupprimeCaisses(varNomFicCaisses.get(), varNomFicTravail.get(), varNomRep.get())
                            else:
                                choixFicCaisse()
                    else:
                        choixRepFinal()
            else:
                choixFicDeTravail()
    except :
        FF.messageWarning("Erreur", "Une erreur est survenue lors de la création du fichier pour rendre des caisses inactives... Vérifiez qu'il n'y ait pas un Alt+Tab dans un des fichiers.")


def afficheInfos():
    global fenPrincipale
    texte = "Penser à ouvrir le(s) fichier(s) résultat(s) avec OpenOffice puis enregistrez les au format '.ods' avant de les importer.\nLe code source de cette application est disponible sur: https://github.com/edlingerpm/DeploiementCLS\n(copié dans le presse papier)."
    try :
        fenPrincipale.clipboard_clear()
        fenPrincipale.clipboard_append("https://github.com/edlingerpm/DeploiementCLS")
        FF.messageInfo("Information importante", texte)
    except :
        print("Erreur!!!!")
        None

def testModif():
    global tableau
    
    if FF.verifieExistanceFichier(varNomFicTravail.get()):
        # try :
        maMatrice = FF.getRensDansFichierExportComplet(varNomFicTravail.get())
        # print(len(maMatrice))
        for i in range(0, len(maMatrice)) :
            # print(maMatrice[i][0])
            tableau.insert('', 'end', iid=maMatrice[i][0], values=(maMatrice[i][1], maMatrice[i][2], maMatrice[i][3]))
            tableau.update
        # except :
        #     print("Erreur testModif!!!!")
        #     None
    else:
        choixFicDeTravail()

# def pointeur(event):
#     print( "Clic détecté en X =" + str(event.x) +\
#                             ", Y =" + str(event.y))
        
#========== Programme principal =============

# Création du widget principal ("parent") :
fenPrincipale = Tk()
fenPrincipale.title("Création du fichier d'importation dans IBM Lotus")
fenPrincipale.geometry("650x130")

# fenPrincipale.geometry("650x200")

# fenPrincipale.bind("<Button-1>", pointeur) # Button-1 --> clic gauche; Button-2 --> clic molette; Button-3 --> clic droit
# fenPrincipale.resizable(False, False)

try: #sert à éviter un message d'erreur si le fichier icone n'existe pas
    fenPrincipale.iconbitmap('icone.ico')
except : None

GAUCHE = 10
LARGEURBOUTONS = 15
LIGNEDUBAS = 100

# création des widgets "enfants" :
# can1 = Canvas(fen1,bg='dark grey',height=250, width=250)
# can1.pack(side=LEFT, padx =5, pady =5)
#chaine.configure(text = "test") # pour changer le texte d'un label

# ---- Gestion de la zone "où enregistrer les fichiers"
# ---- Label
lblRep1 = Label(fenPrincipale, text = 'Choix du répertoire où enregistrer les fichiers de travail :')
lblRep1.place(x=GAUCHE, y = 5)

# ---- zone de texte 
varNomRep = StringVar()
entr2 = Entry(fenPrincipale, textvariable = varNomRep, width =100)
varNomRep.set("")
entr2.place(x=GAUCHE, y= 25)

# ---- Bouton ------------------
btnChoixRep = Button(fenPrincipale, text='...', width =2, command=choixRepFinal)
btnChoixRep.place(x=620, y= 23)
#*********************************************************

# ---- Gestion de la zone "fichier de travail"
# ---- Label
lblFic2 = Label(fenPrincipale, text = 'Choix du fichier de travail :')
lblFic2.place(x=GAUCHE, y=50)

# ---- zone de texte
varNomFicTravail = StringVar()
entr1 = Entry(fenPrincipale, textvariable = varNomFicTravail, width =45) #    varTC.set("")
varNomFicTravail.set("")
entr1.place(x=GAUCHE, y= 70)

# ---- Bouton ------------------
btnFicTravail = Button(fenPrincipale, text='...', width =2, command=choixFicDeTravail)
btnFicTravail.place(x=289, y= 68)
#*********************************************************

# ---- Gestion de la zone "fichier des caisses"
# ---- Label
lblFic3 = Label(fenPrincipale, text = 'Choix du fichier des caisses à rendre inactives :')
lblFic3.place(x=GAUCHE +330, y=50)

# ---- zone de texte
varNomFicCaisses = StringVar()
entr2 = Entry(fenPrincipale, textvariable = varNomFicCaisses, width =45) #    varTC.set("")
varNomFicCaisses.set("")
entr2.place(x=GAUCHE+330, y= 70)

# ---- Bouton ------------------
btnFicCaisse = Button(fenPrincipale, text='...', width =2, command=choixFicCaisse)
btnFicCaisse.place(x=620, y= 68)
#*********************************************************

btnCreerFicTravail = Button(fenPrincipale, text='Créer un modèle', width =LARGEURBOUTONS, command=creerFichierModele)
btnCreerFicTravail.place(x=GAUCHE, y= LIGNEDUBAS)

btnCreerFichierCLS = Button(fenPrincipale, 
                            text='Créer le(s) fichier(s) à importer', 
                            width =LARGEURBOUTONS + 15, 
                            command=creerFichiersCLS)
btnCreerFichierCLS.place(x=115, y= LIGNEDUBAS)

btnSupprimerCaisses = Button(fenPrincipale, 
                            text='Créer le fichier pour supprimer caisse(s)', 
                            width =LARGEURBOUTONS + 20, 
                            command=creerFichierSupprimeCaisse)
btnSupprimerCaisses.place(x=310, y= LIGNEDUBAS)

btnQuit = Button(fenPrincipale,text='Quitter', width =LARGEURBOUTONS -5, command=fermeTout)
btnQuit.place(x=535, y= LIGNEDUBAS)

btnInfo = Button(fenPrincipale,text='?', width =3, command=afficheInfos)
btnInfo.place(x=615, y= LIGNEDUBAS)


# btnModif = Button(fenPrincipale,text='Test', width =5, command=testModif)
# btnModif.place(x=GAUCHE, y= LIGNEDUBAS+30)


# lststrMaListe = ListStore(str, str)

# tableau = Treeview(fenPrincipale, columns=('nomfamille', 'prenom', 'da'))
# tableau.heading('nomfamille', text='Nom de famille')
# tableau.heading('prenom', text='Prénom')
# tableau.heading('da', text='DA')
# tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
# tableau.place(x=GAUCHE + 50, y= LIGNEDUBAS+30)
# tableau.insert('', 'end', iid="45", values=("1", "2", "3"))
# tableau.insert('', 'end', iid="48", values=("4", "5", "6"))
# tableau.set_property("editable", True)
# tableau.editable = True


# démarrage du réceptionnaire d'évènements (boucle principale) :
fenPrincipale.mainloop()

try:
    fenPrincipale.destroy()
except:
    None