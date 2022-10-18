from players.player import Player


class Barbarian(Player):
    def __init__(self, name):
        super().__init__(name)
        self._classe = "Barbarian"
        self._hp = 200
        self._mp = 60
        self._df = 8
        self._atk = 4
        self._level = 1
        self._xp = 0
        self.special_attack = "Bersek Assault" 