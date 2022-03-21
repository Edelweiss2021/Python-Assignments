# Aynı zamanda hem 2'ye hem 4'e hem de 5'e bölünebilen sayılara xyz sayısı diyelim. Hem 2'ye hem de 5'e bölünebilen sayılar ise abc sayısı olsun. 100 ile 300 arasındaki xyz sayılarından kaç tanesi aynı zamanda abc sayısıdır? xyz, abc ve her ikisinde bulunan sayıları da yazdıralım...


xyz_numbers = []
abc_numbers = []
for i in range(100, 300):
    if (i % 2 == 0) and (i % 5 == 0) :
        abc_numbers.append(i)
        if i % 4 == 0:
            xyz_numbers.append(i)
intersection = set(xyz_numbers).intersection(set(abc_numbers))
print("xyz = ", xyz_numbers)
print("abc = ", abc_numbers)
print("intersection = ", intersection )
# count = 0 
# for i in intersection:
#     count +=1
print("count = ", len(intersection))