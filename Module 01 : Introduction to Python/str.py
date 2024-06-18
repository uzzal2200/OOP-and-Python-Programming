# captilaize
b='phitron'
c='PHD'
print(b.capitalize()) # first letter capitalize
print(b.upper()) # upper letter 
print(c.lower()) # shob lower letter 
print(c.casefold) # shob gula lower case e convert kore
a='uzzal'
for ch in a:
    print(ch,end="")

print()
#find
text="hello, world"
src='world'
index=text.find(src)
print(index)
if index !=-1:
    print(f"the result '{src}' was found at index '{index}' ")

else:
    print('not found')
# cout
cp='uzzal'
print(cp.count('z'))
from collections import Counter
print(Counter(cp))