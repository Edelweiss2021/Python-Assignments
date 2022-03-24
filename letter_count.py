# Python Assignment - 011/08 (Letter Count)

# Task:
# Count the number of each letter in a sentence.

#     The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.

#     Write a Python program that;

        #     takes a sentence from the user,
        #     counts the number of each letter/chars of the sentence,
        #     collects the letters/chars as a key and the counted numbers as a value in a dictionary.

# Sample input: hippo runs to us! 	
# Output: {'s': 2, 'r': 1, 't': 1, 'h': 1, 'n': 1, 'i': 1, 'u': 2, 'o': 2, 'p': 2, ' ': 3, '!': 1}

text = input("Enter a text: ")

all_chars = [] # create an empty master list
letters = "q w e r t y u i o p a s d f g h j k l z x c v b n m".split() # create a list with all letters
numbers = "1 2 3 4 5 6 7 8 9 0".split() # create a list with all numbers
special_chars = '''! @ # $ % ^ & * ( ) - _ = + [ { ] } \ | ; : ' , < . > / ? ` ~ "'''.split() # create a list with all special characters

# fill in master list with all the characters available
all_chars.extend(letters)
all_chars.extend(numbers)
all_chars.extend(special_chars)
all_chars.append(" ") # add space to master list

dict1 = {}

for i in text.lower():
  if i in all_chars:
    if i not in dict1:
      dict1[i] = 1
    else:
      dict1[i] += 1

print(dict1)