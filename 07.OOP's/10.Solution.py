# Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
                
    def get_brand(self):
        return self.__brand + " !"
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.fuel_type())

# my_car = Car("BMW", "7 Series 740li")
# my_car.model = "5 Series 520d"
# Car("BMW", "M5")

# print(my_car.general_description())
# print(my_car.model)

class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCarHybrid(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarHybrid("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())