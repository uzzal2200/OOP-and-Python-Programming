# read only ---> you can not set the value. value can not be changed
# getter --> get a value of property.most of the time , you will get the value of a private attribute
# setter ---> set a value of property through a method.most of the time you will set value of a private attribute

class User:
    def __init__(self , name , age , money):
        self.name = name
        self._age = age
        self.__money = money
    # # getter without any setter is readonly attribute
    @property
    def age(self):
        return self._age
    # getter
    @property
    def salary(self):
        return self.__money
    # sette using
    @salary.setter
    def salary(self,value):
        if value < 0:
            return 'salary can not be negative'
        self.__money += value


    
samsu = User('kopa' , 21 ,12000)
# print(samsu.__money)
print(samsu.age)
#print(samsu.money)
print(samsu.salary)
samsu.salary = 1000
print(samsu.salary)
