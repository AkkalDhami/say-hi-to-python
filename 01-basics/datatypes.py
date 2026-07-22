import math
import random

## Datatypes

"""

Number: 123, 1.23,  1+2j, 0b111
String: "Hello World", 'akkal'
Boolean: True, False
List: [1, 2, 3]
Tuple: (1, 2, 3)
Dictionary: {'a': 1, 'b': 2}
Set: {1, 2, 3}
None: None
File: open('file.txt')

"""

""" 
#  Advanced: Decorators, Generators, Iterators

# 1. Mutable: can be changed (list, dict, set, array)

# 2. Immutable: cannot be changed (tuple, string, int, float, bool)

"""

username = "akkal dhami"
print(username)

print(type(username))

username = 1  # creates a new variable in memory

print(type(username))
print(username)


print("\nList:")  # (array)
mylist = [1, 2, 3, [4, 5, 6]]

print(type(mylist))
print(mylist)
print(mylist.__len__())


print("\nTuple:")
mytuple = (1, 2, 3, [4, 5, 6])

print(type(mytuple))
print(mytuple)
print(mytuple[0])
print("lenght of tuple:", len(mytuple))


print("\nDictionary:")
mydict = {"name": "akkal", "age": 21, "city": "New York"}

print(type(mydict))
print(mydict)
print("name:", mydict.get("name"))

print("\nSet:")
myset = {1, 2, 3, 4, 5, 1}

print(type(myset))
print(myset)


print("\nNone:")
myvar = None
print(myvar)


print("\nMath:")
print(math.pi)
print(math.e)
print(math.sqrt(9))


print("\nRandom:")
print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print("\nString:")
name = "akkal"
print(len(name))
print(name[0])
print(name[-2])
print(name[1:3])  # 0-a, 1-k, 2-k, 3-a, 4-l , 3 not included

# print(dir(name))