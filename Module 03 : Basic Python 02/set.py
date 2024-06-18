# list ---> []
# touple ---> ()
# set ---> {}
# set means unique items collection no duplicate value
num=[12,56,98,78,23,53,56]
print(num)
set_num=set(num)
print(set_num)
set_num.add(44)
print(set_num)
set_num.remove(98)
print(set_num)
for item in set_num:
    print(item)
if 9 in set_num:
    print('not exists')
elif 78 in set_num:
    print('exists')

A={1,2,3}
B={1,3,5,2,4,6}
print(A & B) # intersection ber hobe
print(A | B) # union operation