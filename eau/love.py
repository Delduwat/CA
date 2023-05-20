class Plante():
    nb_plantes = 0

    def __init__(self, nom):
        Plante.nb_plantes+=1
        self.nom = nom
        self.frequence_arrosage = -1 # nb fois par mois
        self.a_soif = True
        self.exposition = ""

    def arroser(self):
        self.a_soif = False

    def __str__(self):
        x = "ARROSE MOI" if self.a_soif else ""
        out= f"{self.nom} - {self.frequence_arrosage} / mois - {self.exposition} - {x}"
        return out

p1 = Plante("monstera")
p2 = Plante("chaine de coeur")

p1.frequence_arrosage = 2
p1.exposition = "plein nord"
p2.exposition = "fort, plein soleil"

p1.arroser()
print(p1)
print(p2)


print(f"Il y a {Plante.nb_plantes} plantes en tout")