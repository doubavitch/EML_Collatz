import numpy as np
import matplotlib.pyplot as plt

LI=[] # Liste des itérations
LV=[] # Liste des valeurs prises par n à l'itération correspondante  
n= int(input("Entrez la valeur pour laquelle vous voulez la trajectoire d'itération."))

def Collatz(n):
    i = 0
    l=n # On stocke la valeur du n testé avant qu'elle ne change.
    while n != 1:
        LV.append(n)
        if n%2 == 0:
            n = n//2
            i += 1
        else:
            n = 3*n + 1
            i += 1
        LI.append(i) # On aoute à TDV les temps de vols associés aux différents n dans LN. 
    MAX=max(LV)
    print('Valeur maximale atteinte :', MAX)
    print('Temps de vol :',i)
Collatz(n) # Calcul du temps de vol pour tout n dans LN.

def nuagedepoints(x,y,xtitre,ytitre,titregraphe):
    """
    Fonction générant le nuage de points des y en fonction de x
    Entrées : coordonnées de x, coordonnates de y, titre des abcisses,  titre des ordonnées, titre
    Sorties : nuage de points de y en fonction de x
    """
    plt.plot(x, y, linestyle="none" ,marker="x" ,color="red", markersize="10", label="actual values")
    plt.xlabel(xtitre) # # Légende axe des abcisses
    plt.ylabel(ytitre) # Légende axe des ordonnées
    plt.title(titregraphe) # Donner un titre  

nuagedepoints(LI, LV, "n-ième itération", "valeur correspondant à la n-ième itération ","Trajectoire d'itération de "+str(n)+".")

plt.show()
