# Tableau pré-rempli
myTable = [10, 5, 6, 11, 4, 3]
print(f"Tableau initial :\n{myTable}")

# Écrire un programme implémentant le tri à bulles complet, permettant de trier totalement
# un tableau grâce à l’algorithme du tri à bulles.

# On parcourt le tableau autant de fois qu'il y a d'éléments dans le tableau moins 1
# car si n-1 éléments sont triés à leur place, le dernier élément est forcément trié à sa place aussi
for i in range(len(myTable)-1):
    # Pour chaque itération, on s'arrête à l'avant dernier élément car le dernier élément 
    # sera forcément déjà trié dans cette itération
    for j in range(len(myTable)-1):
        currentValue = myTable[j]
        nextValue = myTable[j+1]
        # Si la valeur observée est plus grande que la valeur suivante, on la fait "remonter" vers la fin du tableau
        if currentValue > nextValue:
            # Permutation des valeurs
            myTable[j] = nextValue
            myTable[j+1] = currentValue

    # Affichage du résultat intermédiaire
    print(f"Tableau après l'itération {i+1} :\n{myTable}")

# Affichage du résultat final
print(f"Tableau après le tri complet :\n{myTable}")
