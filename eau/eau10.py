"""
Créez un programme qui affiche le premier index d’un élément recherché dans un tableau. Le tableau est constitué de tous les arguments sauf le dernier. L’élément recherché est le dernier argument. Afficher -1 si l’élément n’est pas trouvé.


Exemples d’utilisation :
$> python exo.py Ceci est le monde qui contient Charlie un homme sympa Charlie
6


$> python exo.py test test test
0

$> python exo.py test boom
-1

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""

import sys


def where_is(search,items):
    for id,item in enumerate(items):
        if item == search:
            return id
    return -1

def main(items):
    to_find = items[-1]
    rest = items[:-1]
    print(where_is(to_find, rest))




if __name__ == "__main__":
    try:
        main(sys.argv[1:]) # because [0] is eau.py
    except Exception as e:
        print("error")
        print(e)
# end if 