# Fonction pour afficher la table de multiplication d'un nombre n dans une plage spécifiée
def multiplication(n: int, min=1, max=10):
    # Vérification si le numéro minimal est plus grand que le maximum
    if min > max:
        # Affichage du message d'erreur
        print("Le numéro minimal ne peut pas être plus grand que le maximum")
        return

    # Boucle pour itérer de min à max (inclus)
    for i in range(min, max + 1):
        # Affichage du résultat de la multiplication
        print(int(i), "x", int(n), "=", i * n)

# Saisie de l'utilisateur pour la valeur de n
n = int(input("Entrez un nombre pour afficher sa table de multiplication : "))

# Appel de la fonction multiplication avec les valeurs fournies
multiplication(n)
