from math import pi
class Shape:
    def __init__(self,name) -> None:
        self.name = name

class Recntangle(Shape):
    def __init__(self, name,lenght , width) -> None:
        self.length = lenght
        self.width = width
        super().__init__(name)
    def area(self):

        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name , radius) -> None:
        self.radius = radius
        super().__init__(name)
    
        super().__init__(name)
    def area(self):
        return pi * self.radius * self.radius