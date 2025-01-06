# Define the Room class.
"""
Classe qui définie les méthodes d'entrée/sortie des salles ajoute leurs états à chaques fois

Description détaillée de la classe:
** le constructeur : __init__() , il défini l'état de la classe 

liste des attribus de la classe : 
** cela correspond à la question : dans quelle salle sommes-nous ? soit les salles allant de {1 à 8}
**  

liste des méthodes : 
** get_exit , elle définit la sortie de la salle 
** get_long_description(self),
** get_exit_string ,

Liste des exceptions levées par la classe :
Il y a une exception si l'on rencontre un mur ou que l'on ne peut pas sortir de la salle 

des exemples d'utilisations sous forme de doctests : 
"""

class Room:
    """
    Classe qui gère les salles d'un jeu, y compris leurs descriptions, sorties et inventaires.

    Attributs:
        name (str): Nom de la salle.
        description (str): Description de la salle.
        exits (dict): Dictionnaire des sorties de la salle, avec les directions \
        comme clés et les salles correspondantes comme valeurs.
        inventory (dict): Dictionnaire des objets disponibles dans la salle, \
        avec les noms comme clés et les objets comme valeurs.

    Exceptions:
        Aucune exception directe n'est levée, mais des validations\
         simples permettent d'éviter des actions invalides \
         (par exemple, demander une sortie inexistante).
    """

    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        #self.inventory=set()
        self.inventory = {}
        self.pnj={}

    #nécessaire pour ne pas avoir un affichage 0x7edd6001f7d0
    def __str__(self):
        return self.name

    # Define the get_exit method.
    def get_exit(self, direction):
        """
        Retourne la salle correspondante à une direction si elle existe.

        Args:
            direction (str): Direction demandée (par exemple, "nord", "sud").

        Returns:
            Room: La salle correspondant à la direction, ou None si aucune sortie n'existe.
        """


        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():

            return self.exits[direction]

        return None


    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Retourns:
            une description complète de la salle, y compris les sorties.

        Returns:
            str: Description complète de la salle avec les sorties.
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
        return f"{self.description}\nObjets disponibles : {', '.join(self.items.keys()) if self.items else 'Aucun'}"


    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
        Retourne une chaîne indiquant les sorties disponibles de la salle.

        Returns:
            str: Chaîne listant les sorties disponibles.
        """
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string


    def get_inventory(self):
        """
        Retourne une description des objets présents dans la salle.

        Returns:
            str: Description des objets dans la salle, \
            ou un message indiquant que l'inventaire est vide.
        """

        if not self.inventory:
            print("inventaire est vide ")
            return
        inventory_description="\n".join(f"\t- {item.name}: {item.description} ({item.weight} kg)" for item in self.inventory.values())


    def get_pnj(self):
        """dcc
        """
        if not self.pnj:
            print("il n'y a pas de pnj ici")
            return
        pnj_description = "\n".join(f"{character.name_pnj}, {character.description_pnj}, [{character.msg_pnj}]" for pnj in self.pnj.values())

    def look(self):
        """
        Affiche la description complète des objets présents dans la pièce.
        """

        print(self.get_long_description())
        if self.inventory:
            print("\nVous voyez les objets suivants :")
            for item in self.inventory.values():
                print(f"{item.name}: {item.description} (Poids: {item.weight}kg)")
        else:
            print("\nIl n'y a aucun objet ici.")
        
        if self.pnj:
            print("\nIl y a un PNJ dans cette pièce :")
            for character in self.pnj.values():
                print(f"{character.name}, {character.description_pnj}") #[{character.msgs}]
        else:
            print("\nIl n'y a personne ici. Vos lunettes sont sans doutes sales")