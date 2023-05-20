"""
Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre.


Exemples d’utilisation :
$> python exo.py bonjour jour
true


$> python exo.py bonjour joure
false


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.


"""

import sys

"""
python chaineA in chaineB ... :see_no_evil:
"""


def main(base, sub):
    # je passe par une étape intermédiaire car en python c'est True et False avec des maj
    res = sub in base
    print(str(res).lower())

def manage_args():
    assert len(sys.argv) == 3, "Le nombres d'arguments est incorrect"
    for v in sys.argv[1:]:
        assert not v.isdigit(), f"L'argument {v} ressemble trop a un entier"


if __name__ == "__main__":
    try:
        manage_args()
        main(sys.argv[1],sys.argv[2])
    except Exception as e:
        print("error")
        # print(e)
# end if 