# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory={}
    

    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]



        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        self.history.append(self.current_room)

        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        #already visited room
        print("\nvous avez déjà visité les pièces suivantes:\n")
        for i in (self.history):
            print("-",i.name )
        return True

        
        
      
    # Define history
    def get_history2(self):
        print("vous avez déjà visité les pièces suivantes:\n")
        for i in(self.history):
            print("-",i.name)
        return True       
    
    
    
    def get_inventory(self):
        if not self.inventory:
            print("inventor est vide ")
            return
        inventory_description= f"\n \t -{item.name}: {item.description} ({item.weight} kg)" for item in self.inventory.values()    
        return "vous avez comme des intervenai".join(inventory_description)
        
