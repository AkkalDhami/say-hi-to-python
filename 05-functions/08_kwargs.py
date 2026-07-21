"""

Problem 08: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

"""


# def print_kwargs(name="batman", power="lazer"):
#     print(name, power)
#     return {name: power}


def print_kwargs(**kwargs):  # * type: dict
    # print(type(kwargs))
    for key, value in kwargs.items():
        return {key: value}


result = print_kwargs(name="batman", power="lazer")
print(result)
print(print_kwargs(name="python", power="AI"))
print(print_kwargs(power="Web Dev", name="JavaScript"))
