limit = int(input("Limit: "))
sum, num = 1, 1

while sum < limit:
    num += 1
    sum += num

print(sum)