from card import Card
from deck import Deck
from game import Game
from player import Player

if __name__ == '__main__':
  player = Player()
  card = Card()
  deck = Deck(card)
  game = Game(deck, player)
  game.start_game()
  pass