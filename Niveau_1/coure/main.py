def maj(age):
    if age >= 18:
        return True
    return False

def user_info(name="", age=0):
    if name == "":
        return print("Merci de rentre votre nom !")

    if age == 0:
        print("La personne est", name)
    else:
        print("La personne est", name + ", son age est", age, "ans")
    
    print("Le nom comporte", len(name), "caractéres.")

age= 0

age = input("quel et votre age : ")

user_info("",17)

info_age = maj(int(age))
if info_age:
    print("il est majeur")
else:
    print("il est mineur")
