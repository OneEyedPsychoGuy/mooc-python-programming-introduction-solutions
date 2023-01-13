def sum_of_positives(nums: list[int]):
    sum = 0
    for num in nums:
        if num > 0:
            sum += num
    return sum