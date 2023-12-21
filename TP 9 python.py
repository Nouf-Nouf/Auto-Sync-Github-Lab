# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:00:31 2023

@author: nbouc
"""

l = [1, 2, 3, 4]

def mon_decorateur(fonction):
    def inner(*param, **param2):
        print("Action avant ")
        fonction(*param, **param2)
        print("Action après ")
    return inner  # Add this line to fix the issue

# Apply the decorator to a function using @mon_decorateur just before the function definition
@mon_decorateur
def Affichage(v):
    print("Execution des instructions", v)

# Call the decorated function
Affichage(l)

#%%

import time

def mon_decorateur2(function):
    def compteur(*param,**param2):
        debut = time.time()
        print ("temps avant code",debut)
        function(*param,**param2)
        fin = time.time()
        print("temps après code", fin)
        temps = fin - debut
        print ("temps d'execution de la fonction a été de ", temps, " sec ")
        
        
    return compteur


@mon_decorateur2
def exemple_methode():
    # Votre code ici
    time.sleep(2)
    print("Fin de la méthode")

# Appel de la méthode décorée
exemple_methode()


#%%

import numpy as np
import matplotlib.pyplot as plt

#p0 est la position initiale de l'extrémité fixe du ressort
p0=np.array([0.,0.,0.])

#p1 est la position au repos de l'extrémité libre du ressort
p1=np.array([0.,-1.,0.])

#m est la masse de l'extrémité libre
m=1.0

#k est la raideur du ressort
k=0.1

#amort est l'amortissement du ressort
amort=0.1

#deltat est le pas d'integration
deltat=1.0

#time_sim est le temps de la simulation
time_sim=50

#m*gamma=somme des forces
#m*gamma=-amort*v-k*deltaLong*BA/norm(BA) où BA est un vecteu
    
#Calcul de la longueur initiale
longueur = np.sqrt(np.dot(p1 - p0, p1-p0))
vitesse = np.array([0.,0.,0.])

p1 = np.array([0.,-1.1,0.])
longueur1 = np.sqrt(np.dot(p1-p0,p1-p0))
delta = longueur1 - longueur

etapes = np.arange(0,time_sim,deltat)

deltaLongList = []

for i in etapes:
    print ("etape : ", i)
    
    #Calcul ACC1
    
    #Acc = (ammor)
    
    #Calcul V1
    
    #Calcul Position p1
    