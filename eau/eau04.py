"""
Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.


Exemples d’utilisation :
$> python exo.py 14
17
$>

Afficher -1 si le paramètre est négatif ou mauvais.

"""

import sys

"""
idée : reprendre terre10 capable de determiner si oui ou non un nombre est premier
"""
def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def main(value):
    value = int(value)
    while True:
       value +=1
       if is_prime(value):
          break
       
    print(value)

def manage_args():
    assert len(sys.argv) == 2, "Le nombres d'arguments est incorrect"
    assert sys.argv[1].isdigit(), "L'argument n'est pas un entier positif"
    assert int(sys.argv[1])<99999, "L'argument est trop grand"

if __name__ == "__main__":
    try:
        manage_args()
        main(sys.argv[1])
    except Exception as e:
        print("-1")
        # print(e)
# end if 