class BMW:
    def __init__(self,fuel_type,max_speed):
        self.fuel_type=fuel_type
        self.max_speed=max_speed
    def fuel_types(self):
        print("Fuel type for a BMW is",self.fuel_type)
    def max_speeds(self):
        print("Max speed for a BMW is",self.max_speed)
class Ferrari:
    def __init__(self,fuel_type,max_speed):
        self.fuel_type=fuel_type
        self.max_speed=max_speed
    def fuel_types(self):
        print("Fuel type for a Ferrari is",self.fuel_type)
    def max_speeds(self):
        print("Max speed for a Ferrari is",self.max_speed)
b=BMW("Petrol", 250)
f=Ferrari("Petrol", 350)
b.fuel_types()
b.max_speeds()
f.fuel_types()
f.max_speeds()
