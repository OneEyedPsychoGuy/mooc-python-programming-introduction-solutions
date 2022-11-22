limit = int(input("Limit: "))
sum, num = 1, 1
text = f"The consecutive sum: 1"

while sum < limit:
    num += 1
    sum += num
    text += f" + {num}"

print(f"{text} = {sum}")