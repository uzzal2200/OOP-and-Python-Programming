class shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
    def add(self,item,price,quantity):
        product={'item': item, 'price' : price, 'quantity' : quantity}
        self.cart.append(product)
    def check(self,amount):
        total = 0
        for item in self.cart:
            print(item)
            total = total + item['price'] * item['quantity']
            print('total price',total)
            if(amount < total):
                print(f'please provide {total - amount} more ')
            else:
                extra = amount - total
                print(f'Here is your items and extra money : {extra}')


uzzal = shopping('uzzal shopping e jao')
uzzal.add('alo', 60 , 4)
uzzal.add('dim', 10 , 12)
uzzal.add('alo', 50 , 5)
print(uzzal.cart)
uzzal.check(600)