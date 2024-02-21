from collections import Counter

# Votre liste d'entrée
liste = [[2, 2], [2, 1], [1, 2], [0, 0], [0, 1], [1, 0], [2, 0], [0, 2], [2, 4], [2, 3], [1, 4], [0, 2], [0, 3], [1, 2], [2, 2], [0, 4], [4, 2], [4, 1], [3, 2], [2, 0], [2, 1], [3, 0], [4, 0], [2, 2], [4, 4], [4, 3], [3, 4], [2, 2], [2, 3], [3, 2], [4, 2], [2, 4]]

# Compter les occurrences de chaque élément dans la liste
compteur = Counter(tuple(element) for element in liste)

# Filtrer les éléments répétés trois fois
resultat = [list(element) for element, count in compteur.items() if count > 3]

print(resultat)

def compter_occurrences(liste):
    occurrences = {}
    for element in liste:
        key = tuple(element)
        occurrences[key] = occurrences.get(key, 0) + 1
    return occurrences

def filtrer_elements_repetes(liste, repetition):
    occurrences = compter_occurrences(liste)
    resultats = []
    for element, count in occurrences.items():
        if count == repetition:
            resultats.append(list(element))
    return resultats

# Votre liste d'entrée
liste = [[2, 2], [2, 1], [1, 2], [0, 0], [0, 1], [1, 0], [2, 0], [0, 2], [2, 4], [2, 3], [1, 4], [0, 2], [0, 3], [1, 2], [2, 2], [0, 4], [4, 2], [4, 1], [3, 2], [2, 0], [2, 1], [3, 0], [4, 0], [2, 2], [4, 4], [4, 3], [3, 4], [2, 2], [2, 3], [3, 2], [4, 2], [2, 4]]

# Filtrer les éléments répétés trois fois
resultat = filtrer_elements_repetes(liste, 4)

print(resultat)