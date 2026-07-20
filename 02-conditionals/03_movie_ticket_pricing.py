age = int(input("Enter your age: "))

day = "wednesday"

price = int(input("Enter price: ")) if age >= 18 else 8

if day == "wednesday":
    price -= 2  # $2 discount

print(f"Your ticket price is ${price}")
