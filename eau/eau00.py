"""
Créez un programme qui affiche toutes les différentes combinaisons possibles de trois chiffres dans l’ordre croissant, dans l’ordre croissant. La répétition est volontaire.


Exemples d’utilisation :
$> python exo.py
012, 013, 014, 015, 016, 017, 018, 019, 023, 024, ... , 789
$>

987 n’est pas là parce que 789 est présent.

020 n’est pas là parce que 0 apparaît deux fois.

021 n’est pas là parce que 012 est présent.

000 n’est pas là parce que cette combinaison ne comporte pas exclusivement des chiffres différents les uns des autres.

"""

"""
notes

avec 1 chiffre : 
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
avec 2 chiffres :
01, 02, 03, 04, 05, 06, 07, 08, 09
12, 13, 14, 15, 16, 17, 18, 19
23, 24, 25, 26, 27, 28, 29,
33, 34

on a le couple (x,x+1..9)
a chaque nouvelle ligne, on incrémente x
ça semble être l'algo
on veut donc voir les sorties comme des str, plus simple à gérer
"""

def f2():
    out = []
    for i in range(9):
        for j in range(i,9):
            out.append(f"{i}{j+1}")
    return out

def f3():
    out = []
    for i in range(9):
        for j in range(i,9):
            for k in range(j,8):
                out.append(f"{i}{j+1}{k+2}")
    return out

"""
on se rend compte que comme la valeur de fin décrémente au fur et a mesure qu'on ajoute des nombres
car le résultat est x x+1 x+2
"""

def main():
    print(', '.join(f3()))
# end def

if __name__ == "__main__":
    main()
# end if