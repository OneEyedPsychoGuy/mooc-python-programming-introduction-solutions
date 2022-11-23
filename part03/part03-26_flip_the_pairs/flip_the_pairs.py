num = int(input("Please type in a number: "))
cur = 1

while cur < num:
    print(cur + 1)
    print(cur)
    cur += 2

if cur <= num:
    print(cur)