def distinct_numbers(nums: list[int]):
    distincts = []
    for num in nums:
        if num not in distincts:
            distincts.append(num)
    return sorted(distincts)