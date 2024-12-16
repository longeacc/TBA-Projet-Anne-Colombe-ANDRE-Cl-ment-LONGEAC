# Description: Game class
# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
import pygame 
from charactere import Charactere

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.room = []
        self.commands = {}
        self.player = None
        #self.actions = None
        self.item = []
        #self.pnj={}
    
    # Setup the game
    def setup(self):

        # definitions des talk des PNJ dans chaques room: 

        #talk = Command( "talk", " : vous parlez au grand mage", Actions)

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D, n, e, s, o, u, d, NORD, EST, SUD, OUEST, UP, DOWN, Nord, Est, Sud, Ouest, Up, Down, nord, est, sud, ouest, up, down )", Actions.go, 1)
        self.commands["go"] = go
        
        history = Command("history", " : enregistrer l'avancement", Actions.get_history, 0)
        self.commands["history"] = history
        back = Command("back", " :retour dans la pièce précédente", Actions.get_back, 1)
        self.commands["back"] = back

        #inventory =Command("inventory", " :affiche l'inventaire", Actions.inventory, 0)
        #self.commands["inventory"]=inventory

        take=Command("take", " :prends les items", Actions.take,0)
        self.commands["take"]=take
        drop=Command("drop", " :lâche l'item", Actions.drop, 0)
        self.commands["drop"]=drop
        check=Command("check", " :reflète les items présents dans l'inventaire du joeur", Actions.check, 0)
        self.commands["check"]=check
        look=Command("look"," :affiche les items présents dans cette pièce", Actions.look,0 )
        self.commands["look"]=look
        # inventaire=Command("inventaire", ": Qu'avons nous récupérer depuis le début de notre aventure ", Actions.inventory, 0)
        # self.commands["inventory"]=inventory
 
        # Setup rooms
       
        cave1 = Room("cave1", "en Cave1 Une pièce sombre, humide, avec un léger bruit d'eau gouttant.")
        self.room.append(cave1)
        cave2 = Room("cave2", "en Cave2 Vous rampez dans un tunnel dont les murs sont des pics qui vous empêchent de revenir en arrière.")
        self.room.append(cave2)
        cave3 = Room("cave3", "en Cave3 Un murmure étrange semble émaner des murs.")
        self.room.append(cave3)
        cave4 = Room("cave4", "en Cave4 Les quatre torches accrochées aux quatre coins de la pièce vous réchauffent le coeur.")
        self.room.append(cave4)
        cave5 = Room("cave5", "en Cave5 L'air devient plus frais, et un souffle de vent est perceptible.")
        self.room.append(cave5)
        cave6 = Room("cave6", "en Cave6 Au milieu de nulle part, vous tombez sur une grande armoire. Mais que fait-elle ici ?")
        self.room.append(cave6)
        cave7 = Room("cave7", "en Cave7 Vous sentez une odeur de soufre. Une chose est-elle en train de pourrir ?")
        self.room.append(cave7)
        cave8 = Room("cave8", "en Cave8 Un escalier étroit mène vers une pièce avec un tombeau ouvert.")
        self.room.append(cave8)


       
        #Setup inventory

        épée = Item("épée", "une épée au fil tranchant comme un rasoir", 10)
        self.item.append(épée)
        pieu = Item("pieu", "un pieu en bois plus piquant qu'un porc épic",2)
        self.item.append(pieu)
        torche = Item("torche", "une torche pour éclairer votre chemin",1)
        self.item.append(torche)
        bouclier = Item("bouclier", "un bouclier robuste et solide",5)
        self.item.append(bouclier)
        clé = Item("clé", "une clé mais pour ouvrir quoi ?", 1)
        self.item.append(clé)
        pince = ("pince à linge","une pince à linge qui pourrait couper la respiration de n'importe qui",1)
        self.item.append(pince)
        pierre = Item("pierre","une grosse pierre pour quoi faire ? Il n'y a personne à lapider...",3)
        self.item.append(pierre)

        # #pnj def 

        # archibald = Charactere("Archibald", "Il sera notre guide pendant toute l'aventure", cave1,["je suis arcchi"] ) 
        # """ 
        # Archibald est dans toutes les pièces , c'est notre conseiller.

        # """

        # cave1.pnj["archibald"]= archibald
        # cave2.pnj["archibald"]= archibald
        # cave3.pnj["archibald"]= archibald
        # cave4.pnj["archibald"]= archibald
        # cave5.pnj["archibald"]= archibald
        # cave6.pnj["archibald"]= archibald
        # cave7.pnj["archibald"]= archibald
        # cave8.pnj["archibald"]= archibald

        # """lancelot=Charactere("lancelot", " avez vous besoin d'une arme ?", cave1,["je suis lancelot"])
        # cave1.pnj["lancelot"]= lancelot

        # heiter=Charactere("heiter", "que dois-je taillé pour vous ? Je ne suis que menuisier ...",cave2,["je suis heiter"])
        # cave2.pnj["heiter"]= heiter

        # flame= Charactere("flame", " je suis la gardienne de ce feu, je ne vous serait pas d'une grande utilité, je ne peux vous donner qu'un peu de chaleur",cave4, ["je suis flame"])
        # cave4.pnj["flame"]=flame

        # ulfberht= Charactere( "ulfberht" ," je peux te fournir n'importe quelle arme et même des boucliers",cave6,["je suis ulfberht"])
        # cave6.pnj["ulfberht"]=ulfberht

        # phidias= Charactere( "phidias", "je suis tailleur de pierre pour le démon, je veux que vous le renversier c'est pourquoi je vius founi quelques rocher" , cave7,["je suis phidias"])
        # cave7.pnj["phidias"]=phidias

        # selyse= Charactere( "selyse","Puis-je vous aider ? Hélas, je n'ai que des pinces à linges pour vous... ",cave3,["je suis selyse"])
        # cave3.pnj["selyse"]=selyse"""


        # items def  

        épée = Item ("épée", " elle vous sera utile pour votre future aventure ! ", 10) 
        #cave1.inventory.add(épée)
        cave1.inventory["épée"]=épée

        pieu = Item ( "pieu" ," un pieu en bois plus piquant qu'un porc épic" , 2) 
        #cave2.inventory.add(pieu)
        cave2.inventory["pieu"]=pieu

        torche =Item ("torche","une torche pour éclairer votre chemin",1)
        #cave4.inventory.add(torche)
        cave4.inventory["torche"]=torche


        bouclier = Item ("bouclier","un bouclier robuste et solide",5)
        #cave6.inventory.add(bouclier)
        cave6.inventory["bouclier"]=bouclier

        clé = Item ("clé", "une clé mais pour ouvrir quoi ?", 1)
        #cave6.inventory.add(clé)
        cave6.inventory["clé"]=clé

        pince = Item ("pince", "une pince à linge qui pourrait couper la respiration de n'importe qui",1)
        #cave3.inventory.add(pince)
        cave3.inventory["pince"]=pince

        pierre = Item ("pierre", "une grosse pierre pour quoi faire ? Il n'y a personne à lapider...",3)
        #cave7.inventory.add(pierre)
        cave7.inventory["pierre"]=pierre

        #cave1.inventory.append(clef) 


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
    #     """ cette fonctionn a pour but de définir la manière dont les messages des PNJ sont affichés etc 
    #     Ex : 
    #     msg_char = A 
    #     press  SPACE 
    #     msg_char = B 
    #     press SPACE 
    #     msg _ char = C
    #     ...
    #     """
    #   """
    #     for event in pygame.event.get(): 
    #         if event.key == pygame.K_SPACE :
    #             game.action.talk_char()"""

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
            command.action(self,list_of_words, command.number_of_parameters)
        

        if command_word == "look":
            # call look method
            self.player.current_room.look()
            return

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())

"""
    def DEBUG(bool):
        if DEBUG is True : 
            print (DEBUG("DEBUG: message"))
        else :
            return Nothing"""






def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
