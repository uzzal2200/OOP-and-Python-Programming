class Person:
    def __init__(self , name , age , height , weight):
        self.name = name 
        self.age = age 
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat mangso polao komra')
    def excercise(self):
        raise NotImplementedError
class Cricketer(Person):
    def __init__(self, name, age, height, weight,team):
        self.team = team 
        super().__init__(name, age, height, weight)
        # function override
    def eat(self):
        print('vegetables')
    def excercise(self):
        print('giye giye excercise kore')
    # + singn operator overload
    def __add__(self , other):
        return self.age + other.age
    # * singn operator overload
    def __mul__(self , other):
        return self.weight * other.weight
    # len  overload
    def __len__(self):
        return self.height
    # operator over load
    def __gt__(self,other):
        return self.age > other.age

shakib = Cricketer('shakib', 23, 45 , 60 , 'BD')
shakib.eat()
shakib.excercise()
mushfiq = Cricketer('moshfiq' , 34 , 65 , 63, 'BD')
print(shakib + mushfiq)
print(shakib * mushfiq)
print(len(shakib))
print(shakib > mushfiq)
# plus sign overload 
print(34 + 6)
print('uzzal' + 'noman')
print([12,3,4] + [2,3,4,5])