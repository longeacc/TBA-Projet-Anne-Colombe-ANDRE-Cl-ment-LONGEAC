""" Classe principale : Game.

Description :La classe Game articule toutes les classes entre elles(création des salles, 
des objets, des commandes et le joueur... 
"""
# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
DEBUG = False

class Game:
    """ 
    Elle définit les principales méthodes nécessaires pour configurer le jeu.

    Attributs :
        finished (bool) : Indique si le jeu est terminé.
        room (list[Room]) : Liste des salles disponibles dans le jeu.
        commands (dict) : Dictionnaire des commandes disponibles, associées à leurs actions.
        player (Player) : Objet représentant le joueur.
        item (list[Item]) : Liste des objets disponibles dans le jeu.
    """

    # Define the Constructor
    def __init__(self):
        self.finished = False
        self.room = []
        self.commands = {}
        self.player = None
        self.item = []
        self.pnj={}
        self.DEBUG = True

    # Setup the game
    def setup(self):
        """  
        Configure les éléments du jeu :
            - Ajout des commandes disponibles.
            - Création des salles et définition de leurs sorties.
            - Création et emplacement des objets dans les salles.
        """

        help = Command("help", " : afficher cette aide", Actions.help)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une \
        direction cardinale (N, E, S, O, U, D, n, e, s, o, u, d, NORD, \
        EST, SUD, OUEST, UP, DOWN, Nord, Est, Sud, Ouest,\
        Up, Down, nord, est, sud, ouest, up, down )", Actions.go)
        self.commands["go"] = go

        history = Command("history", " : enregistrer l'avancement", Actions.get_history)
        self.commands["history"] = history
        back = Command("back", " :retour dans la pièce précédente", Actions.get_back)
        self.commands["back"] = back

        take=Command("take", " :prends les items", Actions.take)
        self.commands["take"]=take
        drop=Command("drop"," :lâche l'item",Actions.drop)
        self.commands["drop"]=drop
        check=Command("check",":reflète les items présents dans l'inventaire du joeur",
        Actions.check)
        self.commands["check"]=check
        look=Command("look"," :affiche les items\
        présents dans cette pièce",Actions.look)
        self.commands["look"]=look
        talk = Command("talk", ": possibilité de parler avec un PNJ", Actions.talk)
        self.commands["talk"] = talk

        attack = Command("attack", ": attaquer le monstre", Actions.attack)
        self.commands["attack"] = attack


        #Setup rooms

        cave1 = Room("cave1", "en Cave1 Une pièce sombre, humide," +
        " avec un léger bruit d'eau gouttant.")
        self.room.append(cave1)
        cave2 = Room("cave2", "en Cave2 Vous rampez dans un tunnel" +
        " dont les murs sont des pics qui vous empêchent de revenir en arrière.")
        self.room.append(cave2)
        cave3 = Room("cave3", "en Cave3 Un murmure" +
        " étrange semble émaner des murs.")
        self.room.append(cave3)
        cave4 = Room("cave4", "en Cave4 Les quatre torches accrochées" +
        " aux quatre coins de la pièce vous réchauffent le coeur.")
        self.room.append(cave4)
        cave5 = Room("cave5", "en Cave5 L'air devient plus frais," +
        " et un souffle de vent est perceptible.")
        self.room.append(cave5)
        cave6 = Room("cave6", "en Cave6 Au milieu de nulle part," +
        " vous tombez sur une grande armoire. Mais que fait-elle ici ?")
        self.room.append(cave6)
        cave7 = Room("cave7", "en Cave7 Vous sentez une odeur de soufre." +
        " Une chose est-elle en train de pourrir ?")
        self.room.append(cave7)
        cave8 = Room("cave8", "en Cave8 Un escalier étroit mène" +
        " vers une pièce avec un tombeau ouvert.")
        self.room.append(cave8)

        #def monster
        lucifer=Character("lucifer", "prêt à mourrir?", ["je suis lucifer", "ton heure est venue"])
        lucifer.current_room = cave8
        cave8.pnj["lucifer"]=lucifer

        #def pnj
        lancelot=Character("lancelot", " avez vous besoin d'une arme ?",
        ["je suis lancelot","tu es bête ou quoi je viens de te dire"])
        lancelot.current_room = cave1
        cave1.pnj["lancelot"]= lancelot

        heiter=Character("heiter", "Je travaille le bois",
        ["je suis heiter","Que dois-je taillé pour vous ? Je ne suis que menuisier ..."])
        heiter.current_room = cave2
        cave2.pnj["heiter"]= heiter

        flame= Character("flame", " vous avez froid?",
        ["je suis flame","Je suis la gardienne de ce feu, je ne vous serait" +
        "pas d'une grande utilité, je ne peux vous donner qu'un peu de chaleur"])
        flame.current_room = cave4
        cave4.pnj["flame"]=flame

        ulfberht= Character( "ulfberht" ," Je suis très demandé vous savez",
        ["Je suis ulfberht","Je peux te fournir n'importe quelle arme et même des boucliers"])
        ulfberht.current_room = cave6
        cave6.pnj["ulfberht"]=ulfberht

        phidias= Character( "phidias", "Un simple esclave" ,
        ["Je suis phidias","Je suis tailleur de pierre pour le démon,"+
        "il me garde en tant qu'esclave. Aider moi à retrouver ma liberté..."])
        phidias.current_room = cave7
        cave7.pnj["phidias"]=phidias

        selyse= Character("selyse", "C'est une petite entreprise familiale",
        ["Je suis selyse","Puis-je vous aider ? Hélas, je ne possède que des pinces à linges... "])
        selyse.current_room = cave3
        cave3.pnj["selyse"]=selyse


        # items def

        epee = Item ("epee", " elle vous sera utile pour votre future aventure ! ", 10)
        cave1.inventory["epee"]=epee

        pieu = Item ( "pieu" ," un pieu en bois plus piquant qu'un porc épic" , 2)
        cave2.inventory["pieu"]=pieu

        torche =Item ("torche","une torche pour éclairer votre chemin",1)
        cave4.inventory["torche"]=torche

        bouclier = Item ("bouclier","un bouclier robuste et solide",5)
        cave6.inventory["bouclier"]=bouclier

        cle = Item ("cle", "une cle mais pour ouvrir quoi ?", 1)
        cave5.inventory["cle"]=cle

        pince = Item ("pince", "une pince à linge pour couper la respiration de n'importe qui",1)
        cave3.inventory["pince"]=pince

        pierre = Item ("pierre", "une grosse pierre pourquoi? Il n'y a personne à lapider...",3)
        cave7.inventory["pierre"]=pierre



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



    #Play the game
    def play(self):
        """cette fonction défini l'ouverture du jeu"""
        self.setup()
        self.print_welcome()

        # Loop until the game is finished
        while not self.finished:
            #ask fo the payer's command
            command_string = input("> ")
            # Process the command (déplacer les PNJs uniquement si nécessaire)
            self.process_command(command_string)

            # Si le joueur change de salle (commande 'go' + direction valide), déplacer les PNJs
            if command_string.startswith("go") and self.DIRECTION_MAP.get(command_string.split()[1]) is not None:
                moved_pnjs = []
                # Déplacer les PNJs
                for room in self.room:
                    for pnj in list(room.pnj.values()):
                        if pnj not in moved_pnjs:
                            if pnj.move():
                                moved_pnjs.append(pnj)
                                if self.DEBUG:  # Vérifie si le débogage est activé
                                    print(f"Le PNJ {pnj.name} s'est déplacé dans : {pnj.current_room.name}")
                            else:
                                if self.DEBUG:  # Vérifie si le débogage est activé
                                    print(f"Le PNJ {pnj.name} est resté dans : {pnj.current_room.name}")

    # Process the command entered by the player (commande vide)
    def process_command(self, command_string) -> None:
        """
        cette fonction a pour but de donner 
        les commandes de base pour jouer

        Args :
            command_string (str) : La commande saisie par le joueur.
        """

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
                print(f"\nDirection '{normalized_direction}' n'est pas une direction\
                 valide. La liste de commande disponible est: N, E, S, O, U, D, n, e,\
                s, o, u, d, NORD, EST, SUD, OUEST, UP, DOWN, Nord, Est, Sud, Ouest,\
                 Up, Down, nord, est, sud, ouest, up, down.\n")
                return #Nothing happends

            #list_of_words[1] = normalized_direction
            normalized_direction = self.DIRECTION_MAP.get(direction, direction)
            list_of_words[1] = normalized_direction




        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue.\
            Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self,list_of_words)

        if command_word == "look":
            # call look method
            self.player.current_room.look()
            return

    # Print the welcome message
    def print_welcome(self):
        """
        cette fonction affiche bienvenue lors du lancement
        du jeu et donne les instructions d'aide si besoin
        """
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())


def main():
    """ Create a game object and play the game"""
    Game().play()


if __name__ == "__main__":
    main()