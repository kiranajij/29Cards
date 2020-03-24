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
    The card. Following the paradigm of `Everything is a Class`, I made the
    cards into their own class. It's a little bit incomplete in the sense that
    the API doesn't make any sense(for now).

    Every Card class contains a `Card.SUITES` and `Card.NUMBERS` that signifies
    a valid card. These variables are used for checking if a given number is a 
    valid card or for generating a deck of the cards.

    ? WORKS LEFT TO DO
    TODO: Write a documentation that actually makes sense
    """

    SUITES = ["H", "S", "D", "C"]   # The valid cards
    NUMBERS = [                     # The valid numbers
                "A", "2", "3", "4",
                "5", "6", "7", "8",
                "9", "10", "J", "Q",
                "K"
    ]

    def __init__(self, value):
        """
        Create a card object.
        * inputs:
        * value:
            This is the value of the card. for example Ace of Spades has
            the value `SA`. The first character denoting the suite of the
            card and the rest denoting the number (value) fo the card.
            ? The name `value` is a little ambiguous, can someone rename it?
            
        * returs:
            A Card object of the given value
        * raises:
            If the Card value is invalid, raises `CardException`
            
        To create a card, call the consructor with the value of card in the
        format - first character is the suite, and the rest is the value.
        the constructor first checks if it is a valid card, if yes then contunues
        otherwise it raises the exception CardException.
        """

        # check if the card is a valid card
        if not Card.check_valid(value):
            # if not raise the exception
            raise CardException(f"Invalid card exception: {value}")

        # Otherwise
        self.value = value
        self.suite = value[0]
        self.number = value[1]

    def get_suite(self):
        """
        Returns the suite of the card
        """
        return self.suite
    
    def get_number(self):
        """
        Returns the number of the card
        """
        return self.number
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"Card: <{self.value}>"
    
    @classmethod
    def check_valid(klass, val):
        """
        A very crucial method indeed.
        It checks if the card is a valid card for the given class.
        It determnes it by checking if the suite is the klass.SUITES
        and number is in klass.NUMBERS list. if not then it returns
        False.
        """

        suites = klass.SUITES       # Valid Suites
        numbers = klass.NUMBERS     # Valid numbers

        suite, number = val[0], val[1:]     # extract number and suite
        if suite in suites and number in numbers:
            return True
        else:
            return False
    
    @classmethod
    def get_deck(klass):
        """
        This method returns a deck containing all the valid cards of the
        klass. It is done by iterating over all the possible suites and
        numbers of klass and creating a card out of it. 
        """
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
    
    def __repr__(self):
        return f"Cards29<{self.value}"
    
    def __str__(self):
        return self.value
    
    # @staticmethod
    # def generate_deck():
    #     pass


