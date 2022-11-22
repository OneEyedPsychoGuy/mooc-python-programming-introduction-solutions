count = 0

print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    count += 1

print(f"Numbers typed in {count}")