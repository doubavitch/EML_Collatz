import numpy as np
import matplotlib.pyplot as plt

LN=[] # Liste vide dans laquelle on retrouvera tous les entiers naturels pour lesquels on calcule le temps de vol.
VM=[] # Liste des valeurs maximales correspondant aux éléments de LN.
p= int(input('Entrez la première valeur pour laquelle vous voulez la valeur maximale associée.'))
m= int(input('Entrez la dernière valeur pour laquelle vous voulez la valeur maximale associée.'))
for i in range(p,m+1) :
    LN.append(i) # Liste des entiers naturels auxquels on applique Collatz allant de 1 jusqu'à m choisi.


def Collatz(n):
    i = 0
    l=n # On stocke la valeur du n testé avant qu'elle ne change.
    LV=[] #Liste vide dans laquelle on trouve toutes les valeurs prises par n avant d'atteindre 1.
    while n != 1:
        LV.append(n)
        if n%2 == 0:
            n = n//2
            i += 1
        else:
            n = 3*n + 1
            i += 1
    MAX=max(LV)
    VM.append(MAX)

for n in LN:
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

nuagedepoints(LN, VM, "Entiers naturels auxquels on applique Collatz", "Valeur maximale","Valeur maximale en fonction de leur entier naturel respectif")

plt.show()
    


