import random

from models.card import Card
from models.suit import Suit

deck_suits = [Suit("Hearts", "♥"), Suit("Diamonds", "♦"), Suit("Clubs", "♣"), Suit("Spades", "♠")]
deck_ranks = list(range(2,15))

class CardStack:
    def __init__(self, suits: list[Suit] = deck_suits, ranks: list[int] = deck_ranks):
        self.stack = []
        for suit in suits:
            for rank in ranks:
                self.stack.append(Card(suit, rank))

    def __str__(self):
        results = []
        for card in self.stack:
            results.append(str(card))
        
        return "\n".join(results)
    
    def display_rows(self, rows: int):
        results = []
        row_size = (len(self.stack) + rows - 1) // rows

        for row in range(rows):
            row_cards = self.stack[(row * row_size): (row * row_size + row_size)]

            results.append(" ".join(str(card) for card in row_cards))
        
        return '\n'.join(results)
    
    def __len__(self):
        return len(self.stack)

    def shuffle(self):
        random.shuffle(self.stack)

    def pop(self):
        return self.stack.pop()

    def append(self, card: Card):
        self.stack.append(card)