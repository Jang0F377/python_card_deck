from card_constants import *
from card import Card
import random


class Deck:
  card_values = CARD_VALUES
  card_suits = CARD_SUITS
  cards: list
  playersCount = 4
  def __init__(self, card):
    self.card: Card = card
    
  def initialize_deck(self):
    self.cards = self._create_deck(self.card)
    
    self._shuffle_deck(self.cards)
    
    return self.cards
    
  def _create_deck(self, card):
    deck = list()
    created_card: dict
    
    for suit in self.card_suits:
      for value in self.card_values:
        created_card = self.card.create_card(
          suit,
          value,
          self.card_suits,
          self.card_values
        )
        deck.append(created_card)
        
    return deck
  
  def _shuffle_deck(self, deck):
    return random.shuffle(deck)