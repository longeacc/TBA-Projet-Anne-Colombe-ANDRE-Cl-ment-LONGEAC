# Define the Player class.
class Player():
    """
    Classe Player qui gère les actions et l'état du joueur dans le jeu.

    Attributs:
        name (str): Nom du joueur.
        current_room (Room): Salle actuelle où se trouve le joueur.
        history (list): Liste des salles précédemment visitées.
        inventory (dict): Inventaire du joueur, contenant les objets ramassés.
    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory={}


    # Define the move method.
    def move(self, direction):
        """
        Déplace le joueur dans une direction donnée si une sortie existe.

        Args:
            direction (str): Direction dans laquelle le joueur souhaite se déplacer.

        Returns:
            bool: True si le déplacement a réussi, False sinon.
        """

        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]


        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        self.history.append(self.current_room)

        # Set the current room tos the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        #already visited room
        print("\nvous avez déjà visité les pièces suivantes:\n")
        for i in (self.history):
            print("-",i.name )
        return True


    # Define history
    def get_history2(self):
        """ 
        Affiche l'historique des salles déjà visitées par le joueur.

        Returns:
            bool: True une fois l'historique affiché.
        """

        print("vous avez déjà visité les pièces suivantes:\n")
        for i in(self.history):
            print("-",i.name)
        return True


    def get_inventory(self):
        """
        Affiche les objets présents dans l'inventaire du joueur.

        Returns:
            None
        """

        if not self.inventory:
            print("inventaire est vide ")
            return

        for item in self.inventory.values():
            print(f"{item.name}: {item.description} (Poids: {item.weight}kg)")