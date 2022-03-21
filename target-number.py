# Receive target as input from user.
# Find out if target and sum of any items in the list are equal. List items that produce total.
  
target = int(input("enter a target number: "))
a = [5, 9, 4, 7, 12, 3, 2]
new_list = []

for i in a:
    a.remove(i)
    for j in a:
        if target == i + j:
            new_list.extend([i,j])
if len(new_list) == 0:
    print("no match")
else:
    print(new_list)