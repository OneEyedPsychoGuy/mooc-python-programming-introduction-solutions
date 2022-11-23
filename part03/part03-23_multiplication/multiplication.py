num = int(input("Please type in a number: "))
operand1 = 1

while operand1 <= num:
    operand2 = 1
    while operand2 <= num:
        print(f"{operand1} x {operand2} = {operand1 * operand2}")
        operand2 += 1
    operand1 += 1