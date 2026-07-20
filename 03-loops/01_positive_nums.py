"""

Problem 01: Given a list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

"""

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_nums = []

for number in numbers:
    if number > 0:
        positive_nums.append(number)

print("Positive numbers:", positive_nums)
print("Positive numbers count:", positive_nums.__len__())
