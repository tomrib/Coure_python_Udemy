def post(collection: list, number=None):
    if len(collection) == 0:
        print(" ---- AUCUNE PIZZA ---- ")
    else:
        print(f" ---- LISTE DES PIZZAS ( {len(collection)} ) ---- ")
        collection.sort()
        if number is not None:
            for i in collection[:number]:
                print(i)
        else:
            for i in collection:
                print(i)
        print()
        print("Première pizza : " + collection[0])
        print("Dernière pizza : " + collection[-1])


def add_pizza_user(collection):
    new_pizza = input("Nom de la nouvelle pizza : ")
    
    if new_pizza.lower() in collection:
        print("ERREUR : Cette pizza existe déjà.")
    else:
        if new_pizza.strip() != "":
            collection.append(new_pizza)


pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]
vide = []

add_pizza_user(pizzas)
post(pizzas)