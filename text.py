# Création d'une liste de test
ma_liste = [3, 4, 5]

# Parcours de la liste
for i in range(len(ma_liste)):
    if ma_liste[i] == 1:
        del ma_liste[i]  # Suppression de l'élément
        break  # Sortir de la boucle pour éviter les erreurs d'indexation après la suppression

# Ajout de 1 à la liste
else:
    ma_liste.append(1)

print(ma_liste)