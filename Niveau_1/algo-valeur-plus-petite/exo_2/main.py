nom_chauffeur =       ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]
distance_chauffeur_km = [1.5,      2.2,    0.4,    0.9,    7.1,     1.1,      0.6]

index_min = 0
distance_min = distance_chauffeur_km[0]
for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    if distance < distance_min:
        distance_min = distance
        index_min = i

print("Distance minimale:", distance_min, "km")
print("Index de la distance minimale:", index_min)
print("Nom du chauffeur :",nom_chauffeur[index_min])