from models.game import Game
from models.cardstack import CardStack
from models.player import Player

def buildDeck():
    deck = CardStack()
    deck.shuffle()
    return deck

def generatePlayers():
    players = [Player("Binky"), Player("Jack Magic"), Player("Ben P."), Player("Frank Reynolds"), Player ("Dark Walph")]
    return players

def playGame():
    game = Game(buildDeck(), generatePlayers())

    print(game)

    game.deal_cards(2)

    print(game)

if __name__ == "__main__":
    playGame()