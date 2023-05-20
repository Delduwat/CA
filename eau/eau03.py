"""
Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0.


Exemples d’utilisation :
$> python exo.py 3
2
$>

Afficher -1 si le paramètre est négatif ou mauvais.

"""

import sys

"""
fibo

0 -> 0
1 -> 1


2 -> 1
3 -> 2
4 -> 3
5 -> 5
"""
def fibo(x):
    """
    J'ai choisi de ne pas faire de reccurssif pour éviter d'avoir des perfs horribles.
    """
    assert x >= 0, "le paramètre semble négatif"
    a=0
    b=1
    c=a+b

    # 0 -> 0 ; 1 -> 1
    if x < 2:
        return x
    
    for i in range(x-2):
        a=b
        b=c
        c=a+b

    return c

def main(value):
    print(fibo(int(value)))

def manage_args():
    assert len(sys.argv) == 2, "Le nombres d'arguments est incorrect"
    assert sys.argv[1].isdigit(), "L'argument n'est pas un entier positif"
    assert int(sys.argv[1])>=0, "L'argument est négatif"

if __name__ == "__main__":
    try:
        manage_args()
        main(sys.argv[1])
    except Exception as e:
        print("-1")
        # print(e)
# end if 