class Player:
    def __init__(self, name):
        self._name = str(name)
        self._classe = "classless"
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
        return f"NAME: {self._name}\n\tLEVEL: {self._level}\n\tCLASS: {self._classe}\n\tEXP: {self._xp}\n\tHP: {self._hp}\n\tMP: {self._mp}\n"

    def player_data(self):
        return print(f"NAME: {self._name}\n\tLEVEL: {self._level}\n\tCLASS: {self._classe}\n\tEXP: {self._xp}\n\tHP: {self._hp}\n\tMP: {self._mp}\n")

    def set_char_class(self, class_number):

        try:
            if int(class_number) >= 0 or int(class_number) <= 4:
                if int(class_number) == 0:
                    self._classe = "Bard"
                    self._hp = 80
                    self._mp = 150
                elif int(class_number) == 1:
                    self._classe = "Barbarian"
                    self._hp = 200
                    self._mp = 60
                elif int(class_number) == 2:
                    self._classe = "Rogue"
                    self._hp = 50
                    self._mp = 50
                elif int(class_number) == 3:
                    self._classe = "Warrior"
                    self._hp = 120
                    self._mp = 50
                elif int(class_number) == 4:
                    self._classe = "Mage"
                    self._hp = 80
                    self._mp = 200

        except:
            print("Invalid command")


jogador = Player()
