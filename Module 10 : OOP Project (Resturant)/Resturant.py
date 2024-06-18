class Restaurant:
    def __init__(self,name,rent, menu = []):
        self.name = name
        self.orders = []
        self.chef = None
        self.server = None
        self.manager = None
        self.rent = rent
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee

        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee
    
    def add_order(self,order):
        self.orders.append(order)
    
    def receive_payment(self, order, amount , customer):
        #print(f'{amount} {order.bill}')
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print('Not Enough money.pay more tk')
        
    def pay_expense(self, amount, description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount

            print('Expense {amount} for {description}')
        else:
            print(f'Not enough to pay {amount}')
    def pay_salary(self,employee):
        if employee.slary < self.balance:
            employee.receive_salary()

    def show_employees(self):
        print(f'---------SHOWING EMPLOYEE------------')
        if self.chef is not None:
            print(f'Chef: {self.chef.name} with salary: {self.chef.salary} his num:{self.chef.phone}')
        if self.server is not None:
               print(f'Chef: {self.server.name} with salary: {self.server.salary} his num:{self.server.phone}')
        if self.manager is not None:
               print(f'Chef: {self.manager.name} with salary: {self.manager.salary} his num:{self.manager.phone}')
     
