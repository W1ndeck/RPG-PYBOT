from players.player import Player


class Rogue(Player):
    def __init__(self, name):
        super().__init__(name)
        self._classe = "Rogue"
        self._hp = 50
        self._mp = 50
        self._df = 1
        self._atk = 10
        self._level = 1
        self._xp = 0
        self.special_attack = "Stealth Attack" 