"""
terre11

24 to 12
"""

import sys

def is_a_valid_24hour(s):
    valid = False
    try:
        h,m = s.split(':')
        assert 0 <= int(h) < 24, "les heures semblent incorrectes"
        assert 0 <= int(m) < 60, "les minutes semblent incorrectes"
        valid = True
    finally:
        return valid
        
def convert_in_12(hours_value_24):
    if is_a_valid_24hour(hours_value_24):
       h,m = hours_value_24.split(':')
       h= int(h)
       m= int(m)
       
       # 00:00 => 12:00 AM
       # 12:00 => 12:00 PM
       if h == 0:
        h2 = 12
       else:
        h2 = h%12

       ampm = 'AM' if h < 12 else 'PM'

    if m < 10:
        m = f"0{m}"
    if h2 < 10:
        h2 = f"0{h2}"

    return f"{h2}:{m}{ampm}"

def main(input_value):
    print(convert_in_12(input_value))
    

def manage_args():
    assert len(sys.argv) == 2, "Le nombres d'arguments est incorrect"
    assert is_a_valid_24hour(sys.argv[1]), "Le format d'heure est incorrect"

if __name__ == "__main__":
    try:
       manage_args()
       main(sys.argv[1])
    except:
       print("erreur.")
# end if 