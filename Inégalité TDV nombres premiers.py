import numpy as np


MAX=int(input('Entrez la valeur maximale que peut prendre le plus grand des nombres premiers')) 
T=[]
S=0
p=0
P=[]

TDV=[] # Liste des temps de vols correspondant aux éléments de LN.


for n in range(0,MAX + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           P.append(n)
L=len(P)
         
def produit(liste):
    r = 1
    for element in liste:
        r *= element
    return r

def Collatz(n):
    l=n
    i = 0
    LN=[] # Liste vide dans laquelle on retrouvera tous les entiers naturels pour lesquels on calcule le temps de vol.
    while n != 1:
        LN.append(n)
        if n%2 == 0:
            n = n//2
            i += 1
        else:
            n = 3*n + 1
            i += 1
    TDV.append(i)

def Colllatz(n):
    l=n
    i = 0
    LN=[] # Liste vide dans laquelle on retrouvera tous les entiers naturels pour lesquels on calcule le temps de vol.
    while n != 1:
        LN.append(n)
        if n%2 == 0:
            n = n//2
            i += 1
        else:
            n = 3*n + 1
            i += 1
    T.append(i)
    print('Le temps de vol du produit des', L, 'premiers éléments premiers est :', i,'.')

for i in P:
    j=Collatz(i)
    S=sum(TDV)


print("Le nombre d'éléments premiers de 0 à",MAX,"est :",L,".") 
p= produit(P)
R=Colllatz(p)
M=sum(T)
print('La somme des temps de vol des', L, 'premiers éléments premiers est :', S, '.')




    

