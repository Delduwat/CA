"""
Terre02

Programme permettant d'afficher les arguments séparés d'un retour à la ligne
"""

import sys

def main():
	if len(sys.argv) < 2:
		exit
	for item in sys.argv[1:]:
		print(item)
# end def

if __name__ == "__main__":
	main()
# end if