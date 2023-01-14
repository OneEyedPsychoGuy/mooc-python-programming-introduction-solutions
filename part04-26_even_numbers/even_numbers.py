def even_numbers(nums: list[int]) -> list[int]:
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums