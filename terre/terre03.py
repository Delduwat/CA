"""
Terre03

Programme permettant d'afficher l'aphabet avec une boucle à partir de la lettre voulue
"""
import sys

def alphabet():
	return "abcdefghijklmnopqrstuvwxyz"
# end def

def main(input_letter='a'):
	alpha = alphabet()
	if input_letter not in alpha:
		return
	begin = alpha.index(input_letter)
	for letter in alpha[begin:]:
		print(letter, end='')
# end def


if __name__ == "__main__":
	if len(sys.argv) == 2:
		main(sys.argv[1])
# end if
