# Create a class with attributes like brand and model. Then create an instance of this class.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
my_car = Car("BMW", "7 Series 740li")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Harrier")
print(my_new_car.brand)
print(my_new_car.model)