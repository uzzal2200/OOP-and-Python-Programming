class Product:
    def __init__(self):
        self.product = []

class Shop(Product):
    def __init__(self) -> None:
        super().__init__()
    def add_product(self, item):
        self.product.append(item)
    def product_list(self):
        print(self.product)
   
    def buy_product(self,item):
        if item in self.product:
            print('Congrats')
        else:
            print('sorry: this is currently unavilable')
    

my_shop = Shop()
my_shop.add_product("T shirt")
my_shop.add_product("Pent")
my_shop.add_product("shirt")
my_shop.add_product("panjabai")
my_shop.add_product("short pent")

my_shop.buy_product('short pent')
my_shop.buy_product('borka')
