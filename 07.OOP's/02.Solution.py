# Add a method to the Car class that display the full name of the car.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self)  :
        return f"{self.brand} {self.model}"

my_car = Car("BMW", "7 Series 740li")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Harrier")
print(my_new_car.brand)
print(my_new_car.model)