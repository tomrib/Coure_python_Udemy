import random

MIN_NUMBER = 1
MAX_NUMBER = 10
ASK_A_NUMBER = 4


def ask_a_question():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    o = random.randint(0,1)
    operator_str = "+"
    if o == 1:
        operator_str = "*"
    resut = int(input(f"Calculez : {a} {operator_str} {b} = "))
    calculation = a + b
    if o == 1:
        calculation = a * b
    if resut == calculation:
        return True
    return False


plant_number = 0
for i in range(0, ASK_A_NUMBER):
    print(f"question N° {i + 1}")
    if ask_a_question():
        print("Réponse correcte")
        plant_number += 1
    else:
        print("Réponse incorrecte")
    print()
print(f"Votre note est : {plant_number} / {ASK_A_NUMBER}")
print()
if plant_number == ASK_A_NUMBER:
    print("Excellent ;-)")
elif plant_number == 0:
    print("Réviser vos maths :-(")
elif plant_number > int(ASK_A_NUMBER / 2):
    print("Pas mal :-)")
else:
    print("Peut mieux faire :-/")

