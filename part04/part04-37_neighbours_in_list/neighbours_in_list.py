def longest_series_of_neighbours(numbers):
    longest = 1
    length = 1

    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) == 1:
            length += 1
        else:
            length = 1
        longest = max(length, longest)

    return longest