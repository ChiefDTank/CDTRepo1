from models.cardstack import CardStack
from models.card import Card

class Player:
    def __init__ (self, name: str):
        self.name = name
        self.cards = CardStack([],[])

    def __str__ (self):
        if (len(self.cards)):
            return f"{self.name}: {" ".join(str(card) for card in self.cards.stack)}"
        else:
            return f"{self.name} has no cards"
        
    def deal(self, card: Card):
        self.cards.append(card)