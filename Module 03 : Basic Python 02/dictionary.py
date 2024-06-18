# key value pair, dctionary, object,has table,overlap with set
# sentax of dictionary: variable name = {keys : value,keys : value, keys : value}
person={'name' : 'uzzal','adress' : 'sherpur','relationship' : 'single','ocuption' : 'student'}
print(person['relationship'])
print(person.keys())
print(person.values())
person['age']='23'
print(person)
person['name'] = 'shongi hara pakhi'
print(person)
del person['relationship']
print(person)
#sepecial dictionary looping
for key,value in person.items():
    print(key,value)