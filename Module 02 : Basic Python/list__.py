a=["phitron"]

print(a)
print(*a)
c=[['a','b'],['c']]
for i in c:
   # print(i)
   for val in i:
      print(val)
# append
a=[]
a.append(5)
a.append('a')
print(a)
print("before clear",a)
print(a.clear())
print("after clear",a)
# copy
c_=['a','y']
b_=c_.copy()
print(b_)
# insert
my_list=[1,2,3,4,5]
my_list.insert(2,10)
print(my_list)
# my_list.pop(1) # pop kora hoice
delete_val=my_list.pop(1)
print(my_list)
print(delete_val)
l=[31,2,34]
l.reverse()
print(l)
l.sort()
print(l)
l.remove(34)
print(l)