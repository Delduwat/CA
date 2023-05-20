"""
Créez un programme qui détermine si une chaîne de caractères ne contient que des chiffres.


Exemples d’utilisation :
$> python exo.py “4445353”
true


$> python exo.py 42
true

$> python exo.py “Bonjour 36”
false

Afficher error et quitter le programme en cas de problèmes d’arguments.


"""

import sys


def check_digit_only(value):
    for l in value:
        if l not in "0123456789":
            return False
    return True

def main(value):
    print(str(check_digit_only(value)).lower())


def manage_args():
    assert len(sys.argv) == 2, "Le nombres d'arguments est incorrect"

if __name__ == "__main__":
    try:
        manage_args()
        main(sys.argv[1])
    except Exception as e:
        print("error")
        print(e)
# end if 