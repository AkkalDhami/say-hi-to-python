multi = """Akkal
Dhami
""" # <pre>

print(multi)

name = "Akkal Dhami"
print(name)
print("\nslice: ", name[0:3])
print("slice: ", name[:3])
print("slice: ", name[3:])
print("slice: ", name[:])

print("reverse: ", name[::-1])

num_list = "0123456789"
print("\nreverse num: ", num_list[::-1])
print("slice num: ", num_list[0:7:2]) # 0, 2, 4, 6 => 0 - 7(7 not included) with step 2
print("slice num: ", num_list[0:7:3]) # 0, 3, 6 => 0 - 7(7 not included) with step 3
print("slice num: ", num_list[0:7:4]) # 0, 4 => 0 - 7(7 not included) with step 4

fname = "Akkal"
print(f"\nlength of '{fname}': ", len(fname))
print(f"index of 'A': ", fname.index("A"))
print("Upper case: ", fname.upper())
print("Lower case: ", fname.lower())
print("Capitalize: ", "hello world".capitalize())
print("trim/strip: ", "   hello world   ".strip())

print("\nreplace: ", "hello akkal".replace("hello", "hi"))

lang = "python, java, c++, javascript, typescript"

print("\nsplit: ", lang.split(",")) # list
print("find index:", "akkal dhami".find("dhami")) # index => 6

print("count: ", "akkal dhami dhami".count("dhami")) # 2

print("\nstartswith: ", "akkal dhami".startswith("akkal")) # True
print("endswith: ", "akkal dhami".endswith("dhami")) # True

print("\njoin: ", "-".join(["akkal", "dhami"]))
print("join: ", " ".join(["akkal", "dhami"]))

chai_type = "masala"
quantity = 2
order = "I want {} cups of {} chai".format(quantity, chai_type)
print("\nformat: ", f"I want {quantity} cups of {chai_type} chai")
print("format2: ", order)

print("\nfor loop: ")
for letter in "akkal":
  print(letter)
  

ram = "He said, \"Akkal\""
print("\n\" \": ", ram)

raw_str = r"akkal\ndhami"
print("raw string: ", raw_str)

print("\nin: ", "akkal" in "akkal") # True
print("string: ", "akkal" not in 'akkal') # False