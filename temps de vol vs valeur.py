import numpy as np
import matplotlib.pyplot as plt

LN=[] # Liste vide dans laquelle on retrouvera tous les entiers naturels pour lesquels on calcule le temps de vol.
TDV=[] # Liste des temps de vols correspondant aux éléments de LN.
m= int(input('Entrez la dernière valeur pour laquelle vous voulez le temps de vol.'))
for i in range(1,m+1) :
    LN.append(i) # Liste des entiers naturels auxquels on applique Collatz allant de 1 jusqu'à m choisi.


def Collatz(n):
    i = 0
    l=n # On stocke la valeur du n testé avant qu'elle ne change.
    while n != 1:
        if n%2 == 0:
            n = n//2
            i += 1
        else:
            n = 3*n + 1
            i += 1
    #i
    print("Temps de vol pour" , l , ":" ,i)
    TDV.append(i) # On aoute à TDV les temps de vols associés aux différents n dans LN. 

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

nuagedepoints(LN, TDV, "Entiers naturels auxquels on applique Collatz", "Temps de vol","Temps de vol en fonction de leur entier naturel respectif")

plt.show()
    

