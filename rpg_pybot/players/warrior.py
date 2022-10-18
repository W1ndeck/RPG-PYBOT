from players.player import Player


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name)
        self._classe = "Warrior"
        self._hp = 120
        self._mp = 60
        self._df = 5
        self._atk = 5
        self._level = 1
        self._xp = 0
        self.special_attack = "Sword Stroke" 