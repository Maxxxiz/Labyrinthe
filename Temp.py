import os


def OpenCarte(Fichier) :
    os.chdir("cartes")
    CarteAOuvrir=open(Fichier,"r")
    contenu=CarteAOuvrir.read()
    Carte=contenu.split("\n")
    CarteAOuvrir.close()
    return Carte

def AfficherCarte(Carte):
    print(Carte)

print(os.curdir)
Carte=OpenCarte("facile.txt")
AfficherCarte(Carte)

