"""
terre05

division & reste
"""

import sys


def div_and_rest(a,b):
	output=""
	output+=f"résultat : {a//b}\n"
	output+=f"reste : {a%b}"
	return output

def main(a,b):
	try:
		assert b < a
		print(div_and_rest(int(a),int(b)))
	except:
		print("erreur.")
#end def

if __name__ == "__main__":
	a = b = ''
	if len(sys.argv) == 3:
			a,b = sys.argv[1], sys.argv[2] 
	main(a,b)
# end if
