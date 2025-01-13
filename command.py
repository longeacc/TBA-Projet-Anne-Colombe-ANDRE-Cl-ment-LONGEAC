"""This file contains the Command class."""

class Command:
    """
    This class represents a command. A command is composed of 
    a command word, a help string, an action and a number of parameters.

    Attributes:
        command_word (str): The command word.
        help_string (str): The help string.
        action (function): The action to execute when the command is called.
        number_of_parameters (int): The number of parameters expected by the command.

    Methods:
        __init__(self, command_word, help_string, action, number_of_parameters) : The constructor.
        __str__(self) : The string representation of the command.

    Examples:

    >>> from actions import go
    >>> command = Command("go", "Permet de se déplacer dans une direction.", go, 1)
    >>> command.command_word
    'go'
    >>> command.help_string
    'Permet de se déplacer dans une direction.'
    >>> type(command.action)
    <class 'function'>
    >>> command.number_of_parameters
    1

    """

    # The constructor.
    def __init__(self, command_word, help_string, action):
        self.command_word = command_word
        self.help_string = help_string
        self.action = action


    # The string representation of the command.
    def __str__(self):
        """
        Returns a string representation of the command, combining the command word and help string.

        Returns:
            str: A formatted string displaying the command word and its description.
        """
        return f"{self.command_word}: {self:help_string}"