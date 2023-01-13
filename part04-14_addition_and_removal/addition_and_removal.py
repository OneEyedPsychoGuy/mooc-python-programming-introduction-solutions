nums = []
while True:
    print(f"The list is now {nums}")
    command = input("a(d)d, (r)emove or e(x)it: ")
    if command == "d":
        nums.append(len(nums) + 1)
    elif command == "r":
        nums.pop()
    elif command == "x":
        print("Bye!")
        break
    else:
        print("Unknown command")