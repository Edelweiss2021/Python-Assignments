# Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.
# The examples of the desired output are as follows :
# input →  19 ⇉ output : 19 is a prime number
# input →  10 ⇉ output : 10 is not a prime number

# ///////////////////////////////////////////////////

# # instructor's solution:
# n = int(input("Enter a positive int number to check if it's a prime number: "))

# counter = 0

# # if modulus operation in range returns more than 2 (division by 1 and division by self) it is not prime.
# # using counter as a parameter, calculate how many modulus exists.

# for i in range (1, n + 1):
#     if n % i == 0:
#         counter += 1

# if n < 2 or (counter >= 3):
#     print(n, "is not a prime number.")
# else:
#     print(n, "is a prime number.")

# ////////////////////////////////////////////////////

# classmate's solution:

number=int(input("write a number and see if it is a prime number or not: "))
prime = True
for i in range(2, number):
    if number % i == 0:
        prime = False
        break
    else:
        prime = True
if prime and number > 1 :
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

#///////////////////////////////////////////////////

# # another approach

# # get a number from user and generate prime numbers up to the input value.

# given = int(input("Enter a number: "))

# for n in range(2, given):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, "is not a prime number. Because", n, "equals", x, "*", n//x)
#             break
#     else:
#         print(n, "is a prime number.")

#///////////////////////////////////////////////////

# # my works, no solution

# print("Hello! Let's find out if you've entered a prime number!")
# prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# number = int(input("Please enter a number: "))

# if number > 2 and number % 2 == 0: # No even number n greater than 2 is prime because any such number can be expressed as the product 2 × n / 2.
#     print(f"{number} is not a prime number.")
# else:
#     print(f"{number} could be a prime number.")
# else:
#     for i in prime_numbers:
#         if number // i < 1:
#             print(f"{number} is a prime number.")
#             break
#         else:
#             print(f"{number} is not a prime number.")
#             break

# given = int(input("enter a number to check if it's a prime number: "))

# if given > 1:
#     for i in range (2, given):
#         if given // i == 1:
#             print(f"{given} is a prime number.")
#             break                   
#         else:
#             i += 1
# else:
#     print(f"{given} is not a prime number.")

