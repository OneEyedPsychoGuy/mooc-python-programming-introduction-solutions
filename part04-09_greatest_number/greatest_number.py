def greatest_number(num1, num2, num3):
    greatest = num1
    if num2 >= num1 and num2 >= num3:
        greatest = num2
    elif num3 >= num1:
        greatest = num3
    return greatest