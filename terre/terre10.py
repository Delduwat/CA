"""
terre10

le nombre est il premier
"""

import sys

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def main(input_value):
    value = int(input_value)

    prime = False
    if value in [0,1]:
        prime = False
    else:
        prime = is_prime(value)
    
    if prime:
        print(f"Oui, {value} est un nombre premier.")
    else:
        print(f"Non, {value} n'est pas un nombre premier.")
    
def manage_args():
    assert len(sys.argv) == 2, "Le nombres d'arguments est incorrect"
    assert sys.argv[1].isdigit(), "L'argument n'est pas un entier"

if __name__ == "__main__":
    try:
       manage_args()
       main(sys.argv[1])
    except:
       print("erreur.")
# end if 