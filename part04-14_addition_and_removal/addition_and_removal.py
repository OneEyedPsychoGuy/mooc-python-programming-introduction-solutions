numbers = []
while True:
    print(f"The list is now {numbers}")
    command = input("a(d)d, (r)emove or e(x)it: ")
    if command == "d":
        numbers.append(len(numbers) + 1)
    elif command == "r":
        numbers.pop()
    elif command == "x":
        print("Bye!")
        break
    else:
        print("Unknown command")