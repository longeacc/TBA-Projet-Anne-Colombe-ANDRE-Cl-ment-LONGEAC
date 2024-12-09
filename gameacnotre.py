# Description: Game class
#clement test
# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.item=[]
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D, n, e, s, o, u, d, NORD, EST, SUD, OUEST, UP, DOWN, Nord, Est, Sud, Ouest, Up, Down, nord, est, sud, ouest, up, down )", Actions.go, 1)
        self.commands["go"] = go
        
        history = Command("history", " : enregistrer l'avancement", Actions.get_history, 0)
        self.commands["history"] = history
        
        back = Command("back", " : revenir dans la pièce précédente", Actions.get_back, 0)  # 🌸
        self.commands["back"] = back  # 🌸

        item= Command("command", ": quels sont mes outils à dispositions" , Game.__init__,0)
        self.commands["item"]=item

        # Setup rooms
        cave1 = Room("Cave1", "(salle1) Une pièce sombre, humide, avec un léger bruit d'eau gouttant.")
        cave2 = Room("Cave2", "(salle2) Vous rampez dans un tunnel dont les murs sont des pics qui vous empêchent de revenir en arrière.")
        cave3 = Room("Cave3", "(salle3) Un murmure étrange semble émaner des murs.")
        cave4 = Room("Cave4", "(salle4) Les quatre torches accrochées aux quatre coins de la pièce vous réchauffent le coeur.")
        cave5 = Room("Cave5", "(salle5) L'air devient plus frais, et un souffle de vent est perceptible.")
        cave6 = Room("Cave6", "(salle6) Au milieu de nulle part, vous tombez sur une grande armoire. Mais que fait-elle ici ?")
        cave7 = Room("Cave7", "(salle7) Vous sentez une odeur de soufre. Une chose est-elle en train de pourrir ?")
        cave8 = Room("Cave8", "(salle8) Un escalier étroit mène vers une pièce avec un tombeau ouvert.")

        
        # items def 

        épee = Item ("épée", " elle vous sera utile pour votre future aventure ! ", 10)
        
        clef = Item( "clé" ," une clef mais pour ouvrir quoin ?" , 1)
        cave1.inventory.append(clef)
        
        

       
        # Create exits for rooms(passage interdit/sens unique )

        cave1.exits = {"N" : cave2, "E" : None, "S" : None, "O" : cave7}
        cave2.exits = {"N" : cave3, "E" : None, "S" : None, "O" : None}
        cave3.exits = {"N" : None, "E" : None, "S" : cave2, "O" : cave4}
        cave4.exits = {"N" : None, "E" : cave3, "S" : None, "O" : cave5}
        cave5.exits = {"N" : None, "E" : cave4, "S" : cave6, "O" : None}
        cave6.exits = {"N": cave5, "E": None, "S": cave7, "O": None}
        cave7.exits = {"N": cave6, "E": cave1, "S": None, "O": None, "D": cave8}
        cave8.exits = {"N": None, "E":None, "S":None, "O":None, "U": cave7}


        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = cave1

        #setup artéfacts 
        

    # Mapping for direction normalisation (utilisation de plusieurs mots clés)
    DIRECTION_MAP = {
            "nord": "N",
            "est": "E",
            "sud": "S",
            "ouest": "O",
            "up": "U",
            "down": "D",
            "n": "N",
            "e": "E",
            "s": "S",
            "o": "O",
            "u": "U",
            "d": "D",
            "N": "N",
            "E": "E",
            "S": "S",
            "O": "O",
            "U": "U",
            "D": "D",
            "Nord": "N",
            "Est": "E",
            "Sud": "S",
            "Ouest": "O",
            "Up": "U",
            "Down": "D",
            "NORD": "N",
            "EST": "E",
            "SUD": "S",
            "OUEST": "O",
            "UP": "U",
            "DOWN": "D",
        }



    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
            # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player (commande vide)
    def process_command(self, command_string) -> None:
        if command_string=='':
            return

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]






         # Normalize direction if 'go' command is used
        if command_word == "go" and len(list_of_words) > 1:
            direction = list_of_words[1]
            normalized_direction = self.DIRECTION_MAP.get(direction, None)

            # Verifying if the direction exists using the DIRECTION_MAP
            if normalized_direction is None:
                print(f"\nDirection '{normalized_direction}' n'est pas une direction valide. La liste de commande disponible est: N, E, S, O, U, D, n, e, s, o, u, d, NORD, EST, SUD, OUEST, UP, DOWN, Nord, Est, Sud, Ouest, Up, Down, nord, est, sud, ouest, up, down.\n")
                return #Nothing happends 

            else:
                list_of_words[1] = normalized_direction


            normalized_direction = self.DIRECTION_MAP.get(direction, direction)
            list_of_words[1] = normalized_direction






        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
