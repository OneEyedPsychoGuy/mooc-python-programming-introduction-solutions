year = int(input("Year: "))
next = year

while True:
    next += 1
    if next % 400 == 0:
        break
    elif next % 4 == 0 and next % 100 != 0:
        break
    
print(f"The next leap year after {year} is {next}")