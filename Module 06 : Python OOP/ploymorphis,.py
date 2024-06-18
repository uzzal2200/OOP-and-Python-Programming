# poly --> many , multiple 
# morph --> shape
class Animal:
    def __init__(self , name) -> None:
        self.name = name

    def make_sound(self):
        print('Animal making some sound')
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('meow meow ')
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('gheu gheu')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('beh beh beh ')


   
cat = Cat('real cat')
dog = Dog('real dog')
dog.make_sound()
cat.make_sound()
mess = Goat('LM')
mess.make_sound()
less = Goat('Gora gora')

animals = [cat , dog , mess,less]
for animal in animals:
    animal.make_sound()