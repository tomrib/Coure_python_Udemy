def extensions_fichiers(fichiers):
    """
    La fonction "extensions_fichiers" prend une liste de noms de fichiers et renvoie une liste de leurs
    extensions de fichiers en minuscules.

    Args:
        fichiers: Le paramètre "fichiers" est une liste de noms de fichiers.

    Returns:
        une liste d'extensions de fichiers en minuscules.
    """
    extensions = [
        fichier.split(".")[-1] if "." in fichier else "" for fichier in fichiers
    ]
    extensions_lower = [extension.lower() for extension in extensions]
    return extensions_lower


def fichiers_par_extension(definition_extensions, fichiers):
    """
    La fonction "fichiers_par_extension" prend une liste d'extensions de fichiers et une liste de
    fichiers, et renvoie deux listes : une contenant des fichiers avec les extensions correspondantes,
    et une autre contenant des fichiers sans extensions ou avec des extensions inconnues.

    Args:
        definition_extensions: Le paramètre "definition_extensions" est une liste de tuples. Chaque tuple
    contient deux éléments : le premier élément est une chaîne représentant une extension et le deuxième
    élément est une chaîne représentant la définition ou la description de cette extension.
        fichiers: Le paramètre "fichiers" est une liste de noms de fichiers.

    Returns:
        The function `fichiers_par_extension` returns two lists: `fichiers_correspondants` and
    `fichiers_sans_extension`.
    """
    extensions_lower = extensions_fichiers(fichiers)
    fichiers_correspondants = []
    fichiers_sans_extension = []

    for i, extension in enumerate(extensions_lower):
        correspondant_trouve = False
        for d in definition_extensions:
            if d[0] == extension:
                fichiers_correspondants.append((fichiers[i], d[1]))
                correspondant_trouve = True
                break

        if not correspondant_trouve:
            fichiers_sans_extension.append(
                (
                    fichiers[i],
                    "Aucune extension" if not extension else "Extension non connue",
                )
            )

    return fichiers_correspondants, fichiers_sans_extension


fichiers = (
    "notepad.exe",
    "mon.fichier.perso.doc",
    "notes.TXT",
    "vacances.jpeg",
    "planning",
    "data.dat",
)

definition_extensions = (
    ("doc", "Document Word"),
    ("exe", "Executable"),
    ("txt", "Document Texte"),
    ("jpeg", "Image JPEG"),
)

# Le code appelle la fonction `fichiers_par_extension` avec les `definition_extensions` et `fichiers`
# comme arguments. Il attribue ensuite les valeurs renvoyées aux variables « correspondants » et «
# sans_extension ».
correspondants, sans_extension = fichiers_par_extension(definition_extensions, fichiers)

print("Fichiers correspondants :")
for fichier, description in correspondants:
    print(f"{fichier} ({description})")

for fichier, description in sans_extension:
    print(f"{fichier} ({description})")

"""
notepad.exe (Executable)
mon.fichier.perso.doc (Document Word)
notes.TXT (Document Texte)
vacances.jpeg (Image JPEG)
planning (Aucune extension)
data.dat (Extension non connue)
"""

""" 
lower/upper
in/index/for
split
-1 
"""



