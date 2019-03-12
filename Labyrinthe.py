class Carte :

    """ Classe définissant une Carte de labyrinthe. Elle possède comme attibuts :
    - son nom - nom du fichier .txt associé
    - les données de la carte (une chaine de caractères)
    - sa largeur (permettra de décomposer la chaine de caractères)
    - La position de départ du joueur (peut être vide)
    - son record (nb de coups minimum réalisé jusqu'à présent pour sortir du labyrinthe
    - nom du joueur détenteur du record"""

    def __init__(self, Nom, ListeDonnées):
        """Constructeur de la carte.
        les 2 seuls paramètres nécessaires sont le nom de la carte et une liste contenant les données de chaque ligne.
        Les données de chaque ligne peuvent avoir des longueurs différentes"""

        self._Nom = Nom
        self._Largeur = max([len(ligne) for ligne in ListeDonnées])
        self._Donnees=""
        for ligne in ListeDonnées :
            while len(ligne) < self._Largeur :
                ligne += " "
            self._Donnees += ligne
        self.PositionDepart = self._Donnees.index("X")
        self.Record = 0
        self.Recordman = ""
        #TODO : supprimer le X de la map après avoir enregistré la position de départ


    def __repr__(self):
        return"Carte : Nom {} de taille {}x{}".format(self._Nom, self._Largeur, int(len(self._Donnees)/self._Largeur))

