# Write a python code that finds the largest number among the n numbers given by the user as input.
# First, take n from the user, then take n numbers one by one and select-print the largest one.
# It is forbidden to use max() function.

# Example:
# Input                Output
# ---------------:     -------------------------:
# n = 5, 1 2 3 4 5     The largest number is:  5
# n = 3, 67 85 19      The largest number is:  85

my_list = []
largest = 0
counter = 0

n = int(input("enter how many numbers you'd like to register: "))

for i in range(n):
    numbers = int(input("enter the numbers: "))
    my_list.append(numbers)
print(n, my_list)

while counter < len(my_list):
    if my_list[counter] > largest:
        largest = my_list[counter]
        counter += 1
    else:
        break       
print("The largest number is: ", largest)