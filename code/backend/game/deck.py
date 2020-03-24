import game
from random import shuffle
from itertools import product
import cards



class Deck(game.GameBase):
    def __init__(self, deck=None):
        if not deck is None:
            try:
                temp = deck[0]
                if not isinstance(temp, cards.Card):
                    raise TyperError("Not a valid card type")
            except IndexError:
                pass
            else:
            self.deck = deck
        else:
            self.deck = Deck.get_new_deck()
    
    def shuffle_cards(self, n=1):
        for i in range(n):
            shuffle(self.deck)
    
    def pop_n(self, n=0):
        for i in range(n):
            yield self.deck.pop(0)
        
    def pop(self):
        return self.deck.pop(0)

    def cards_left(self):
        return len(self.deck)

    @staticmethod
    def get_new_deck():
        """
        Returns a deck of cards 
        """
        pass

if __name__ == "__main__":
    deck = Deck.get_deck()
    print(deck, flush=True)