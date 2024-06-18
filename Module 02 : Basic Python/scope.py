balance=400
def buy(item,price):
    global balance
    print(f'previous balance value',balance)
    balance=balance - price
    print(f'balance after buying{item}',balance)

buy('sunglass',1000)