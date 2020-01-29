# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:21:32 2020

@author: elsar
"""

from Codage import Codage
class Main:
    code=Codage("alice")
    taux=code.tauxCompression()
    code.creationFichierAlphabet()
    #code.drawArbre()
    print("Taux de compression : ",taux)
    