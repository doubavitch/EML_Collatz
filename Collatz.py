import pickle #ce module nous permettra d'enregistrer la liste de tous les entiers testés ainsi que leur temps de vol associé

L=[] #on crée une liste vide dans laquelle nous enregistrerons plus tard les entiers testés avec leurs temps de vol respectifs

def Collatz():
    n = int(input('Entrez votre nombre:'))
    i = 0
    L.append(n)
    while n != 1:
        print(n)
        if n%2 == 0:
            n = n//2
            i += 1
        else:
            n = 3*n + 1
            i += 1
    print(1)
    print('Temps de vol:',i)
    L.append(i)
    L.append("/")
    #cette commande nous permet de sauvegarder la liste L dans un autre fichier
    with open('Sy.py', 'wb') as Syracuse:
        pickle.dump(L, Syracuse)


#cette commande nous permet de charger la liste L préalablement enregistrée afin de l'imprimer si nécessaire
with open('Sy.py', 'rb') as f:
    L = pickle.load(f)
