def element_in_list(name, list):
    return name.lower() in [item.lower() for item in list]

names = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

if element_in_list("JeAn", names):
    print("Jean est là")
else:
    print("Jean n'est pas là")
