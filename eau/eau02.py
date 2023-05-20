"""
Créez un programme qui affiche ses arguments reçus à l’envers.


Exemples d’utilisation :
$> python exo.py “Suis” “Je” “Drôle”
Drôle
Je
Suis


$> python exo.py ha ho
ho
ha

$> python exo.py “Bonjour 36”
Bonjour 36

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""

import sys

def main(items):
    # on aurait aussi pu la faire plus long en faisant:
    # pour i de len(items) à 0, i-=1
    #   print items[i]
    
    print("\n".join(items[::-1]))

def manage_args():
    assert len(sys.argv) >= 1, "Le nombres d'arguments est incorrect"

if __name__ == "__main__":
    try:
        manage_args()
        main(sys.argv[1:])
    except Exception as e:
        print("error")
        # print(e)
# end if 