"""
terre13

trouver milieu
"""

import sys


def main(a,b,c):
    l = [int(a),int(b),int(c)]
    if len(l) != len(set(l)):
        raise ValueError("Les valeurs de la liste doivent être différentes")
    l.sort()
    # on a 3 valeurs triées, donc la suisse est forcément à l'index 1
    print(l[1])
    

def manage_args():
    assert len(sys.argv) == 4, "Le nombres d'arguments est incorrect"
    for v in sys.argv[1:]:
        assert v.isdigit(), f"L'argument {v} n'est pas un entier"

if __name__ == "__main__":
    try:
        manage_args()
        main(sys.argv[1],sys.argv[2],sys.argv[3])
    except Exception as e:
        print("erreur.")
        print(e)
# end if 