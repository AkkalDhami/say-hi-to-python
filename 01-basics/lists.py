langs = ["python", "java", "c++", "javascript", "php"]
print("\nlenght : ", len(langs))

print(langs)
print(langs[0])
print(langs[-1])
print(langs[0:3])
print(langs[::-1])

langs[0] = "kotlin"
print("\nupdate: ", langs)

langs.append("typescript")
print("append: ", langs)

langs.insert(2, "go")
print("insert: ", langs)

langs.remove("php")
print("remove: ", langs)

print("\nlangs: ", langs)

print("\nremove last element: ", langs.pop())  # * removes last element
print("langs: ", langs)
print("\nremove 1st element: ", langs.pop(0))  # * removes first element
print("langs: ", langs)

nums = [1, 2, 3, 4, 5]
print("\nnums: ", (nums))
print("clear: ", nums.clear())
print("nums: ", (nums))

print("\nlangs: ", langs)
print("\nfor loop: ")
for lang in langs:
    print(lang, end="-> ")

print("\n")
for lang in langs:
    print(lang, end=", ")

if "go" in langs:
    print("\nGo is present in langs")


copied_langs = langs.copy()
print("\ncopied langs: ", copied_langs)

print(copied_langs == langs)  # True (check value)
print(copied_langs is langs)  # False (check memory address)

langs.remove("go")
print("\nremoved go: ", langs)
print("copied langs: ", copied_langs)  # no change because it is a copy not reference

print("\nrange: ", range(1, 10))

squared_nums = [x**2 for x in range(1, 10)]
print("\nsquared nums: ", squared_nums)

cube_nums = [x**3 for x in range(5)]
print("\ncube nums: ", cube_nums)
