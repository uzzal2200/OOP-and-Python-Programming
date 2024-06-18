class phone:
    # class atribute
    manufature='china'
    # constructor
    def __init__(self,owner,brand,price):
         # pass means kono kiso na likhle ata likhte hobe 
        self.owner=owner
        self.brand=brand
        self.price=price
# method
    def send(self,phn,sms):
        text=f'sending to {phn} and {sms}'
        print(text)

my_phone=phone('kala chan','oppo',9800)
print(my_phone.owner,my_phone.brand,my_phone.price)


##########################################################
# A Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)


p = Person('Nikhil')
p.say_hi()
