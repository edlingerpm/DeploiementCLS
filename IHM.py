# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:37:06 2020

@author: Pierre-Marie
"""

from tkinter import *
import ProgCreationFichierCLS as Prog
import FonctionsFichier as FF

# définition des gestionnaires
# d'événements :

def choixFicDeTravail():
    print(FF.getFichier())
    
def choixRepFinal():
    print(FF.getRepertoire())
    
    
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

btnQuit = Button(fenPrincipale,text='Quitter', width =10, command=fenPrincipale.destroy)
btnQuit.pack(side=BOTTOM)
btnFicTravail = Button(fenPrincipale, text='Choix du fichier de travail', width =80, command=choixFicDeTravail)
btnFicTravail.pack()
btnChoixRep = Button(fenPrincipale, text='Choix du répertoire où enregistrer le fichier', width =80, command=choixRepFinal)
btnChoixRep.pack()
# démarrage du réceptionnaire d'évènements (boucle principale) :
fenPrincipale.mainloop()