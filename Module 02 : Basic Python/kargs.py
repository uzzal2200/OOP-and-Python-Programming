def full_name(first,last):
    name=f'full name is: {first} {last}'
    return name
# take paremeters inorder (serial wise)
#name=full_name('uzzal','noman')
name=full_name(last='noman',first='uzzal')
print(name)
def a_lot(num1,num2):
    sum=num1+num2
    sub=num1-num2
    divide=num1/num2
    mul=num1*num2
    return sum,sub,divide,mul
everything=a_lot(45,5)
print(everything)