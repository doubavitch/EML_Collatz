import numpy as np
import pickle #ce module nous permettra d'enregistrer la liste de tous les entiers testés ainsi que leur temps de vol associé

L=[] #on crée une liste vide dans laquelle nous enregistrerons plus tard les matrices testées avec leurs temps de vol respectifs

a = [[4,4]]

def Collatz():
    n = np.mat(a)
    print(n)
    l = len(a)
    c = len(a[0])
    i = 0
    L.append(n)
    b = np.ones((l,c), dtype=int)
    d = np.mat(b)
    comparison = n == d
    print(comparison)
    equal_matrices = comparison.all()
    print(equal_matrices)
    while equal_matrices == False:
        comparison = n == d
        equal_matrices = comparison.all()
        print(n)
        for j in range(l):
            for k in range(c):
                if (n[j,k])%2 == 0%2:
                    n[j,k] = (n[j,k])/2
                else:
                    n[j,k] = 3*(n[j,k])+1
        if i>500:
            quit()
        i+=1
    if i == 0:
        print('Temps de vol:',i)
    else:
        print('Temps de vol:',i-1)
    L.append(i)
    L.append("/")
    #cette commande nous permet de sauvegarder la liste L dans un autre fichier
    with open('Sy_Mat.py', 'wb') as Syracuse:
        pickle.dump(L, Syracuse)


#cette commande nous permet de charger la liste L préalablement enregistrée afin de l'imprimer si nécessaire
with open('Sy_Mat.py', 'rb') as f:
    L = pickle.load(f)
