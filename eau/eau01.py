"""
Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.


Exemples d’utilisation :
$> python exo.py
00 01, 00 02, 00 03, 00 04, ... , 00 99, 01 02, ... , 97 99, 98 99
$>
"""

"""
notes

i <- 0..98
j <- i+1..99

(i, j)
"""
def get_couples():
    out=[]
    for i in range(98):
        for j in range(i+1, 99):
            a=f"{'0' if i < 10 else ''}{i}"
            b=f"{'0' if j < 10 else ''}{j}"
            out.append((a,b))
    
    return out

def main():
    # sans doute améliorable avec une map
    print(", ".join([f"{item[0]} {item[1]}" for item in get_couples()]))
    

if __name__ == "__main__":
    main()
# end if