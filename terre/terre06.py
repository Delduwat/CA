"""
terre06

inverser une chaine
"""

import sys

# def reverse_string(s):
# 	return(s[::-1])	
# # end def

def reverse_string(s):
	s2 = ''
	for i in range(len(s)):
		s2+=s[len(s)-1-i]
	return s2
# end def

def main(s):
	try:
		print(reverse_string(s))
	except:
		print("erreur.")
#end def

if __name__ == "__main__":
	to_reverse = ''
	if len(sys.argv) == 2:
			to_reverse = sys.argv[1]
	main(to_reverse)
# end if
