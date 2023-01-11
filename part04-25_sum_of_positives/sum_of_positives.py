def sum_of_positives(numbers):
    sum = 0
    for num in numbers:
        if num > 0:
            sum += num
    return sum