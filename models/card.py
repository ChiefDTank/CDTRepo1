from models.suit import Suit

class Card:
    def __init__(self, suit: Suit, rank: int):
        self.suit = suit
        self.rank = rank
    
    def display_rank(rank: int):
        if rank >= 2 and rank <= 9:
            return " " + str(rank)
        elif rank == 10:
            return rank
        elif rank == 11:
            return ' J'
        elif rank == 12:
            return ' Q'
        elif rank == 13:
            return ' K'
        elif rank == 14:
            return ' A' 
    
    def __str__(self):
        return f"{Card.display_rank(self.rank)}{self.suit}"