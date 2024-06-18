class Laptop:
    def __init__(self,brand,price,colour, memory):
        self.brand = brand
        self.price = price
        self.colour = colour
        self.memory = memory

    def run(self):
        return f'Running python laptop: {self.brand}'
    def coding(self):
        return f'learning pyhton and paracticing'
    
class Phone:
    def __init__(self , brand , price , color , dual_sim):
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim
    def  run(self):
        return f'phn tipa tipa kora'
    def phn_call(self, number , text):
        return f'Sending SMS to : {number} with  : {text}'
        

class Camera:
    def __init__(self , brand , price, color , pixel):
        self.brand = brand
        self.price = price 
        self.color = color
        self.pixel = pixel
    def run(self):
        pass
    def change_lens(self):
        pass

        

    
