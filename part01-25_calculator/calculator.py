num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    print(f"\n{num1} + {num2} = {num1 + num2}")
elif operation == "multiply":
    print(f"\n{num1} * {num2} = {num1 * num2}")
elif operation == "subtract":
    print(f"\n{num1} - {num2} = {num1 - num2}")