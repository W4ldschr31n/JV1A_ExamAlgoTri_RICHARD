# Tableau pré-rempli
myTable = [10, 5, 6, 11, 4, 3]
print(f"Tableau initial :\n{myTable}")

# Écrire un programme permettant de permuter deux valeurs du tableau myTable
indiceMax = len(myTable)-1
indice1 = int(input(f"Premier indice à permuter? [0-{indiceMax}]\n"))
indice2 = int(input(f"Second indice à permuter? [0-{indiceMax}]\n"))

# Permutation des valeurs
valeurTmp = myTable[indice1]
myTable[indice1] = myTable[indice2]
myTable[indice2] = valeurTmp

# Affichage du résultat
print(f"Tableau après permuation ({indice1}<->{indice2}) :\n{myTable}")