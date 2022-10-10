class Player:
    def __init__(self, name):
        self._name = str(name)
        self._hp = 100
        self._mp = 100
        self._level = 0
        self._xp = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self.name = new_name

    def __str__(self):
        return f"NAME: {self._name}\n\tLEVEL: {self._level}\n\tEXP: {self._xp}\n\tHP: {self._hp}\n\tMP: {self._mp},    "


jogador = Player("Lucas")
print(jogador)
