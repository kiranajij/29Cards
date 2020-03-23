from exceptions import *
import game
from itertools import product
import deck


class CardBase(game.GameBase):
    """
    Base class for cards and deck 
    """
    pass


class Card(CardBase):
    """
    # Card
    ---
    The card.
    """
    SUITES = ["H", "S", "D", "C"]
    NUMBERS = [
                "A", "2", "3", "4",
                "5", "6", "7", "8",
                "9", "10", "J", "Q",
                "K"
    ]

    def __init__(self, value):
        if not Card.check_valid(value):
            raise CardException(f"Invalid card exception: {value}")

        self.value = value
        self.suite = value[0]
        self.number = value[1]

    def get_suite(self):
        return self.suite
    
    def get_number(self):
        return self.number
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"Card: <{self.value}>"
    
    @classmethod
    def check_valid(klass, val):
        suites = klass.SUITES
        numbers = klass.NUMBERS

        suite, number = val[0], val[1:]
        if suite in suites and number in numbers:
            return True
        else:
            return False
    
    @classmethod
    def get_deck(klass):
        suites = klass.SUITES
        nums = klass.NUMBERS

        cards = []

        for suite, n in product(suites, nums):
            val = suite+n
            # print(val)
            card = klass(suite+n)
            cards.append(card)
        
        return deck.Deck(cards)


class Card29(Card):

    SUITES = ["D", "S", "H", "C"]
    NUMBERS = ["A", "7", "8", "9", "10", "J", "K", "Q"]
    POINTS = {
        "A": 1, "7": 0, "8": 0
    }

    def __init__(self, value):
        
        if not Card29.check_valid(value):
            raise CardException(f"Invalid card exception: {value}")
            
        self.value = value
    
    def get_point(self):
        return self.points

    # @staticmethod
    # def check_valid(value):
    #     suites = Card29.SUITES
    #     numbers = Card29.NUMBERS

    #     suite, number = value[0], value[1:]

    #     if suite in suites and number in numbers:
    #         return True
    #     return False
    
    @staticmethod
    def card_point(value):
        if not Card29.check_valid(value):
            return
        suite, number = list(value)
    
    # @staticmethod
    # def generate_deck():
    #     pass


