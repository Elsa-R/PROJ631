# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:43:10 2020

@author: ruellee
"""

class Arbre:
    
    def __init__(self,label,valeur,filsDroit=None,filsGauche=None):
        self.label=label
        self.valeur=valeur
        self.filsDroit=filsDroit
        self.filsGauche=filsGauche
        
    def parcoursProfondeur(self):
        print("arbre : -",self.label,"- ",self.valeur)
        self.valEnfants()
        if self.filsGauche!=None:
            self.filsGauche.parcoursProfondeur()
        if self.filsDroit!=None:
            self.filsDroit.parcoursProfondeur()
    
    def valEnfants(self):
        l=[]
        for enfant in [self.filsGauche,self.filsDroit]:
            if enfant!=None:
                l.append((enfant.label,enfant.valeur))
        print('enfant :',l)
        
    def drawArbre(self):
        print("arbre : -",self.label,"- ",self.valeur)
        self.valEnfants()
        if self.filsGauche!=None:
            self.filsGauche.drawArbre()
        if self.filsDroit!=None:
            self.filsDroit.drawArbre()
    
    def codeLettre(self,lettre,code=""):
        if lettre==self.label:
            return code
        else:           
            if self.filsGauche!=None:
                if self.filsGauche.codeLettre(lettre,code+"1")!=None:
                    return self.filsGauche.codeLettre(lettre,code+"1")
                if self.filsDroit!=None:
                    if self.filsDroit.codeLettre(lettre,code+"0")!=None:
                        return self.filsDroit.codeLettre(lettre,code+"0")