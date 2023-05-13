"""
terre12

12 to 24
"""

import sys


def split_12_hours_format(s):
    h,rest = s.split(':')
    ampm = rest[-2:]
    m = rest[:-2]
    return h,m,ampm

def is_a_valid_12hour(s):
    valid = False
    try:
        h,m,ampm = split_12_hours_format(s)
        assert 0 <= int(h) <= 12, "les heures semblent incorrectes"
        assert 0 <= int(m) < 60, "les minutes semblent incorrectes"
        assert int(m) + int(h) > 0, "heure et minutes a zero n'est pas envisagable"
        assert ampm in ["AM","PM"], "le meridien semble incorrect"
        valid = True
    # except AssertionError as e:
    #     print(e)
    finally:
        return valid
        
def convert_in_24(hours_value_12):
    if is_a_valid_12hour(hours_value_12):
       h,m,ampm = split_12_hours_format(hours_value_12)
       h= int(h)
       m= int(m)

       h2 = h+12 if ampm == "PM" else h
       # 12:00 AM => 00:00
       # 12:00 PM => 12:00
       if h == 12:
        if ampm == 'AM':
            h2 = 0
        else:
            h2 = 12
    

    if m < 10:
        m = f"0{m}"
    if h2 < 10:
        h2 = f"0{h2}"

    return f"{h2}:{m}"

def main(input_value):
    print(convert_in_24(input_value))
    

def manage_args():
    assert len(sys.argv) == 2, "Le nombres d'arguments est incorrect"
    assert is_a_valid_12hour(sys.argv[1]), "Le format d'heure est incorrect"

if __name__ == "__main__":
    try:
       manage_args()
       main(sys.argv[1])
    except:
       print("erreur.")
# end if 