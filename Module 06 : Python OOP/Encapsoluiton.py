 # encapsulation  ---> hide details
# acces modifier  : public , private , protected
class Bank:
    def __init__(self , holder_name , initial_deposite):
        self.holder_name = holder_name # public attribute
        self._brance = 'bonani 11' # protected attribute
        self.__balance = initial_deposite #  private attribute
    def deposite(self,amount):
        self.__balance += amount
    def got_balance(self):
        return self.__balance
    def withdraw(self , amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
        else :
            return f'taka nai'

rafsan = Bank('rafsan' , 50000)
print(rafsan.holder_name)
# print(rafsan.balance)
rafsan.deposite(5000)
print(rafsan.got_balance())
# print(dir(rafsan))
print(rafsan._Bank__balance)
