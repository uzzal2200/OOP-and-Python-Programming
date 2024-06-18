def call():
    print('calling some one  i dont know ')
class phone:
    price=19000
    colour='blue'
    brand='samsung'
    feature=['ami','tumake','ro','kase','pete']

    def call(self):
        print('really miss you')
    def send(self,phn,sms):
        text=f'sending sms to : {phn} and message {sms}'
        return text

my_phone=phone()
print(my_phone.feature)
my_phone.call()
result=my_phone.send(1621969977,'I am so alone')
print(result)
