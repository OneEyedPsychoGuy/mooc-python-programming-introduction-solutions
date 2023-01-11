start = int(input("Year: "))
year = start

while True:
    year += 1
    if year % 400 == 0:
        break
    elif year % 4 == 0 and year % 100 != 0:
        break
    
print(f"The next leap year after {start} is {year}")