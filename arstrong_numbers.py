given = input("Please enter a value: ")
a = len(given)
i = 0
my_list = list()
total = 0

if not given.isdigit() or int(given) < 0:  # display error message for incorrect value entry
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

while i < a: # populate the list
  my_list.append(int(given[a - 1 - i])**a)
  i +=1
  if i > a:
    break
print(my_list)

for x in range(a):  # sum
    total += my_list[x]
print(total)

if total == int(given): # display success message
    print(int(given), "is an Armstrong number")
else:
    print(int(given), "is not an Armstrong number")