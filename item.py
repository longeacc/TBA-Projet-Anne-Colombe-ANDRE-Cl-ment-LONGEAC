"""définition de la classe Item"""
class Item :
    """
    Classe représentant un objet dans le jeu.

    Attributs:
        name (str): Nom de l'objet.
        description (str): Description de l'objet.
        weight (float): Poids de l'objet en kilogrammes.
    """

    def __init__(self,name ,description ,weight):
        self.name=name
        self.description = description
        self.weight = weight



    # on défini la méthode __str__() :
    def __str__(self):
        """
        Retourne une représentation textuelle de l'objet.

        Returns:
            str: Nom, description et poids de l'objet sous forme de chaîne.
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"