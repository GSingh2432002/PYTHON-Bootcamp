# Counting Positive Numbers
numbers = [1,-5,3,-2,9,-7,4,2,-9,8,10,-45,-67]
positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Final count of Positive number is: ", positive_number_count)