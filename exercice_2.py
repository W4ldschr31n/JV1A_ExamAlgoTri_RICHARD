# Tableau pré-rempli
myTable = [10, 5, 6, 11, 4, 3]
print(f"Tableau initial :\n{myTable}")

# Écrire un programme permettant le parcours du tableau au cours d’une itération du tri à bulles.

# On parcourt le tableau une seule fois
# On s'arrête à l'avant dernier élément car le dernier élément sera forcément déjà trié dans cette itération
for i in range(len(myTable)-1):
    currentValue = myTable[i]
    nextValue = myTable[i+1]
    # Si la valeur observée est plus grande que la valeur suivante, on la fait "remonter" vers la fin du tableau
    if currentValue > nextValue:
        # Permutation des valeurs
        myTable[i] = nextValue
        myTable[i+1] = currentValue

# Affichage du résultat
print(f"Tableau après une seule itération :\n{myTable}")