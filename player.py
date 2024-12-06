# Define the Player class.
#from gameacnotre import Game
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history=[]
        
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # Add the current room to history before moving.
        self.history.append(self.current_room)

        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        #print(self.Game.get_history()), # affiche l'historique lorsque le joueur va dans une mauvaise direction 
        return True
    
        # Define the get_history method.
    def get_history(self):
        """
        Returns a formatted string of the rooms visited by the player.

        Returns:
            str: The history of visited rooms.
        """
        if not self.history:
            return "Vous n'avez encore visité aucune pièce."

        # Generate the list of short descriptions of the visited rooms.
        history_descriptions = [room.get_short_description() for room in self.history]
        history_text = "Vous avez déjà visité les pièces suivantes :\n" + "\n".join(f"- {desc}" for desc in history_descriptions)
        return history_text
      


   