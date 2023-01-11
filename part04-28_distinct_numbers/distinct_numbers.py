def distinct_numbers(numbers):
    distincts = []
    for num in numbers:
        if num not in distincts:
            distincts.append(num)
    return sorted(distincts)