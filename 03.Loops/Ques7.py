# Validate Input
while True:
    number = int(input("Enter value between 1 and 10:- "))
    if 1 <= number <= 10:
        print("Thank Your for the Input :) ")
        break
    else:
        print("Invalid Number, Please try again!! ")