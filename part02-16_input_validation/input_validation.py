from math import sqrt

while True:
    num = int(input("Please type in a number: "))
    if num > 0:
        print(sqrt(num))
    elif num == 0:
        print("Exiting...")
        break
    else:
        print("Invalid number")