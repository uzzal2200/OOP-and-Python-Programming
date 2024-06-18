# def doulble(x):
#     return x*2

doubled=lambda num : num*2
sq=lambda num : num ** 2
print(doubled(50),sq(4)) 
add=lambda x,y,z : x+y+z
print(add(1,2,3))

numbers=[12,3,45,56,56,23,45,76]
result=map(lambda x: x*2,numbers)
result1=map(lambda x: x**2,numbers)
print(list(result1))
print(list(result))

actors=[
    { 'name': 'uzzal','age' : 56},
    { 'name': 'rahim','age' : 26},
    { 'name': 'korim','age' : 46},
    { 'name': 'helal','age' : 60},
]
jun=filter( lambda actor : actor['age'] < 40,actors)
print(list(jun))

numbers = [9, 15, 2, 36]
numbers[1:4] = [20, 14, 36]
print(numbers)