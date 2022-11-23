while True:
    num = int(input("Please type in a number: "))
    if num <= 0:
        break

    cur, fact = 1, 1
    while cur <= num:
        fact *= cur
        cur += 1
    
    print(f"The factorial of the number {num} is {fact}")
    
print("Thanks and bye!")