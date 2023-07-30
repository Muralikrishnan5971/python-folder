class Vehicle():
    def __init__(self, price, gas , color) -> None:
        self.price = price
        self.gas = gas
        self.color = color

    def fill_up_tank(self):
        self.gas = 100
    
    def empty_tank(self):
        self.gas = 0
    
    def gas_left(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color, speed) -> None:
         super().__init__(price, gas, color)
         self.speed = speed
    
    def hit_horn(self):
        print("BEEEEEEP......BEEEEEP")


class Truck (Vehicle):
    def __init__(self, price, gas, color, speed, no_of_wheels) -> None:
         super().__init__(price, gas, color)
         self.speed = speed
         self.no_of_wheels = no_of_wheels
    
    def hit_horn(self):
        print("HONKKKK.....HONK")

    def no_of_wheels_in_truck(self):
        return self.no_of_wheels 