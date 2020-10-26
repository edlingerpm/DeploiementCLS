# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:31:58 2020

@author: Pierre-Marie EDLINGER
"""
import FonctionsFichier as FF
import LigneParMateriel as LM

# Initialisation des variables globales
NOMFICHIERRESULTAT = "Resultat"
EXTENSIONFICHIER = ".csv"
fichierResultat = None
XXX = "" 
xIP = ""
xVille = ""
xSite = ""
xContact = ""
xRD = ""
xRA = ""
xDate = ""
NBCLS = ""
NBMONNAYEUR = ""
NBIMPRSTICKERS = ""
debutNouveauFichier = True

def CreerFichierTravail(Fichier): 
    fichiertravail = open (Fichier, "w")    # Création et ouverture du fichier à remplir
    
    #écriture de la 1ère ligne des noms de colonne au format attendu dans le programme
    FF.ecritTexteDansFichier(fichiertravail, LM.getTexteFichierTravail())
    fichiertravail.close ()  # fermeture du fichier
    
def enteteColonnesFichierIP(fichier):
    """ Insère la première ligne du fichier des adresses IP
        ENTREE : rien
        SORTIE : rien
        >>> à adapter au format du fichier attendu par l'imprimante d'étiquettes """

    #écriture de la 1ère ligne des noms de colonne au format attendu par l'imprimante d'étiquettes
    FF.ecritTexteDansFichier(fichier, "Magasin;;Num matériel;;Adresse IP")
                             
    
def enteteColonnes(fichier):
    """ Insère la première ligne du fichier résultat
        ENTREE : rien
        SORTIE : rien
        >>> à adapter au format du fichier attendu dans IBM Lotus """

    #écriture de la 1ère ligne des noms de colonne au format attendu dans Lotus
    FF.ecritTexteDansFichier(fichier, "id du document;Nom du matériel;Description;"
                             + "Etat de la fiche;lien vers la photo;"
                             + "Statut de la fiche;Nom du matériel de backup;"
                             + "Pays impacté;Composant matériel;Marque;Modèle;"
                             + "Type de matériel;Numéro de série;Technologie;"
                             + "Pays d'hébergement;Ville;Site;Nom du site;"
                             + "Localisation;Emplacement;Contact sur le site;"
                             + "Affecté à;Composant hébergé;Criticité;RD;RA;"
                             + "Société propriétaire;Pays propriétaire;"
                             + "Date d'entrée;Date de mise à jour;Date de fin;"
                             + "Type de contrat d'assistance;Nom prestataire;"
                             + "Numéro de contrat;Date de début du contrat;"
                             + "Date de fin du contrat;Réseau : ip;Sous-réseau;"
                             + "passerelle;Adresse Mac;Supervision;Accessibilité;"
                             + "Fournisseur;Numéro de commande;Coût de l'achat;"
                             + "Numéro de la facture;Valeur;Bon de livraison;"
                             + "Date de la commande;Date de livraison;"
                             + "Type escalade N2;Escalade N2;Escalade N3;"
                             + "Attribut 1;Attribut 2;Attribut 3;Attribut 4;"
                             + "Attribut 5;Attribut 6;Attribut 7;Attribut 8;"
                             + "Attribut 9;Attribut 10;Attribut 11;Attribut 12;"
                             + "Attribut 13;Attribut 14;Attribut 15;Attribut 16;"
                             + "Attribut 17;Attribut 18;Attribut 19;Attribut 20;"
                             + "Attribut 21;Attribut 22;Attribut 23;Attribut 24;"
                             + "Attribut 25;Attribut 26;Attribut 27;Attribut 28;"
                             + "Attribut 29;Attribut 30")


### Début programme **********************************************************
def LanceCreationFichierSupprimeCaisses(fichierCaisses, fichierTravail, RepResultat): 
    cpt = 0
    cpt2 = 0
    cpt3 = 0
    # on remplit une matrice avec toutes les noms des matériels à rechercher 
    # du fichier caisses à rendre inactives
    matrice = FF.getRensDansFichierCaisses(fichierCaisses)

    listeNomsMateriels = matrice[0]
    listeMagasins = matrice[1]
    dateARetenir = listeNomsMateriels[0]
    
    # print(listeMagasins)
    del listeNomsMateriels[0]
    # print(listeNomsMateriels)
    # print("ICI20")
    # création et ouverture du fichier des caisses à supprimer
    fichierCaissesARendreInactives = open (RepResultat+"/FichiersCaissesARendreInactives.csv", "w")    # Création et ouverture du fichier rempli "+ listeNomsMateriels[0] +"
    # on rempli l'entête des colonnes
    enteteColonnes(fichierCaissesARendreInactives)
    # print("ICI21")
    # ouverture fichier à trier
    with open (fichierTravail, "r") as fichier:  # ouverture du fichier en mode lecture
        for ligne in fichier :                   # pour toutes les lignes du fichier
            s = ligne.strip ("\n\r")       # on enlève les caractères de fin de ligne
            l = s.split (";")           # on découpe en colonnes
            # print(len(l))
            # remplissage des lignes concernant les caisses à supprimer
            if l[1].lower() in listeNomsMateriels: # si le nom du matériel est dans notre liste
                FF.ecritTexteDansFichier(fichierCaissesARendreInactives, transformeLigne(l, dateARetenir)) # on ajoute la ligne dans le fichier final
                cpt = cpt +1 # on incrémente le compteur
            # print("ICI3")    
            # remplissage des lignes des caisses dont il faut changer les scanners
            # s'il s'agit d'un scanner
            
            # ça ça sert à faire un test pour trouver où il y a une erreur dans le fichier souvent un Alt+Tab 
            # print(l[0])
            # cpt3 = cpt3 +1
            # print(cpt3)
                
            if l[16] in listeMagasins: # si le magasin est dans notre liste de magasins
                # on vérifie qu'il s'agit bien d'un scanner 11 caractères
                # print(l[1][0:10].lower())
                if l[1][0:11].lower() == "scannercais":
                    # cpt2 = cpt2 +1 # on incrémente le compteur
                    #  il ne faut pas que ce soit une caisse qu'on supprime
                    if l[1].lower() not in listeNomsMateriels:
                        FF.ecritTexteDansFichier(fichierCaissesARendreInactives, transformeLignesScanner(l, dateARetenir)) # on ajoute la ligne dans le fichier final
                        cpt2 = cpt2 +1 # on incrémente le compteur
                        
            ######################################################          
            # on prend les scanners des CLS mais normalement il n'y en a pas
            # et s'il y en a, cela ne fera aucune modif pour eux
            ###################################################### 
                # None
            # print("ICI4")
    fichierCaissesARendreInactives.close ()  # fermeture du fichier
            
    FF.messageInfo("Succès", "L'opération s'est déroulée avec succès. "+ str(cpt)
                   + " lignes insérées pour suppression de caisse et "+ str(cpt2)
                   +" lignes pour changement de scanner.")       

def transformeLigne(liste, date):
    nouveauTexte = ""
    for i in range(len(liste)):
        if i == 3 :
            nouveauTexte = nouveauTexte + "Inactif (hors parc);"
        else :
            if i == 29 :
                nouveauTexte = nouveauTexte + date +";"
            else :
                nouveauTexte = nouveauTexte + liste[i]+";"
    
    return nouveauTexte[0:len(nouveauTexte)-1]

def transformeLignesScanner(liste, date):
    nouveauTexte = ""
    for i in range(len(liste)):
        if i == 9 :
            if liste[9] == "Datalogic" and liste[10] == "VS 2200":
                nouveauTexte = nouveauTexte + "Datalogic;3200 VSI;"
            else:
                if liste[9] == "Datalogic" and (liste[10] == "8400 Magellan PSC" or liste[10] == "8201 Magellan PSC"):
                    nouveauTexte = nouveauTexte + "Magellan;Bi-optique 9800i (9801);"
                else :
                    nouveauTexte = nouveauTexte + liste[i]+";"+liste[i+1]+";"
        else :
            if i == 29 :
                nouveauTexte = nouveauTexte + date +";"
            else :
                if i == 10 : 
                    None
                else :
                    nouveauTexte = nouveauTexte + liste[i]+";"
    
    return nouveauTexte[0:len(nouveauTexte)-1]
    
def LanceCreationFichierCLS(fichierTravail, RepResultat):
    global debutNouveauFichier
    numFichier = 1
    texteNumFichier = ""
    # on remplit une matrice avec toutes les lignes du fichier de travail
    maMatrice = FF.getRensDansFichier(fichierTravail)
    
    # Création du fichier des adresses IP
    fichierIP = open (RepResultat+"/ListeIPPourEtiquettes.csv", "w")    # Création et ouverture du fichier rempli
    enteteColonnesFichierIP(fichierIP)        
    
    # pour toutes les lignes de la matrice
    for ligneFichier in range (1, len(maMatrice)):
        
        # s'il ne s'agit pas d'une ligne vide
        if maMatrice[ligneFichier][0] != "" :
                       
            #si on est au début d'un nouveau fichier
            if debutNouveauFichier == True :
                # on indique que l'on ne sera plus à la création d'un nouveau fichier
                debutNouveauFichier = False
                # on crée et ouvre un nouveau fichier qui portera
                #le numéro du 1er magasin à traiter
                
                # traitement du numéro de fichier
                # si < 10 alors on rajoute 0
                if numFichier < 10:
                    texteNumFichier = "0"+ str(numFichier) + " - "
                else:
                    texteNumFichier = str(numFichier)+ " - "
                    
                # Création et ouverture du fichier rempli
                fichierResultat = open (RepResultat+"/"+texteNumFichier+NOMFICHIERRESULTAT+maMatrice[ligneFichier][0]+EXTENSIONFICHIER, "w")
                
                # incrémentation du numéro de fichier
                numFichier = numFichier + 1
                
                # on rempli l'entête des colonnes
                enteteColonnes(fichierResultat)
            # else:
            #     #on rajoute au fichier
            #     fichierResultat = open (RepResultat+NOMFICHIERRESULTAT+maMatrice[ligneFichier][0]+EXTENSIONFICHIER, "a")
            
            #On initialise tous les paramètres
            XXX = maMatrice[ligneFichier][0] 
            xIP = FF.getIP(maMatrice[ligneFichier][1])
            xVille = maMatrice[ligneFichier][2]
            xSite = maMatrice[ligneFichier][3]
            xContact = maMatrice[ligneFichier][4] 
            xRD = maMatrice[ligneFichier][5]
            xRA = maMatrice[ligneFichier][6]
            xDate = maMatrice[ligneFichier][7]
            NBCLS = maMatrice[ligneFichier][8]
            NBMONNAYEUR = maMatrice[ligneFichier][9]
            NBIMPRSTICKERS = maMatrice[ligneFichier][10]
            
            # on s'occupe ici de chaque CLS et de tous leurs matériels
            for i in range(int(NBCLS)) :
                numero = 21+i # le numéro des CLS commence toujours par 21
                
                #UC dans CLS
                FF.ecritTexteDansFichier(fichierResultat, 
                                         LM.getCLS(XXX, str(numero), xIP, xVille, xSite, 
                                                   xContact, xRD, xRA, xDate))
                # IP des UC CLS
                FF.ecritTexteDansFichier(fichierIP, 
                                         LM.getIP(XXX, str(numero), xIP, True))
                
                #Scanners
                FF.ecritTexteDansFichier(fichierResultat, 
                                         LM.getScanner(XXX, str(numero), xVille, xSite, 
                                                       xContact, xRD, xRA, xDate))
                #Imprimantes M30
                FF.ecritTexteDansFichier(fichierResultat, 
                                         LM.getImprimanteM30(XXX, str(numero), xVille, 
                                                            xSite, xContact, xRD, 
                                                            xRA, xDate))
            
                #Mâts
                FF.ecritTexteDansFichier(fichierResultat, 
                                         LM.getMat(XXX, str(numero), xVille, xSite, 
                                                   xContact, xRD, xRA, xDate))
                
                #Balances
                FF.ecritTexteDansFichier(fichierResultat, 
                                         LM.getBalance(XXX, str(numero), xVille, xSite, 
                                                   xContact, xRD, xRA, xDate))
                                 
                #Ecrans
                FF.ecritTexteDansFichier(fichierResultat, 
                                         LM.getEcran(XXX, str(numero), xVille, xSite, 
                                                   xContact, xRD, xRA, xDate))
            
            #Monnayeurs
            numCLS = 21 # sert à déterminer entre quelles CLS sont placés les monnayeurs
            for i in range(int(NBMONNAYEUR)) :
                numero = 45+i
                numCLS1 = numCLS
                numCLS2 = numCLS1 + 1
                FF.ecritTexteDansFichier(fichierResultat, 
                                         LM.getMonnayeur(XXX, str(numero), 
                                                         str(numCLS1), str(numCLS2), 
                                                         xIP, xVille, xSite, 
                                                         xContact, xRD, xRA, xDate))
                # IP des monnayeurs
                FF.ecritTexteDansFichier(fichierIP, 
                                         LM.getIP(XXX, str(numero), xIP, False))
                
                numCLS = numCLS2 + 1
            
            #Imprimantes pour les stickers
            for i in range(int(NBIMPRSTICKERS)) :
                numero = 1+i
                FF.ecritTexteDansFichier(fichierResultat, 
                                         LM.getImprimanteStickers(XXX, str(numero), 
                                                                  xVille, xSite, 
                                                                  xContact, xRD, 
                                                                  xRA, xDate))
            # 1 portillon par magasin
            FF.ecritTexteDansFichier(fichierResultat, 
                                         LM.getPortillon(XXX, xIP, xVille, xSite, xContact, xRD, xRA, xDate))
                
        else : # si la 1ère cellule de la ligne n'est pas vide
            # on indique que l'on ne sera plus à la création d'un nouveau fichier
            debutNouveauFichier = True
            fichierResultat.close ()  # fermeture du fichier
        
        # Si on a atteind la fin du fichier
        if ligneFichier == len(maMatrice)-1 :  
            fichierResultat.close ()  # fermeture du fichier
            fichierIP.close ()  # fermeture du fichier
            
    FF.messageInfo("Succès", "L'opération s'est déroulée avec succès.")
    
    ### Fin programme **********************************************************