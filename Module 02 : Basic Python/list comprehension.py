numbers=[45,87,96,65,43,85,1426,61]
odds=[]
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)

print(odds)
#odd_num=[num for num in numbers if num % 2 == 1 ]  
odd_num=[num for num in numbers if num % 2 == 1 if num % 5 == 0]  
print(odd_num)

players=['shakib','tamim','mostafiz']
ages=[39,38,34]
age_com=[]
for player in players:
    print(player)
    for age in ages:
        print(player,age)
        age_com.append([player,age])
print(age_com)
age_comb2=[[player,age] for player in players for age in ages]
print(age_comb2)
