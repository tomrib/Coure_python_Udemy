"""
Pour cet exercice, vous allez créer un programme de conversion d'unités,
qui sera capable de convertir des pouces (inch) en centimètres (cm), et vice-versa.
1 pouce = 2.54 cm
1 cm = 0.394 pouces

Exemple :
Un écran de 17 pouces de diagonale, correspond à 43,18 cm (=17*2.54)
Voici comment votre programme doit se comporter :
1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)
3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
- fin du programme.

Nombres à virgule :
Nous avons vu comment manipuler des données numériques avec Python,
notamment avec le type "int" qui concerne les nombres entiers (sans virgules).
Pour cet exercice, vous allez être amené à manipuler des nombres à virgule. Il s'agit du type "float".
Le principe du float est similaire à celui du int.
Pour utiliser un nombre à virgule, il faut utiliser le point (et non une virgule).

Exemples :
a = 5  # int
b = 5.2 # float
c = 5,2 # erreur : ne pas utiliser de virgule, mais le point

Optionnel :
Boucler pour convertir plusieurs valeurs (en conservant toujours le même sens de conversion),
 et proposer une option pour sortir du programme.

Votre réponse :
Codez avec l'éditeur de votre choix, puis faites un copier/coller de votre code directement dans le champ de la réponse.
Questions pour cet exercice
Collez directement votre code ici, en utilisant le formatage <> code.

OPTIONNEL :
Dites moi ici vos remarques : avez-vous aimé cet exercice ? Est-ce que c'était difficile/facile ?
 Souhaitez-vous d'autres exercices de ce type ? Combien de temps ça vous a pris ?
"""

"""
def cm_to_inch(cm):
    return cm * 0.394


def inch_to_cm(inch):
    return inch * 2.54


choice = input("Vouler vous convertire de pouces vers cm ou de cm vers pouces? ")
print()
if choice == "pouces vers cm" or choice == "cm vers pouces":
    answer = False
    while answer == False:
        try:
            value = float(input(f"Entrez la valeur à convertir en {choice}: "))
            answer = True
        except:
            print()
            continue_str = input("ERREUR: La valeur donnée n'est pas correcte! voulez vous continuer oui ou non ? ")
            if continue_str == "oui":
                answer
            else:
                exit()

    if choice.lower() == "pouces vers cm":
        results = inch_to_cm(value)
        unite_result = "cm"
    elif choice.lower() == "cm vers pouces":
        results = cm_to_inch(value)
        unite_result = "pouces"
    else:
        print("Choix invalide. Veuillez entrer 'pouces vers cm' ou 'cm vers pouces'")
        exit()

    print(f"La valeur convertie est: {results} {unite_result}")
else:
    print(f"{choice} nes pas une bonne reponce")
"""

def demander_et_afficher_conversion(unit1: str, unit2: str, facteur: float):
    valeur_str = input(f"Conversion {unit1} -> {unit2}. Donnez la valeur en {unit1} (ou 'q' pour quitter) : ")
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        print("(utilisez le point et non la virgule pour les décimales)")
        return demander_et_afficher_conversion(unit1, unit2, facteur)

    valeur_convertie = round(valeur_float * facteur, 2)
    print(f"Résultat de la conversion : {valeur_float} {unit1} = {valeur_convertie} {unit2}")
    return False


while True:
    # Menu : choix de la conversion
    print("Ce programme vous permet d'effectuer des conversions d'unités")
    print("1 - Pouces vers cm")
    print("2 - cm vers pouces")
    choix = input("Votre choix (1 ou 2): ")
    if choix == "1" or choix == "2":
        break
    print("ERREUR : Vous devez choisir 1 ou 2")

while True:
    # Demander les valeurs à convertir à l'utilisateur
    if choix == "1":
        if demander_et_afficher_conversion("pouces", "cm", 2.54):
            break
    if choix == "2":
        if demander_et_afficher_conversion("cm", "pouces", 0.394):
            break