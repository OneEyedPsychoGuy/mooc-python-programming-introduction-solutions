def longest_series_of_neighbours(nums: list[int]):
    longest = 1
    length = 1

    for i in range(len(nums) - 1):
        if abs(nums[i] - nums[i + 1]) == 1:
            length += 1
        else:
            length = 1
        longest = max(length, longest)

    return longest