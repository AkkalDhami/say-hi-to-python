"""

Problem 04: Create a function that returns both the area and circumference of a circle given its radius.

"""

from math import pi


def calculate_area_circumference(radius):
    return {
        "area": round(pi * radius**2, 2),
        "circumference ": round(pi * 2 * radius, 2),
    }


result = calculate_area_circumference(2.34)
print(result)
