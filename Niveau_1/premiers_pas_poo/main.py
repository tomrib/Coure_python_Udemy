class Utilisateur:
    ESPESE = "humian"
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom
        self.age = age
        if nom == "":
            self.NouvelUtilisateur()

    def SePresenter(self):
        info_utilisateur = "Bonjour, je m'appelle " + self.nom

        if self.age != 0:
            print(info_utilisateur + " et j'ai ", self.age, " ans")
            if self.EstMajeur():
                print("et je suis majeur")
            else:
                print("et je suis mineur")
        else:
            print(info_utilisateur)

    def EstMajeur(self):
        return self.age >= 18

    def NouvelUtilisateur(self):
        self.nom = input("Quel est votre nom :")
        
    def AfficherInfoEtreVivant(self):
        print(utilisateur.ESPESE)


# Liste d'utilisateurs
liste_utilisateurs = [Utilisateur("toto", 25), Utilisateur("tata", 17), Utilisateur("tom",20)]

# Boucle pour présenter chaque utilisateur
for utilisateur in liste_utilisateurs:
    utilisateur.SePresenter()
    utilisateur.AfficherInfoEtreVivant()
    
