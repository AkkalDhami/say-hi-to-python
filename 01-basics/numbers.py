x = 2
y = 3

print(f"x + y: {x + y}")
print(f"x - y: {x - y}") 
print(f"x * y: {x * y}") # int
print(f"x / y: {x / y}") # float
print(f"x // y: {x // y}") # floor
print(f"x % y: {x % y}") # remainder
print(f"x ** y: {x ** y}") # power

print("\nint: ",int(2.5))
print("round off: ",round(2.8)) # 3
print("round off: ", round(2.8123, 2)) # 2.81
print("hello " + "akkal")

print(x, y)

print(f"2 ^ 10: { 2 ** 10 }")

print("bool: ", True + False)
print("bool: ", (True + True))
print("type: ", type(True + True)) # int

print("bool: ", not False) # True
print("bool: ", not True) # False

print("bool: ", 1 == 1) # True
print("bool: ", 1 == 2) # False

print("bool: ", 1 < 2 and 2 < 3) # True
print("bool: ", 1 > 2 and 2 < 3) # False
print("bool: ", 1 > 2 or 2 < 3) # True


import math

print("\n\nMath:")

print("sqrt: ", math.sqrt(4))
print("floor: ", math.floor(4.65)) # 4 
print("ceil: ", math.ceil(4.65)) # 5
print("pow: ", math.pow(2, 3))

print("max: ", max(1, 2, 3, 4, 5))
print("min: ", min(1, 2, 3, 4, 5))

print("trunc: ", math.trunc(4.15)) # 4 (toward zero)
print("factorial: ", math.factorial(5)) # 120
print("abs: ", abs(-123)) #* 123 (absolute value(positive))

print("sum: ", sum([1, 2, 3, 4, 5]))
print("pi: ", math.pi)
print("e: ", math.e)
print("log: ", math.log(10))

octal = 0o20
print("octal: ", octal) # 16
'''
0o10 => 8
0o15 => 3
'''

#! (8, 9 => ERROR)

print("octal: ", 0o12) # 10 

print("hex: ", 0x12) # 18

print("bin: ", 0b11) # 3

print("bin: ", bin(3))
print("hex: ", hex(3))
print("octal: ", oct(3))

print(int('1000', 2)) # 8

import random

print("\n\nRandom:")
print(random.random())
print(random.randint(1, 10)) #* returns random number between 1 to 10
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #* returns random number from list

print("\n\nSet:")
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("union: ", set1 | set2) #* union
print("intersection: ", set1 & set2) #* intersection
print("difference: ", set1 - set2) #* difference
print("symmetric difference: ", set1 ^ set2)