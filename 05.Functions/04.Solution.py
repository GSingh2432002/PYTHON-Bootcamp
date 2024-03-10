# Create a function that returns both the area and circumference of a circle given its radius
import math
def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference
ar, cf = circle_stats(4)
print("Area:- ", ar, "Circumference:- ", cf)
