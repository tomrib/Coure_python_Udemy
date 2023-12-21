noms = []

# Continuer à demander le nom jusqu'à ce qu'il ne soit plus saisi
while True:
    nom = input("Quel est votre nom : ")
    if nom == "":
        break
    noms.append(nom)

# Afficher les noms saisis
for i in noms:
    print(f"Votre nom est : {i}")
