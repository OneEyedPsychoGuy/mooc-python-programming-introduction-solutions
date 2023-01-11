limit = int(input("Limit: "))
sum, num = 0, 0

while sum < limit:
    num += 1
    sum += num

print(str(sum))