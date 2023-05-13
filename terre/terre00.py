"""
Terre00

Programme permettant d'afficher l'aphabet avec une boucle
"""

def alphabet():
	return "abcdefghijklmnopqrstuvwxyz"
# end def

def main():
	for letter in alphabet():
		print(letter,end='')
# end def


if __name__ == "__main__":
	main()
# end if
