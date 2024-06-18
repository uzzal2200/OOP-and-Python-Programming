# inheritan vs composition

class Engine:
    def __init__(self):
        pass
    def start(self):
        return "Engine started"
class Driver:
    def __init__(self):
        pass

# car "has a" engine
class Car:
    def __init__(self):
        self.engine = Engine()
        self.driver = Driver()
    def star(self):
        self.engine.start()
# other Example composition
class CPU:
    def __init__(self,cores) -> None:
        self.cores = cores
        
class RAM:
    def __init__(self, size):
        self.size = size

class HardDriver:
    def __init__(self,capacity):
        self.capacity = capacity
class Computer:
    def __init__(self , cores , size_ram, hd_capacity):
        self.cpu = CPU(cores)
        self.ram = RAM(size_ram)
        self.hd_disc = HardDriver(hd_capacity)

mac =  Computer(8, 16, 512)