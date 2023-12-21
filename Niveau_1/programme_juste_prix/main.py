import random
def user_number(MIN_NUMBER,MAX_NUMBER):
    number_int = 0
    while number_int == 0:
        number_str = input("quel est le nombre magique ( "+ str(MIN_NUMBER) + " et " + str(MAX_NUMBER) + " ) ?")
        try:
            number_int = int(number_str)
        except:
            print("ERREUR: vous dever rentre un nombre. Réessayez.")
        else:
            if number_int < MIN_NUMBER or number_int > MAX_NUMBER:
                print(f"ERREUR: le nombre doit être entre {str(MIN_NUMBER)} et {str(MAX_NUMBER)}. Réessayez.")
                number_int = 0
    return number_int

MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER,MAX_NUMBER)
LIVES_NUMBER = 4

"""number = 0
lives = LIVES_NUMBER
while not number == MAGIC_NUMBER and lives > 0:
    print(f"il voure reste {lives} vies.")
    number = user_number(MIN_NUMBER, MAX_NUMBER)
    if number == MAGIC_NUMBER:
        print("Bravo, vous avez gagné")
    elif number > MAGIC_NUMBER:
        print("le nombre magique et plus petit")
        lives -= 1
    else:
        print("le nombre magique et plus grand")
        lives -= 1

if lives == 0:
    print(f"vous avec perdu! Le nombre magique était: {MAGIC_NUMBER}")"""

won = False
for i in range(0,LIVES_NUMBER):
    lives = LIVES_NUMBER - i
    print(f"il voure reste {lives} vies.")
    number = user_number(MIN_NUMBER, MAX_NUMBER)
    if number == MAGIC_NUMBER:
        print("Bravo, vous avez gagné")
        won = True
        break
    elif number > MAGIC_NUMBER:
        print("le nombre magique et plus petit")
    else:
        print("le nombre magique et plus grand")


if won:
    print(f"vous avec perdu! Le nombre magique était: {MAGIC_NUMBER}")