#touple means single baket e value gola ashbe
# list e third baketer modde value gula ashbo

def touple():
    return 3,4
print(touple())
things = 'pen','chair','water botol','ami','tumi'
# print(type(things))
# print(things[0])
# print(things[-2])
# print(things[::-1])
# print(things[3:6])
if 'ami' in things:
    print('exists')
for item in things:
    print(item)
print(len(things))
mega=([1,2,3],[2,4,5])
print(mega[0])
mega[0][1]=34
print(mega)