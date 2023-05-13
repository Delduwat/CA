"""
terre07

compter les lettres
on attend ici un seul parametre qui est une chaine, et pas de chiffre/nombre
"""

import sys

def count_letters(s):
	return len(s)

def main(s):
	try:
		assert not s.isdigit() # just to match what's wanted in exercice, in reality '123' is a three char string
		print(count_letters(s))
	except:
		print("erreur.")
#end def

if __name__ == "__main__":
	if len(sys.argv) != 2:
		# TODO (aga) : virer ça et faire en sorte d'avoir le message d'erreur une seule fois dans le code.
		print("erreur.")
		sys.exit(1)
	main(sys.argv[1])
# end if 
