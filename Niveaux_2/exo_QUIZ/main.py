def demander_reponse_numerique_utilisateur(minimum, maximum):
    reponse_str = input("Votre réponse (entre {} et {}) : ".format(minimum, maximum))
    try:
        reponse_int = int(reponse_str)
        if minimum <= reponse_int <= maximum:
            return reponse_int

        print("ERREUR : Vous devez rentrer un nombre entre {} et {}".format(minimum, maximum))
    except ValueError:
        print("ERREUR : Veuillez rentrer uniquement des chiffres")
    return demander_reponse_numerique_utilisateur(minimum, maximum)


class Question:
    def __init__(self, titre, reponses, bonne_reponse):

        self.titre = titre
        self.reponses = reponses
        self.bonne_reponse = bonne_reponse

    def poser_question(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.reponses)):
            print("  ", i + 1, "-", self.reponses[i])

        print()
        resultat_response_correcte = False
        reponse_int = demander_reponse_numerique_utilisateur(1, len(self.reponses))
        if self.reponses[reponse_int - 1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")

        print()
        return resultat_response_correcte

class Guestionnaire:
    def __init__(self, guestion):
        self.guestion = guestion

    
    def launch_questionnaire(self):
        score = 0
        for question in  self.guestion:
            if question.poser_question(): 
                score += 1
        print("Score final : ",score, "sur" ,len(self.guestion))
        return score



questionnaire = [
    Question("Quelle est la capitale de la France ?", ["Marseille", "Nice", "Paris", "Nantes", "Lille"], "Paris"),
    Question("Quelle est la capitale de l'Italie ?", ["Rome", "Venise", "Pise", "Florence"], "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ["Anvers", "Bruxelles", "Bruges", "Liège"], "Bruxelles"),
]

# Lancement du questionnaire
questionnaire = Guestionnaire(questionnaire)
questionnaire.launch_questionnaire()
