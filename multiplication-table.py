# task: generate multiplication table

number = int(input("enter a number: "))

for i in range(11):
  c = number * i
  print(number, "x", i, "=", c)