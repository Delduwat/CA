"""
Créez un programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. Min inclus, max exclus.


Exemples d’utilisation :
$> python exo.py 20 25
20 21 22 23 24


$> python exo.py 25 20
20 21 22 23 24

$> python exo.py hello
error

Afficher error et quitter le programme en cas de problèmes d’arguments.
"""

import sys


def gimme_range(a,b):
    x=min(a,b)
    y=max(a,b)
    return list(range(x,y+1,1))

def main(a,b):
    for item in gimme_range(int(a),int(b)):
        print(item, end=" ")
    print('')



def manage_args():
    assert len(sys.argv) == 3, "Le nombres d'arguments est incorrect"
    for v in sys.argv[1:]:
        assert v.isdigit(), f"L'argument {v} n'est pas un entier"

if __name__ == "__main__":
    try:
        manage_args()
        main(sys.argv[1], sys.argv[2])
    except Exception as e:
        print("error")
        print(e)
# end if 