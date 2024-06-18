class Family:
    def __init__(self, adress) -> None:
        self.adress = adress
class Scholl:
    def __init(self , id , level):
        self.id = id
        self.level = level

class Sports:
    def __init__(self , game):
        self.game = game
class Student(Family , Sports):
    def __init__(self, adress , id , level , game) -> None:
        super().__init__(adress)
        Scholl.__init__(self , id , level , game)
        Sports.__init__(self , game)
        Family.__init__(self , adress)