def times_ten(start: int, end: int) -> dict[int, int]:
    tens_dict = {}
    for num in range(start, end + 1):
        tens_dict[num] = num * 10
    return tens_dict