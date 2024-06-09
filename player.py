

class Player:
  players = list()
  def __init__(self) -> None:
    pass
  
  def _create_player(self, id: int):
    new_player = {
      'hand': list(),
      'id': id
    }
    return new_player
  
  def initialize_players(
    self,
    players_count,
  ):
    for player in range(players_count):
      add_player = self._create_player(player)
      self.players.append(add_player)
      
    return self.players
      