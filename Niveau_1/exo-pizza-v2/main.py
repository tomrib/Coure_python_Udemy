class Pizza:
    def __init__(self, name, prix, ingredients, vg=False):
        self.name = name
        self.prix = prix
        self.ingredients = ingredients
        self.vg = vg

    def Afficher(self):
        description = ""
        if self.vg:
            description = " - végétarienne"

        print(f"PIZZA {self.name}: {self.prix} € {description}")
        print(", ".join(self.ingredients))
        print()

class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    DERNIER_NUMERO = 0

    def __init__(self, ):
        super().__init__("Personnalisée " + self.number, 0, [])
        PizzaPersonnalisee.DERNIER_NUMERO += 1
        self.number = PizzaPersonnalisee.DERNIER_NUMERO 
        self.demander_ingredients()
        self.calcule_prix()

    def demander_ingredients(self):
        print("----------------------------------")
        print("Ingrédients disponibles pour la pizza personnalisée ", self.number, ": tomate, jambon, lardon, poulet, olive, fromage")
        while True:
            print()
            ingredient = input("Ajoutez un ingrédient (ou appuyez sur ENTRE pour terminer): ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) {', '.join(self.ingredients)}")

    def calcule_prix(self):
        self.prix = self.PRIX_DE_BASE + len(self.ingredients) * self.PRIX_PAR_INGREDIENT

liste_pizzas = [
    Pizza("4 fromages", 8.50, ("brie", "emmental", "comté", "parmesan"), True),
    Pizza("hawai", 11.0, ("ananas", "amantal", "jambon")),
    Pizza("calzone", 12.0, ("tomate", "jambon", "emmental")),
    PizzaPersonnalisee(),
    PizzaPersonnalisee()
]

def tri(e):
    return len(e.ingredients)

liste_pizzas.sort(key=tri, reverse=True)

for i in liste_pizzas:
    """_summary_
    if i.vg:
        i.Afficher()
    if not i.vg:
        i.Afficher()
    if "tomate" in i.ingredients:
        i.Afficher()
    if 10 > i.prix:
        i.Afficher()
    """
    i.Afficher()
