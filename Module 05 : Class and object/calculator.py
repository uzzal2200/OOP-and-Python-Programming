class calculator:
    brand='casio m100'
    def sum(self,num1,num2):
        s = num1 + num2
        return s
    def multiply(self,n1,n2):
        result = n1 * n2 
        return result
    def divide(self,t1, t2):
        r = t1 / t2
        return r
    
my_calculator = calculator()
result1 = my_calculator.sum(2,3)
result2 = my_calculator.multiply(2,3)
result3 = my_calculator.divide(12,3)
print(result1)
print(result2)
print(result3)
    