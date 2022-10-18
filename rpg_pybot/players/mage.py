from players.player import Player


class Mage(Player):
    def __init__(self, name):
        super().__init__(name)
        self._classe = "Mage"
        self._hp = 80
        self._mp = 200
        self._df = 1
        self._atk = 6
        self._level = 1
        self._xp = 0
        self.special_attack = "Fire Ball" 
