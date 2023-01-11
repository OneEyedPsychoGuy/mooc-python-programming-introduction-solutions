num = int(input("Please type in a number: "))
cur = 1

while cur <= num // 2:
    print(cur)
    print(num + 1 - cur)
    cur += 1

if num % 2 != 0:
    print(cur)