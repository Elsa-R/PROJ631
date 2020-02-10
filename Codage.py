# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 08:23:18 2020

@author: ruellee
"""
import os
from Arbre import Arbre

class Codage:
    
    # Constructeur
    def __init__(self,text):
        self.text=text
        self.longueurTexte=0
        self.elem=self.alphaFreq()
        self.listeArbre=[]
        
    # Retourne la liste triee composee de tuple (frequence,lettre)
    def alphaFreq(self):
        fichier=open(self.text+".txt","r")
        self.listeAlpha=[]
        liste=[]
        for ligne in fichier:
            for lettre in ligne:
                self.longueurTexte=self.longueurTexte+1
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
        fichier=open(self.text+".txt","r")
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
    
    # Retourne l'index de l'arbre passe en parametre quand celui-ci se trouve 
    # dans la listeArbre triee
    def indexNouvelArbre(self,arbre):
        listeVal=[]
        # On recupere le tuple (freq,lettre) de l'arbre passe en parametre
        nouvelArbre=(arbre.valeur,arbre.label)
        # On recupere le tuple (freq,lettre) des arbres de listeArbre
        for arbre in self.listeArbre:
            listeVal.append((arbre.valeur,arbre.label))
        # On ajoute le tuple de l'arbre passe en parametre dans la liste
        listeVal.append(nouvelArbre)
        #On trie la liste
        l=sorted(listeVal)
        #On retourne l'index de l'arbre passe en parametre
        return l.index(nouvelArbre)
          
      
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
        self.listeArbre[0].drawArbre()
            
#==============================================================================
        ''' CREATION DU CODAGE'''
#==============================================================================          
        
    # Retourne le code du texte passe en parametre dans le constructeur
    # Retourne une chaine de caractere
    def creationCode(self):
        code=""
        self.arbre()
        dico=self.dicoCode()
        fichier=open(self.text+".txt","r")
        for ligne in fichier:
            for lettre in ligne:
                code=code+dico.get(lettre)
                #code=code+self.listeArbre[0].codeLettre(lettre)
        fichier.close
        self.code=code
        self.creationFichierBinaire()
    
    def dicoCode(self):
        dico={}
        for alpha in self.listeAlpha:
            #print(alpha,' = ',self.listeArbre[0].codeLettre(alpha))
            dico[alpha]=self.listeArbre[0].codeLettre(alpha)
        return dico
    
    # Retourne le taux de compression
    def tauxCompression(self):
        self.creationCode()
        lCode=len(self.code)
        longTexte=8*self.longueurTexte
        return (1-(lCode/longTexte))*100

#==============================================================================
        ''' CREATION DES FICHIERS'''
#============================================================================== 
    
    # Creation du fichier texte qui contient les lettres de l'alphabet et de leur frequence 
    def creationFichierAlphabet(self):
        self.fichierAlphabet=open(self.text+"_freq.txt","w")
        # Nombre de lettre dans l'alphabet
        self.fichierAlphabet.write(str(len(self.elem))+"\n")
        for (u,v) in self.elem:
            # Lettre et sa frequence 
            self.fichierAlphabet.write(v+" : "+str(u)+"\n")    
        self.fichierAlphabet.close()
        
    # Creation du fichier texte code
    def creationFichierOctet(self):
        self.fichierOctet=open(self.text+"_oct.txt","w")
        a=""
        for num in self.code:
            a=a+num
            if len(a)==8:
                self.fichierOctet.write(a+"\n")
                a=""
        while len(a)!=8 and len(a)!=0:
            a=a+"0"
        self.fichierOctet.write(a)
        self.fichierOctet.close()
        
    # Creation du fichier bianire
    def creationFichierBinaire(self):
        self.creationFichierOctet()
        with open(self.text+"_comp.bin","wb") as self.fichierBin:
            with open(self.text+"_oct.txt","r") as self.fichierOctet:
                for octet in self.fichierOctet:
                    nombre=0
                    cpt=0
                    for i in octet:
                        if i!="\n":
                            cpt=cpt+1
                            # On convertit le nombre binaire en nombre decimal
                            nombre=nombre+(int(i)*2**(8-cpt))
                    # On convertit le nombre decimal en octet 
                    n=(nombre).to_bytes(1, byteorder='big')
                    self.fichierBin.write(n)
                    #bytes(octet.encode('utf_8'))
            self.fichierOctet.close()
        self.fichierBin.close()
        somme=0
        dico=self.dicoCode()
        for (freq,lettre) in self.elem:
            somme=somme+(freq*(len(dico[lettre])))
        print("Nombre moyen de bits de stockage d’un caractère du texte compressé : ",somme/self.longueurTexte)   
#==============================================================================
        ''' FIN DU CODE '''
#==============================================================================        