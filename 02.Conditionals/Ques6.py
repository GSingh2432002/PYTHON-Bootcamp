# Transportation Mode Selection
dist = 78
if dist < 3:
    transport = "Walk"
elif dist <= 15:
    transport = "Bike"
else:
    transport = "Car"
print("AI recommends you the transport of: ", transport)