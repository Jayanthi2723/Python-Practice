class Engine:
    def __init__(self,capacity):
        self.capacity=capacity
    def start(self):
         print("Engine started")
    def stop(self):
        print("Engine stopped")
class Car:
    def __init__(self,make,model,capacity):
        self.make=make
        self.model=model
        self.engine=Engine(capacity)
    def start(self):
        print(f"{self.make} {self.model} started")
        self.engine.start()
    def stop(self):
        print(f"{self.make} {self.model} stopped")
        self.engine.stop()
my_car=Car("Toyota","Bmw", 2000)
my_car.start()
my_car.stop()
