# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:31:58 2020

@author: Pierre-Marie EDLINGER
"""
import FonctionsFichier as FF
import LigneParMateriel as LM

# Initialisation des variables globales
NOMFICHIERRESULTAT = "Resultat"
EXTENSIONFICHIER = ".ods"
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

def LanceCreationFichierCLS(fichierTravail, RepResultat):
    global debutNouveauFichier
    
    # on remplit une matrice avec toutes les lignes du fichier de travail
    maMatrice = FF.getRensDansFichier(fichierTravail)
    
    # Création du fichier des adresses IP
    fichierIP = open (RepResultat+"/ListeIPPourEtiquettes.ods", "w")    # Création et ouverture du fichier rempli
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
                fichierResultat = open (RepResultat+"/"+NOMFICHIERRESULTAT+maMatrice[ligneFichier][0]+EXTENSIONFICHIER, "w")    # Création et ouverture du fichier rempli
                
                # on rempli l'entête des colonnes
                enteteColonnes(fichierResultat)
            # else:
            #     #on rajoute au fichier
            #     fichierResultat = open (RepResultat+NOMFICHIERRESULTAT+maMatrice[ligneFichier][0]+EXTENSIONFICHIER, "a")
            
            #On initialise tous les paramètres
            XXX = maMatrice[ligneFichier][0] 
            xIP = maMatrice[ligneFichier][1]
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