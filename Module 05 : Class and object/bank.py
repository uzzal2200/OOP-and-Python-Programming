class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 1000000
    def get_balance(self):
        return self.balance
    def deposite(self,amount):
        if(amount > 0):
            self.balance += amount
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f'you can not withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'you can not withdraw more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'here is your money : {amount}')
            print(f'your balance after withdraw :{self.get_balance()}')

brac =Bank(15000)
brac.withdraw(25)
brac.withdraw(20000)
brac.withdraw(1000)



shonali = Bank(5000)
shonali.deposite(2000)
shonali.deposite(4000)
print(shonali.get_balance())