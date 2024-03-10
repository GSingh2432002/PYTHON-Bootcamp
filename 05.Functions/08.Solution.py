# Create a function that accepts any number of keyword arguments and prints them in the format.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
print_kwargs(name="Hulk", power="Sbko maut ke ghat utarna")
print_kwargs(name="Hulk")
print_kwargs(name="Hulk", power="Sbko maut ke ghat utarna", enemy="Thor")