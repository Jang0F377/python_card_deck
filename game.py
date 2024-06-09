from deck import Deck
from player import Player
from typing import List

class Game:
  PLAYER_COUNT = 4
  
  def __init__(self, deck, players) -> None:
    self.deck: List[Deck]  = deck
    self.players: List[Player] = players
    
  
  def start_game(self) -> None:
    self.players = self.players.initialize_players(self.PLAYER_COUNT)
    self.deck = self.deck.initialize_deck()
    self._pass_out_cards()
    
  def _pass_out_cards(
    self,
  ):
    cards_per_player = int(len(self.deck) / self.PLAYER_COUNT)
    
    for x in range(cards_per_player):
      for player in self.players:
        player['hand'].append(self.deck.pop())
    
    print(self.players)