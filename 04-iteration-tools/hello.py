"""

? Iterable object: file, lists, dictionaries, range

"""

file = open("04-iteration-tools/test.py")

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.__next__())
# print(file.__next__())
# print(file.__next__())
# print(file.__next__())
# print(file.__next__())


# for line in file:
#     print(line)

while True:
    line = file.readline()
    if not line:
        break
    print(line)


my_list = [1, 2, 3, 4]
Iter = iter(my_list)
print(Iter.__next__())  # 1
print(Iter.__next__())  # 2
print(Iter.__next__())  # 3
print(Iter.__next__())  # 4


print("file is iter(file):", file is iter(file))  # True
print("my_list is iter(my_list):", my_list is iter(my_list))  # False


my_dict = {"a": 1, "b": 2}

for key, value in my_dict.items():
    print(f"{key}: {value}")

DictIter = iter(my_dict)
# print(DictIter)
print(next(DictIter))
print(next(DictIter))


Range = range(5)
print(Range)
IterRange = iter(Range)
print(next(IterRange))
print(next(IterRange))
print(next(IterRange))
print(next(IterRange))
print(next(IterRange))
