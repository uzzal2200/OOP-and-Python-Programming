# abstract base class
from abc import ABC, abstractmethod
class Animal:
    @abstractmethod # enforce all derived class to hace a eat method
    def eat(self):
        print('the dog is eating')

    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.catagory = 'Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print('hey na nana , I am eatin banana')
    def move(self):
        print('hanging on the braches')
layka = Monkey('lucky')
layka.eat()
layka.move()
