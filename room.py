# Define the Room class.
"""
Cette classe définie les méthodes d'entrée et de sortie des différentes salles en ajoutant leurs états à chaques fois

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
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
