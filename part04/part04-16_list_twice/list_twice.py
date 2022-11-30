numbers = []

while True:
    num = int(input("New item: "))
    if num == 0:
        break

    numbers.append(num)
    print(f"The list now: {numbers}")
    print(f"The list in order: {sorted(numbers)}")

print("Bye!")