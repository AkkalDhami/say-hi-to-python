""" "

Problem 04: Reverse a string using a loop.

"""

str = input("Enter a string: ")

reversed_str = str[::-1]
print(f"Reversed string: {reversed_str}")

rev_str = ""

# for i in range(len(str) - 1, -1, -1):
#   rev_str += str[i]

for char in str:
    rev_str = char + rev_str

print(f"Reversed string: {rev_str}")
