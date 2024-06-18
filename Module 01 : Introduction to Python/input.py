# print(' Now I need money')
# money=input('Give me some money : ')
# print('here is your money',money)
first_money=input(' one man gave me some money: ')
second_money=input(' second man gave me some momey: ')
print('I got momey : ' ,first_money, 'and' , second_money)
# By default the input from user will be string type 
print(type(first_money))
first_money_int=int(first_money)
second_money_int=int(second_money)
print(type(first_money_int))
total= first_money_int + second_money_int
print(total)
""" 
type converrsion
1. str(y)      It converts y to a string.
2. tuple(y)    It converts y to a tuple.
3. list(y)     It converts y to a list.
4. set(y)      It converts y to a set
5. float(y)    It converts y to a floating-point number.
6. oct(y)	   It converts an integer to an octal string
7. hex(y)	   It converts an integer to a hexadecimal string.
8. ord(y)	   It converts a character into an integer.
9. dict(y)     It creates a dictionary and y should be a sequence of (key, value) tuples.
10. complex(real [imag])    It creates a complex number.
11. int(y [base])       It converts y to an integer, and Base specifies the number base
                        For example, if you want to convert the string into decimal numbers then you’ll use 10 as the base.
 """