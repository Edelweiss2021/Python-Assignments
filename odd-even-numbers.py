# write a program to get input from the user as integers and collect the even and odd numbers in two different list. 
# Plus, display how many times odd and even numbers entered.

evens = []
odds = []
given_list = []

print("Let's check how many odd and even numbers a series have!")
n = int(input("How many numbers would you like to check? "))

for i in range(n):
    number = int(input("Enter numbers: "))
    given_list.append(number)

print(f"Here's the numbers you've entered: {given_list}")
for i in given_list:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i) 

print(f"The number of even digits: {len(evens)}")
print("Even numbers are: ", evens)
print(f"The number of odd digits: {len(odds)}")
print("Odd numbers are: ", odds)