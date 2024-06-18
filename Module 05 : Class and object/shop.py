class Shop:
    cart=[]
    def __init__(self,buyer):
        self.buyer = buyer
    def add_to_cart(self,item):
        self.cart.append(item)
uzzal = Shop('uzzal shoping jabe')
uzzal.add_to_cart('shoes')
uzzal.add_to_cart('half pent')
print(uzzal.cart)
nisho = Shop('nisho')
nisho.add_to_cart('longi')
nisho.add_to_cart('watch')
print(nisho.cart)

