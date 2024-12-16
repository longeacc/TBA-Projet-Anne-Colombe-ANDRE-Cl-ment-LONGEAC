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

    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        #self.inventory=set()
        self.inventory = {}
        # self.pnj={}


    # Define the get_exit method.
    def get_exit(self, direction):
        """Donne les sorties de la pièce.

    Args:
        

    Returns:
        
    """

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():

            return self.exits[direction]

        return None


    # Return a long description of this room including exits.
    def get_long_description(self):
        """Donne la description complète de la pièce.

    Args:
        

    Returns:
        
    """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
        return f"{self.description}\nObjets disponibles : {', '.join(self.items.keys()) if self.items else 'Aucun'}"


    # Return a string describing the room's exits.
    def get_exit_string(self):
        """Affiche les différentes sorties des pièces.

    Args:
        

    Returns:
        
    """
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string


    def get_inventory(self):
        """Donne les objets présents dans la pièce.

    Args:
        

    Returns:
        
    """
        if not self.inventory:
            print("inventaire est vide ")
            return
        inventory_description="\n".join(f"\t- {item.name}: {item.description} ({item.weight} kg)" for item in self.inventory.values())

        # pnj_description= "\n".join(f"\t- {charactere.name}: {charactere.description} " for charactere in self.pnj.values())


    def look(self):
        """
        Affiche la description complète des objets présents dans la pièce.
    

    Args:
        

    Returns:
        
    """
        print(self.get_long_description())
        if self.inventory:
            print("\nVous voyez les objets suivants :")
            for item in self.inventory.values():
                print(f"{item.name}: {item.description} (Poids: {item.weight}kg)")

            # for charactere in self.pnj.values():
            #     print(f"{pnj.name}: {pnj.description}")
        else:
            print("\nIl n'y a aucun objet ici.")
# """
#     def integer_PNJ(self):
#         """ affiche le nom du PNJ présent dans la piece
#         """

#         print(self.get_long_description_PNJ())
#         if self.pnj.values():
#             print("\nVous voyez les objets suivants :")
#             for charactere in self.pnj.values():
#                 print(f"{self.name_pnj} : {self.description} en cave ({self.current_room}) , dit nous ! {self.msg_char} " )
#         else:
#             print("\nIl n'y a personne ici. Vos lunettes sont sans doutes sales")"""
