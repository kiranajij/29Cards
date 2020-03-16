import random
from exceptions import *

"""
This is the module that contains all the required functionality
to start a 29 cards game.
"""

class GameBase:
    """
    # GameBase
    This is the base for all game object. This is done to keep
    things simple
    """
    pass


class Player(GameBase):
    def __init__(self, name):
        self.name = name

class Game:
    def __init__(self, id):
        self.id = id

        self.players = {
            0: None,
            1: None,
            2: None,
            3: None
        }

    def add_player(self, player, n):
        if not isinstance(player, Player):
            raise PlayerTypeError("Player must be of type Player!")

        