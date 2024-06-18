# def sum(num1,num2,num3,num4=0,num5=0):
#     result=num1+num2+num3
#     return result
# final=sum(5,5,5)
# print(final)
# args
def all_sum(num1,num2,*numbers):
    print(numbers)
    sum=0
    for num in numbers:
        sum = sum+num
    return sum
total=all_sum(1,2,3,5,3)
print(total)

