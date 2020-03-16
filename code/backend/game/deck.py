from game import GameBase
from random import shuffle


class Deck(GameBase):
    def __init__(self):
        self.deck = [ i+j for i in ("S", "H", "D", "") for
               j in ("1", "7", "8", "9", "10", "K", "Q", "J") ]