# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:21:32 2020

@author: elsar
"""

from Codage import Codage

if __name__ == '__main__':
    
    code=Codage("alice")
    code.creationFichierAlphabet()
    taux=code.tauxCompression()
    #print(code.listeArbre[0].codeLettre("p"))
    #code.drawArbre()
    print("Taux de compression : ",taux)