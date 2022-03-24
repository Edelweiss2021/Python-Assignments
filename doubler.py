# Assignment - 1 (Doubler)
# Task: Given two integer values, return their sum. If the two values are the same, then return double their sum.

def sum_double(a, b):
    if a == b:
        return (a+b)*2
    else:
        return (a+b)

print(sum_double(1, 2))
print(sum_double(5, 7))
print(sum_double(5, 5))