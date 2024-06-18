
from Menu import Pizza, Burger, Drinks, Menu
from Resturant import Restaurant
from user import Chef,Customer,Server, Manger
from order import Order

def main():
    menu = Menu()
    pizza_1 =Pizza('shotki pizza', 600, 'large',['shotki','onion'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 =Pizza('Alur pizza', 400, 'large',['potato','onion','oil'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3 =Pizza('Dal pizza', 500, 'large',['dal','oil'])
    menu.add_menu_item('pizza',pizza_3)

 # add burger to the menu

    burger_1 =Burger('nage Burger',1000,'chiken',['bread','chili'])
    menu.add_menu_item('burger',burger_1)
    burger_2 =Burger('beaf Burger',1200,'beef',['goro','haddi'])
    menu.add_menu_item('burger',burger_2)

# add drink to the menu
    coke = Drinks('Coke',50, True)
    menu.add_menu_item('drinks',coke)
    coffee = Drinks('Mocha coffee',300, False)
    menu.add_menu_item('drinks',coffee)

 # show men call
    menu.show_menu()
    
    restaurant = Restaurant('sai baba Restaurant',200, menu)
    # add employee
    manager = Manger('uzzal',1621969977,'uzzalhasan1238@gmail.com','sherpur',2000,'janu 1 2022','core')
    restaurant.add_employee('manager',manager)
    
    # add chef
    chef = Chef('rifat',943,'rifat@gmail','mymenshing',200,'jan 2 2021','chef','all')
    restaurant.add_employee('chef',chef)
    # server
    server = Server('noman',9593,'noman@','dhaka',500,'janu 4 2022','serve')
    restaurant.add_employee('server',server)

    # show empylooyss
    restaurant.show_employees()
   # first customer
    customer_1 = Customer('tax',5934,'tax@','club',10000)
    order_1 = Order(customer_1,[pizza_3,coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    # customer one paying for order
    restaurant.receive_payment(order_1,2000,customer_1)
    print('revenue and balance after first customer', restaurant.revenue, restaurant.balance)

    # second customer
    customer_2 = Customer('sohel',5934,'sohek@','dipo',10000)
    order_2 = Order(customer_2,[pizza_1,burger_2,burger_1,pizza_1,coffee])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)

    # customer one paying for order
    restaurant.receive_payment(order_2,1000,customer_2)
    print('revenue and balance after second customer', restaurant.revenue, restaurant.balance)

     # pay rent
    restaurant.pay_expense(restaurant.rent,'Rent')
    print('after',restaurant.revenue,restaurant.balance,restaurant.expense)

if __name__ == '__main__':
    main()