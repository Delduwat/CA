"""
terre14

est-ce triée ?
"""

import sys

def is_sorted(list_of_values):

    item_to_compare = list_of_values[0]
    for i in range(1,len(list_of_values)):
        if list_of_values[i] < item_to_compare:
            return False
        item_to_compare = list_of_values[i]
    return True

def main(values):
    print("Triée !" if is_sorted(values) else "Pas triée !")    

def manage_args():
    assert len(sys.argv) >= 2, "Le nombres d'arguments est incorrect"
    for v in sys.argv[1:]:
        assert v.isdigit(), f"L'argument {v} n'est pas un entier"

if __name__ == "__main__":
    try:
       manage_args()
       main(sys.argv)
    except Exception as e:
       print("erreur.")
       print(e)
# end if 