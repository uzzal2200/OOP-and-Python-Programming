nam1='shakib'
nam4='shakib\'s khan' # skip kora
nam2="shakib"
# multiline string
nam3=""" 
shakib khan one and only
"""
print(nam1)
print(nam2)
print(nam3)
print(nam4)
name='uzzal'
for char in name:
    print(char)
print(name[2])
print(name[1:3])
print(name[-2])
print(name[::-1])
# mutable means changeable
# imutable means you can not change it
uzzal='khanpatha'
if 'khan' in uzzal:
    print('exist')
