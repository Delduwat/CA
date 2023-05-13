"""
terre04

Sont ils pair ou impair ?
"""

import sys

def is_it_even(value):
	return 'pair' if value % 2 == 0 else 'impair'
#end def

def main(value):
	# user input with sys.argv is string, so we can use isdigit
	try:
		print(is_it_even(int(value)))
	except:
		print("Tu ne me la mettras pas à l'envers.")
#end def

if __name__ == "__main__":
        input = sys.argv[1] if len(sys.argv) == 2 else ''
        main(input)
# end if
