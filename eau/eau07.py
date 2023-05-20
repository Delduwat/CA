"""
Créez un programme qui met en majuscule la première lettre de chaque mot d’une chaîne de caractères. Les autres lettres devront être en minuscules. Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.


Exemples d’utilisation :
$> python exo.py “bonjour mathilde, comment vas-tu ?!”
Bonjour Mathilde, Comment Vas-tu ?!


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.



"""

import sys


def main(value):
    print(value.title()) # cheat code ?

def validate_input(value):
    for letter in value:
        if letter.isalpha() or letter in "!?; -_":
            pass
        else:
            return False
    return True

def manage_args():
    assert len(sys.argv) == 2, "Le nombres d'arguments est incorrect"
    assert validate_input(sys.argv[1]), "validation failed."

if __name__ == "__main__":
    try:
        manage_args()
        main(sys.argv[1])
    except Exception as e:
        print("error")
        print(e)
# end if 