"""
Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.


Exemples d’utilisation :
$> python exo.py “Hello world !”
HeLlO wOrLd !


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.


"""

import sys

def maj_sur_deux(s):
    out = ""
    should_upper = True
    for l in s:
        if should_upper and l.isalpha():
            out+=l.upper()
            should_upper=False
        elif not should_upper and l.isalpha():
            out+=l
            should_upper=True
        else:
            out+=l
    return out


def main(value):
    print(maj_sur_deux(value))

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