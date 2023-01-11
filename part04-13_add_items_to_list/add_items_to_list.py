items = []
amount = int(input("How many items: "))

while len(items) < amount:
    items.append(int(input(f"Item {len(items) + 1}: ")))

print(items)