class shop:
    shopingmall = 'jumuna park' # class atribute 
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] # instance attribute
    def add(self,item):
        self.cart.append(item)
    
uzzal = shop('kiso kibo')
uzzal.add('patija longi')
uzzal.add('akta short pent')
print(uzzal.cart)
prio = shop('shoping giye foska khao')
prio.add('shari')
prio.add('lipistic')
print(prio.cart)
noman = shop('meye dekhe goro shopin kora vad diye')
noman.add('shirt')
noman.add('half pent')
print(noman.cart)

def call():
    print('calling someone i dont know')
    return 'call done'


class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']


    def call(self):
        print('calling someone i know')



my_phone = Phone()
call()