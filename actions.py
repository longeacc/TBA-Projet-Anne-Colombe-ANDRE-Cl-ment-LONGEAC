"""
Classe actions pas vraiment écrite comme telle
"""
#Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.
# The error message is stored in the MSG0/MSG1 variables, formatted with the command_word variable.
# The MSG0 variable is used when the command does not take any parameter.
# The MSG1 variable is used when the command takes 1 parameter.
MSG0 = "\nLa commande {command_word} ne prend pas de paramètre.\n"
MSG1 = "\nLa commande {command_word} prend 1 seul paramètre.\n"


class Actions:

    """
    Class Actions qui regroupe toutes les actions du jeu
    """
    @staticmethod
    def go(game, list_of_words):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, P).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """

        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.

        if l <2:
            return False

        #get the direction from the list
        direction = list_of_words[1]
        #move the player to the specific direction
        player.move(direction)
        return True

    @staticmethod
    def get_back(game, list_of_words):
        """Permet de retourner dans la pièce précédente.

        Args:
            game (Game): L'objet jeu.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendu pour la commande.

        Returns:
            bool: True si la commande a été exécutée correctement, False sinon.
        """
        player = game.player

        # Retourner dans la pièce précédente
        if not player.history:
            print("\nVous n'avez pas visité d'autres pièces.")
        else:
            previous_room = player.history.pop()
            player.current_room = previous_room
            print(f"\nVous êtes retourné dans la pièce précédente : {previous_room.name}\n")


            # Historique mis à jour
            history_names = ",".join(room.name for room in player.history)
            print(f"Historique des pièces visitées : {history_names}\n")

            # Affichage des sorties disponibles
            #sert à vérifier la présence de l'attribut
            if hasattr(previous_room, 'exits') and previous_room.exits:
                exits = [direction for direction, room in previous_room.exits.items()]
                exits_display = ", ".join(exits) if exits else "aucune direction disponible"
                print(f"Sorties disponibles depuis {previous_room.name} : {exits_display}\n")
            else:
                print("Les infos sur les sorties ne sont pas disponibles pour cette pièce.\n")

        return True

    @staticmethod
    def quit(game, list_of_words):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    @staticmethod
    def get_history(game,list_of_words):
        """
        allows to show up the previosu visited rooms 
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
           
        Returns:
            bool: True if the command was executed successfully, False otherwise.
            
        """
        player = game.player

        # Afficher l'historique des pièces visitées
        if player.history:
            print("\nHistorique des pièces visitées :\n")
            for room in player.history:
                print(f"- {room.name} : {room.get_long_description()}\n")
        else:
            print("\nVous n'avez pas encore visité de pièce.")
        return True

    @staticmethod
    def check(game, list_of_words):
        """
        Display the player's inventory.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """

        # Affiche l'inventaire du joueur
        player = game.player
        if player.inventory:
            print("\nVotre inventaire contient :")
            player.get_inventory()
        else:
            print("\nVotre inventaire est vide.")
        return True

    @staticmethod
    def look(game,list_of_words):

        """
        allows to have a look on a room inventory

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        """
        # Afficher la description de la pièce actuelle
        player = game.player
        current_room = player.current_room
        print(current_room.get_long_description())

        # Vérifier et afficher les objets dans la pièce
        if current_room.inventory:
            print("\nVous voyez les objets suivants :")
            print(current_room.get_inventory())
        else:
            print("\nIl n'y a aucun objet ici.")
        return True

    @staticmethod
    def take(game,list_of_words):
        """
        Take an objet from the inventory of a room and add it into the inventory of the player.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        """
        player = game.player
        current_room = player.current_room

        # Récupérer le nom de l'objet à prendre
        item_name = list_of_words[1]

        # Vérifier si l'objet est dans la pièce
        #get_inventory me renvoie un str
        if item_name in current_room.inventory:
            # Ajouter l'objet à l'inventaire du joueur
            player.inventory[item_name] = current_room.inventory[item_name]
            # Retirer l'objet de la pièce
            del current_room.inventory[item_name]

            print(f"\nVous avez pris {item_name} et l'avez ajouté à votre inventaire.")
            return True

        print(f"\nL'objet '{item_name}' n'est pas présent dans cette pièce.")
        return False

    @staticmethod
    def drop(game,list_of_words):
        """
        allows to drop an objet from the player inventory to the inventory of the room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """

        player = game.player
        current_room = player.current_room

        # Récupérer le nom de l'objet à prendre
        item_name = list_of_words[1]

        # Vérifier si l'objet est dans la pièce
        #get_inventory me renvoie un str
        if item_name in player.inventory:
            # Ajouter l'objet à l'inventaire du joueur
            current_room.inventory[item_name] = player.inventory[item_name]
            # Retirer l'objet de la pièce
            del player.inventory[item_name]

            print(f"\nVous avez laissé {item_name} dans la pièce")
            return True

        print(f"\nVous n'avez pas {item_name} dans votre inventaire")
        return False

    @staticmethod
    def talk(game,list_of_words):
        """
        Permet au joueur de parler à un PNJ dans la salle actuelle.

        Args:
        game (Game): Instance du jeu en cours.
        character_name (str): Nom du personnage avec lequel parler.

        Returns:
        None
        """
        player = game.player
        current_room = player.current_room

        # Récupérer le nom de l'objet à prendre
        character_name = list_of_words[1]

        player = game.player

        #Vérifie si le PNJ existe dans la salle actuelle
        if character_name in player.current_room.pnj:
            print(player.current_room.pnj[character_name].get_msg())
            return True
        else:
            print(f"Il n'y a pas de personnage nommé {character_name} ici.")
            return False

    @staticmethod
    def attack(game, list_of_words):
        player = game.player
        current_room = player.current_room

        #si le joueur ne possède pas tous les items alors il perd
        if len(player.inventory) < 7:
            print(f"\n {player.name} vient de mourrir")
            game.finished =True
        #si le joueur possède tous les items alors il gagne
        else:
            print(f"\n {player.name} a tué Lucifer")
            game.finished = True