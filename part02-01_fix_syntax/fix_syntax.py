num = int(input("Please type in a number: "))

if num > 100:
    print("The number was greater than one hundred")
    num -= 100
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {num}")

print(f"{num} must be my lucky number!")
print("Have a nice day!")