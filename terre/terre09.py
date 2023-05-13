"""
terre09

trouver la racine
"""

from math import sqrt
import sys

def find_squarred_root(value):
    return int(sqrt(value))

def main(input_value):
    squarred = int(input_value)
    print(find_squarred_root(squarred))
    
def manage_args():
    # 1 seul argument voulu
    # il doit être un entier
    assert len(sys.argv) == 2, "Le nombres d'arguments est incorrect"
    assert sys.argv[1].isdigit(), "L'argument n'est pas un entier"

if __name__ == "__main__":
    try:
        manage_args()
        main(sys.argv[1])
    except:
        print("erreur.")	
# end if 