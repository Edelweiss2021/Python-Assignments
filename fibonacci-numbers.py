# fibonacci numbers: each number is the sum of the two preceding ones
# starts from 1 and 1

# Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function.

# n = int(input("enter how many times you'd like to iterate Fibonacci values: "))
# fibonacci = [1, 1]
# x = 0
# y = 1

# for i in range(n):
#     a = fibonacci[x] + fibonacci[y]
#     fibonacci.append(a)
#     x += 1
#     y += 1
    
# print(f"Fibonacci values: ", fibonacci)

# instructor's solution:

n = int(input("enter how many times you'd like to iterate Fibonacci values: "))

fibo = [1, 1]

for i in range(n-2):

    fibo.append(fibo[i] + fibo[i+1])
print("Fibonacci numbers : ", fibo)