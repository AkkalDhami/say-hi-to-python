"""

Problem 07: Write a function that takes variable number of arguments and returns their sum.

"""


def sum_all(*args):  # *args => tuple
    # print("args: ", type(args))
    res = 0
    for i in args:
        res += i
        print("i: ", i * 2)

    print("result: ", res)
    return sum(args)


print("sum: ", sum_all(1, 2, 3))

# print("sum: ", sum_all(1, 2, 3, 4))
