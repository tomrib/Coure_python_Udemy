import random
import time
import os

"""
Vous allez demander à l'utilisateur de mémoriser une séquence de chiffres de plus en plus longue.

La séquence sera aléatoire, et commencera avec 4 chiffres. 
L'utilisateur à 3 secondes pour la mémoriser.

Si il donne la bonne réponse, on rajoute un nouveau chiffre à la suite de la séquence on la redemande à l'utilisateur...
 et ainsi de suite, jusqu'à ce que l'utilisateur se trompe.
"""
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


time.sleep()
clear_screen()
print("coucou")