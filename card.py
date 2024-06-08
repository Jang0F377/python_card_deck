class Card:
  def __init__(self) -> None:
    pass
  
  def create_card(self, suit, value, card_suits, card_values):
    card = dict()
    suit_str = str(card_suits[f'{suit}'])
    value_str = str(card_values[f'{value}'])
    full_name = self._return_full_name(suit_str, value_str)
    full_value = self._determine_value(suit, value)
    card = {
      'suit': suit,
      'rank': value,
      'suit_str': suit_str,
      'rank_str': value_str,
      'full_name': full_name,
      'comparable_value': full_value
    }
    return card
    
    
  def _return_full_name(self, suit, value):
    return f"{value} of {suit}"
  
    
  def _determine_value(self, suit, value):
    suit_value: int
    rank_value: int
    
    if suit == 'D':
      suit_value = 1
    elif suit == 'C':
      suit_value = 2
    elif suit == 'H':
      suit_value = 3
    else:
      suit_value = 4
      
      
    if value == '2':
      rank_value = 14  
    elif value == 'J':
      rank_value = 10
    elif value == 'Q':
      rank_value = 11
    elif value == 'K':
      rank_value = 12
    elif value == 'A':
      rank_value = 13
    else:
      rank_value = int(value) - 1
      
    return (rank_value, suit_value)