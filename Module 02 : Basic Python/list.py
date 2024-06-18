# list , connection , array is same (simple terms)
#index=    0    1    2    3    4    5    6    7    8
numbers=[ 45 , 34 , 78 , 90 , 32 , 12 , 49 , 19 , 78 ]
# index=  -9   -8   -7   -6   -5   -4   -3   -2   -1
print(numbers[3],numbers[-3])
# list(start : end) 
# start from the start index and stops before the end index
print(numbers[2:6])
print(numbers[1:7])
# list(start: end : step)
print(numbers[1:3:1])
print(numbers[1:6:2])
print(numbers[7:2:-1])
print(numbers[2:]) 
print(numbers[:6]) 
print(numbers[:]) # shortcut to copy a list
print(numbers[::-1]) # shortcut reverse
