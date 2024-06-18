# static attribute (class attribute)
# static mehtod @staticmethod 
# class method @classmehtod
# difference between static method and class method
class Shopping:
    cart = [] # class attribute # static attribute
    orgin = 'china'
    def __init__(self , name , location):
        self.name = name # instance attribute
        self.location = location
    def purchase(self , item , price , amount):
        remaining = amount - price
        print(f'buying : {item} for price : {price} amd remaining : {remaining}')
    @classmethod
    def show(self,item):
        print(self.name)
        print('goragori not kinakini',item)
    @staticmethod
    def multiply(a,b):
        result= a*b
        print(result)

    
basundara = Shopping('baundara','dhaka')
#basundara.purchase('longi' , 500, 1000)
basundara.show('longi')
Shopping.show('longi')
Shopping.multiply(4,5) # static method
basundara.multiply(5,7)