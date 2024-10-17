# -*- coding: utf-8 -*-
"""
Éditeur de Spyder
Ceci est un script temporaire.
"""
import random
import sys



sommets = int(input("Entrez le nombre de sommets :"))

while True:
    arcs = int(input(f"Entrez le nombre d'arcs doit être inférieur ou égale à {sommets**2} : "))
    if arcs <= sommets**2:
        break
    else:
        print(f"Le nombre d'arcs doit être inférieur à {sommets**2}. Veuillez réessayer.")
    


matrice = [[0 for _ in range(sommets)] for _ in range(sommets)]
c = 0
while c < arcs :
    i = random.randint(0, sommets-1)
    j = random.randint(0, sommets-1)
    if matrice[i][j] == 0 and i != j :
        matrice[i][j] = 1
        c+=1;
        
for ligne in matrice:
    print(ligne)

degP = 0
degM = 0
for j in range(sommets):
    for i in range(sommets):
        if matrice[i][j] == 1:
            degP += 1;
        if matrice[j][i] == 1:
            degM += 1;
if degP == degM :
    print("il y a equilibre ")
else:
    print("Il n'y a pas d'equilibre")
    





print("code fini", sys.argv)    
    
    
    
    
    