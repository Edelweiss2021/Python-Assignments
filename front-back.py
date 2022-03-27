# Task:

# Given a string, return a new string where the first and last chars have been exchanged.

# my solution:

# def front_back(word):
#     if len(word) > 1:
#         a = list(word)
#         c = a[0]
#         d = a[-1]
#         a.pop(0)
#         a.pop(-1)
#         a.insert(0, d)
#         a.append(c)
#         b = ''
#         for i in a:
#             b += i
#         return b
#     else:
#         return word
# print(front_back('clarusway'))
# print(front_back('a'))
# print(front_back('ab'))

# //////////////////////

# classmate's solution:

def front_back(word):
    start = word[0]
    end = word[-1]
    switched = end + word[1:-1] + start
    if len(word) > 1:
        return switched
    else:
        return word

print(front_back("clarusway"))
print(front_back("a"))
print(front_back("ab"))
