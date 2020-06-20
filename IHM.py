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
    Prog.CreerFichierTravail(FF.getOuEnregistrerFichier())

def creerFichiersCLS():
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
                else:
                    choixRepFinal()
        else:
            choixFicDeTravail()
    
#========== Programme principal =============

# Création du widget principal ("parent") :
fenPrincipale = Tk()
fenPrincipale.title("Création du fichier d'importation dans IBM Lotus")

"""
#Pour changer l'icone'
fenPrincipale.iconbitmap("questhead")
"""

# création des widgets "enfants" :
# can1 = Canvas(fen1,bg='dark grey',height=250, width=250)
# can1.pack(side=LEFT, padx =5, pady =5)

chaine2 = Label(fenPrincipale, text = 'Choix du répertoire où enregistrer les fichiers de travail :')
chaine2.grid(row =0, column =0, sticky = W)

chaine = Label(fenPrincipale, text = 'Choix du fichier de travail :')
chaine.grid(row =2, column =0, sticky = W)
#chaine.configure(text = "test")

# ---- Gestion de la zone de texte qui récupère le nom du répertoire où enregistrer les fichiers
varNomRep = StringVar()
entr2 = Entry(fenPrincipale, textvariable = varNomRep, width =100)
varNomRep.set("")
entr2.grid(row =1, column =0)

# ---- Gestion de la zone de texte qui récupère le nom de fichier
varNomFicTravail = StringVar()
entr1 = Entry(fenPrincipale, textvariable = varNomFicTravail, width =100) #    varTC.set("")
varNomFicTravail.set("")
entr1.grid(row =3, column =0)


# ---- Gestion des boutons ------------------
btnChoixRep = Button(fenPrincipale, text='...', width =0, command=choixRepFinal)
btnChoixRep.grid(row =1, column =1, sticky = W)
btnChoixRep.width = 0

btnFicTravail = Button(fenPrincipale, text='...', width =0, command=choixFicDeTravail)
btnFicTravail.grid(row =3, column =1, sticky = W)

btnCreerFicTravail = Button(fenPrincipale, text='Créer un modèle', width =0, command=creerFichierModele)
btnCreerFicTravail.grid(row =DERNIERELIGNE, column =0, sticky =W)

btnCreerFichierCLS = Button(fenPrincipale, 
                            text='Créer le(s) fichier(s) à importer', 
                            width =0, 
                            command=creerFichiersCLS)
btnCreerFichierCLS.grid(row =DERNIERELIGNE, column =1, sticky = E)

btnQuit = Button(fenPrincipale,text='Quitter', width =10, command=fermeTout)
btnQuit.grid(row =DERNIERELIGNE, column =3, sticky =E)

# démarrage du réceptionnaire d'évènements (boucle principale) :
fenPrincipale.mainloop()

try:
    fenPrincipale.destroy()
except:
    None
