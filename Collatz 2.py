import pickle #ce module nous permettra d'enregistrer la liste de tous les entiers testés ainsi que leur temps de vol associé

L=[] #on crée une liste vide dans laquelle nous enregistrerons plus tard les entiers testés avec leurs temps de vol respectifs, et la valeur maximale atteinte dans la suite de Collatz associée

def Collatz():
    LV=[] #on crée une liste vide dans laquelle nous enregistrerons toutes les valeurs prises par n avant d'atteindre 1.
    n = int(input('Entrez votre nombre:'))
    i = 0
    L.append(n)
    while n != 1:
        LV.append(n)
        if n%2 == 0:
            n = n//2
            i += 1
        else:
            n = 3*n + 1
            i += 1
    LV.append(1)
    MAX= max(LV)
    print(LV)
    print('Valeur maximale atteinte :', MAX)
    print('Temps de vol :',i)
    L.append(i)
    L.append(MAX)
    L.append("/")
    #cette commande nous permet de sauvegarder la liste L dans un autre fichier
    with open('Sy.py', 'wb') as Syracuse:
        pickle.dump(L, Syracuse)

#cette commande nous permet de charger la liste L préalablement enregistrée afin de l'imprimer si nécessaire
with open('Sy.py', 'rb') as f:
    L = pickle.load(f)


