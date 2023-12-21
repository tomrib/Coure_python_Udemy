import time
import beepy

# Constantes pour les durées
DUREE_OEUF_COQUE = 3
DUREE_OEUF_MOLLET = 6
DUREE_OEUF_DUR = 9

# Affiche les options
print(f"a) Oeufs à la coque : {DUREE_OEUF_COQUE} minutes")
print(f"b) Oeufs mollets : {DUREE_OEUF_MOLLET} minutes")
print(f"c) Oeufs durs : {DUREE_OEUF_DUR} minutes")

# Demande à l'utilisateur de faire un choix
while True:
    choix = input("Comment voulez-vous vos œufs : ")
    if choix in ["a", "b", "c"]:
        break
    else:
        print("ERREUR : Vous devez choisir entre a, b et c")

# Lance le minuteur en fonction du choix
if choix == "a":
    duree = DUREE_OEUF_COQUE
elif choix == "b":
    duree = DUREE_OEUF_MOLLET
else:  # choix == "c"
    duree = DUREE_OEUF_DUR

# Affiche les points et la durée restante pendant la cuisson
for i in range(duree * 60, 0, -1):
    time.sleep(1)
    print(".", end="", flush=True)
    # Affiche la durée restante toutes les 10 secondes
    if i % 10 == 0:
        minutes = i // 60
        seconds = i % 60
        print(f"\nTemps restant : {minutes:02d}:{seconds:02d}", end="", flush=True)

print("\nCuisson terminée")
beepy.beep(sound="ping")
