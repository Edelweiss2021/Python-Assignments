# Python Assignment - 011/06 (Prime Numbers)
# Task : Print the prime numbers which are between 1 to entered limit number (n).
# You can use a nested for loop.
# Collect all these numbers into a list
# The desired output for n=100 : [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

num = int(input("enter a number to generate prime numbers up to entered value: "))
prime_numbers = []

for i in range(2, num+1):
  isPrime = True
  for j in range(2, i):
    if i % j == 0:
      isPrime = False
  if isPrime:
    prime_numbers.append(i)
print(prime_numbers)

# # /////////////////////

# # Python program to print first 10 prime numbers

# # A function name prime is defined using def

# def prime(n):
# 	x = 1
# 	count = 0
# 	while count < n:
# 		for d in range(2, x, 1):
# 			if x % d == 0:
# 				x += 1
# 		else:
# 			print(x)
# 			x += 1
# 			count += 1

# # Driver Code
# n = 10

# # print statement
# print("First 10 prime numbers are: ")
# prime(n)
