def greatest_number(num1: int, num2: int, num3: int) -> int:
    greatest = num1
    if num2 >= num1 and num2 >= num3:
        greatest = num2
    elif num3 >= num1:
        greatest = num3
    return greatest