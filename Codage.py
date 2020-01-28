# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 08:23:18 2020

@author: ruellee
"""
from Arbre import Arbre

class Codage:
    
    def __init__(self,text):
        self.text=text
        self.elem=self.alphaFreq()
        self.listeArbre=[]
        
    #retourne la liste triee composee de tuple (frequence,lettre)
    def alphaFreq(self):
        fichier=open(self.text,"r")
        self.listeAlpha=[]
        liste=[]
        for ligne in fichier:
            for lettre in ligne:
                if lettre not in self.listeAlpha:
                    self.listeAlpha.append(lettre)
                    freq=self.frequence(lettre)
                    liste.append((freq,lettre))
        fichier.close
        # On retourne la liste triee 
        return sorted(liste)
        
    # Retourne le nbr de fois que la lettre passée en paramètre apparait
    # dans le texte
    def frequence(self,lettre):
        fichier=open(self.text,"r")
        cpt=0
        for ligne in fichier:
            for l in ligne:
                if l==lettre:
                    cpt=cpt+1
        fichier.close
        return cpt
        
#==============================================================================
        ''' CREATION DE L'ARBRE'''
#==============================================================================
        
    def indexNouvelArbre(self,arbre):
        listeVal=[]
        nouvelArbre=(arbre.valeur,arbre.label)
        for arbre in self.listeArbre:
            listeVal.append((arbre.valeur,arbre.label))
        listeVal.append(nouvelArbre)
        l=sorted(listeVal)
        index=l.index(nouvelArbre)
        return index
        
        
    # Cree un arbre composé d'un seul noeud sans enfant pour chaque lettre 
    # qui compose le texte
    def creationFeuille(self):
        for (u,v) in self.elem:
            self.listeArbre.append(Arbre(v,u))
        
    # Cree l'arbre complet pour le codage
    def arbre(self):
        self.creationFeuille()
        while len(self.listeArbre)!=1:
            self.creationArbre()
        
    #Cree un arbre dont la racine a les deux plus petit element de listeArbre 
    #(qui sont ensuite enleves de listeArbre) et l'ajoute a listeArbre à la bonne place
    # il a comme valeur la somme des deux frequences de ses enfants
    def creationArbre(self):
        # On prend les 2 plus petit elements de listeArbre
        abr1=self.listeArbre[0]
        abr2=self.listeArbre[1]
        
        # On cree un nouvel arbre qui va avoir 2 enfants (abr1 et abr2)
        arbre=Arbre("",abr1.valeur+abr2.valeur,abr2,abr1)
        
        # On enleve les 2 plus petit elements de listeArbre
        self.listeArbre.pop(1)
        self.listeArbre.pop(0)
        
        # On recupère l'index de la place ou doit etre placer arbre
        index=self.indexNouvelArbre(arbre)
        
        # On ajoute arbre au bon endroit dans listeArbre
        self.listeArbre[index:index]=[arbre]
        
    # Affiche l'arbre
    def drawArbre(self):
        self.listeArbre[0].parcoursProfondeur()
            
#==============================================================================
        ''' CREATION DU CODAGE'''
#==============================================================================          

    def creationCode(self):
        code=""
        self.arbre()
        fichier=open(self.text,"r")
        for ligne in fichier:
            for lettre in ligne:
                code=code+self.listeArbre[0].codeLettre(lettre)
        return code
    
    def tauxCompression(self)
        
        
        
        
        
#==============================================================================
        ''' TEST DU CODE'''
#==============================================================================
        
code=Codage("textesimple.txt")
result=code.creationCode()
print(result)

