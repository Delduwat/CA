"""
terre08

puissance
"""

import sys

def calculate_power(a,b):
    return a**b

def main(input_1, input_2):
    x = calculate_power(int(input_1),int(input_2))
    print(x)
#end def

if __name__ == "__main__":
    try:
        assert(len(sys.argv) == 3)
        main(sys.argv[1],sys.argv[2])
    except:
        print("erreur.")	
# end if 