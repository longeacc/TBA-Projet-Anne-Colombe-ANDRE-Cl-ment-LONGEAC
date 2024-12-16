"""définition de la classe Item"""
class Item :
    """cette classe défini les méthodes de Item"""
    def __init__(self,name ,description ,weight):
        self.name=name
        self.description = description
        self.weight = weight



    # on défini la méthode __str__() :
    def __str__(self):
        """retourne la représentation textuelle du personnage"""
        return f"{self.name} : {self.description} ({self.weight} kg)"
