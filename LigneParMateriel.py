# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:06:08 2020

@author: Pierre-Marie EDLINGER
"""
def getIP(XXX, num, xIP, CLS):
    machine = ""
    ip = ""
    numero = num
    if CLS==True: # Si c'est une UC de CLS
        ip = str(int(num)+10) # l'adresse IP est toujours le numéro de caisse + 10 pour les CLS
        machine = "CLS"
    else: # Si c'est un monnayeur
        ip = num
        numero = str(int(num)-44)
        machine = "Monnayeur"
    
    texte = ""
    texte = texte + "Mag "+XXX+"; - ;"+ machine +" n° "+numero+"; - ;IP: 172.24."+ xIP+"."+ip
    return texte

def getScanner(XXX, num, xVille, xSite, xContact, xRD, xRA, xDate):
    texte = ""
    texte = texte + ";scannercais"+XXX+"fm"+num+";Scanner CLS N°"+num
    texte = texte + " de F0"+XXX
    texte = texte + ";Actif (en parc);\\\\match-supermarket.com\\DSI\\DSI_Photos_Mag_FR\\Photos\\France\\"
    texte = texte + XXX+";Production;;France;Caisses;Magellan;Bi-optique 9800i;;;Physique;France;"
    texte = texte + xVille+";F0"+XXX+";"+xSite+";;;"+xContact+";;;5 Normal;"
    texte = texte + xRD+";"+xRA+";Match;France;;"+xDate
    texte = texte + ";;;PEBIX;;;;;;;;;;;;;;;;;;Externe;PEBIX;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
    return texte

def getMonnayeur(XXX, num, numCLS1, numCLS2, xIP, xVille, xSite, xContact, xRD, xRA, xDate):
    texte = ""
    texte = texte + ";cmonnayeur"+XXX+"fm"+num+";Monnayeur CLS N°"+numCLS1
    texte = texte + " et N°"+ numCLS2+" - MATCH – "+XXX+" - "
    texte = texte + xSite
    texte = texte + ";Actif (en parc);\\\\match-supermarket.com\\DSI\\DSI_Photos_Mag_FR\\Photos\\France\\"
    texte = texte + XXX+";Production;;France;Caisses;Glory;RCW-100;;;Physique;France;"
    texte = texte + xVille+";F0"+XXX+";"+xSite+";;;"+xContact+";;;5 Normal;"
    texte = texte + xRD+";"+xRA+";Match;France;;"+xDate+";;;Glory;;;;172.24."
    texte = texte + xIP+"."+num+";255.255.255.0;172.24."+xIP
    texte = texte + ".254;;;\"Ping;VNC\";;;;;;;;;Externe;Glory;;Unité caisse;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
    return texte

def getImprimanteM30(XXX, num, xVille, xSite, xContact, xRD, xRA, xDate):
    texte = ""
    texte = texte + ";impcai"+XXX+"fm"+num+";Imprimante CLS N° "
    texte = texte + num+" - MATCH – "+XXX+" – "+xSite
    texte = texte + ";Actif (en parc);\\\\match-supermarket.com\\DSI\\DSI_Photos_Mag_FR\\Photos\\France\\"
    texte = texte + XXX+";Production;;France;Caisses;Epson;TM M30;;;Physique;France;"
    texte = texte + xVille+";F0"+XXX+";"+xSite+";;;"+xContact+";;;5 Normal;"
    texte = texte + xRD+";"+xRA+";Match;France;;"+xDate
    texte = texte + ";;;PEBIX;;;;;;;;;;;;;;;;;;Externe;PEBIX;;Imprimante caisse;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
    return texte

def getCLS(XXX, num, xIP, xVille, xSite, xContact, xRD, xRA, xDate):
    ip = int(num)+10 # l'adresse IP est toujours le numéro de caisse + 10 pour les CLS
    
    texte = ""
    texte = texte + ";c"+XXX+"fm"+num+";Caisse Libre Service n° "+num+" de "+xSite
    texte = texte + ";Actif (en parc);\\\\match-supermarket.com\\DSI\\DSI_Photos_Mag_FR\\Photos\\France\\"
    texte = texte + XXX+";Production;;France;Caisses;HP;FLEX PRO C;Ubuntu;;Physique;France;"
    texte = texte + xVille+";F0"+XXX+";"+xSite+";;;"+xContact+";;Camélia;5 Normal;"
    texte = texte + xRD+";"+xRA+";Match;France;;"+xDate+";;;PEBIX;;;;172.24."
    texte = texte + xIP+"."+str(ip)+";255.255.255.0;172.24."+xIP
    texte = texte + ".254;;;\"Ping;VNC\";;;;;;;;;Externe;PEBIX;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
    return texte

def getMat(XXX, num, xVille, xSite, xContact, xRD, xRA, xDate):
    texte = ""
    texte = texte + ";cmat"+XXX+"fm"+num+";Mat Caisse Libre Service N° "+num
    texte = texte + "- MATCH - "+XXX+" – "+xSite
    texte = texte + ";Actif (en parc);\\\\match-supermarket.com\\DSI\\DSI_Photos_Mag_FR\\Photos\\France\\"
    texte = texte + XXX+";Production;;France;Caisses;ITAB;Light Tower Controller;LTC-02;;Physique;France;"
    texte = texte + xVille+";F0"+XXX+";"+xSite+";;;"+xContact+";;;5 Normal;"
    texte = texte + xRD+";"+xRA+";Match;France;;"+xDate
    texte = texte + ";;;ITAB;;;;;;;;;\"Ping;VNC\";;;;;;;;;Externe;ITAB;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
    return texte

def getBalance(XXX, num, xVille, xSite, xContact, xRD, xRA, xDate):
    texte = ""
    texte = texte + ";balancecls"+XXX+"fm"+num+";Balance Caisse Libre Service N° "+num
    texte = texte + "- MATCH - "+XXX+" - "+xSite
    texte = texte + ";Actif (en parc);\\\\match-supermarket.com\\DSI\\DSI_Photos_Mag_FR\\Photos\\France\\"
    texte = texte + XXX+";Production;;France;Caisses;ITAB;Flintab  AB;;;Physique;France;"
    texte = texte + xVille+";F0"+XXX+";"+xSite+";;;"+xContact+";;;5 Normal;"
    texte = texte + xRD+";"+xRA+";Match;France;;"+xDate+";;;ITAB;;;;;;;;;\"Ping;VNC\";;;;;;;;;Externe;ITAB;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
    return texte

def getEcran(XXX, num, xVille, xSite, xContact, xRD, xRA, xDate):
    texte = ""
    texte = texte + ";ecrancais"+XXX+"fm"+num+";Ecran Caisse LS n°"+num+" de "+xSite
    texte = texte + ";Actif (en parc);\\\\match-supermarket.com\\DSI\\DSI_Photos_Mag_FR\\Photos\\France\\"
    texte = texte + XXX+";Production;;France;Caisses;Elo touch;ET 2002L;;;Physique;France;"
    texte = texte + xVille+";F0"+XXX+";"+xSite+";;;"+xContact+";;Camélia;5 Normal;"
    texte = texte + xRD+";"+xRA+";Match;France;;"+xDate+";;;PEBIX;;;;;;;;;;;;;;;;;;Externe;PEBIX;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
    return texte

def getImprimanteStickers(XXX, num, xVille, xSite, xContact, xRD, xRA, xDate):
    texte = ""
    texte = texte + ";impsticker"+XXX+"fm0"+num+";Imprimante Sticker - MATCH -" 
    texte = texte + XXX+" – "+xSite
    texte = texte + ";Actif (en parc);\\\\match-supermarket.com\\DSI\\DSI_Photos_Mag_FR\\Photos\\France\\"
    texte = texte + XXX+";Production;;France;Imprimante Sticker;Zebra;ZQ610;;;Physique;France;"
    texte = texte + xVille+";F0"+XXX+";"+xSite+";;;"+xContact+";;;5 Normal;"
    texte = texte + xRD+";"+xRA+";Match;France;;"+xDate
    texte = texte + ";;;BEARCOD;;;;;;;;;;;;;;;;;;Externe;BEARCOD;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
    return texte

def getTexteFichierTravail():
    return "Numéro du magasin;IP Magasin;Nom de la ville;Nom du site;Contact sur le site;Responsable D;Responsable A;Date de mise à jour;Nbr CLS;Nbr Monnayeurs;Nbr Imprimantes Stickers"
    