# Tableau pré-rempli
myTable = [10, 5, 6, 11, 4, 3]
print(f"Tableau initial :\n{myTable}")

# Écrire un programme implémentant le tri à bulles complet, permettant de trier totalement
# un tableau grâce à l’algorithme du tri à bulles.

# On parcourt le tableau autant de fois qu'il y a d'éléments dans le tableau moins 1
# car dans le pire des cas on doit déplacer le dernier élément du tableau en première position,
# ce qui nécessite n-1 permutations (n=nombre d'éléments)
for i in range(len(myTable)-1):
    # Pour chaque itération, on s'arrête à l'avant dernier élément car le dernier élément n'a pas d'élément suivant
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
