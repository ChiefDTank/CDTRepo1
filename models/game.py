from models.cardstack import CardStack
from models.player import Player

class Game:
    def __init__(self, deck: CardStack, players: list[Player]):
        self.deck = deck
        self.players = players
        self.current_player_turn = 0

    def __str__(self):
        result = []
        result.append(self.deck.display_rows(6))
        
        result.append("Players:")
        for player in self.players:
            result.append(str(player))

        return "\n".join(result)
    
    def deal_cards(self, number: int):
        for _ in range(number):
            for player in self.players:
                player.deal(self.deck.pop()) 
            
