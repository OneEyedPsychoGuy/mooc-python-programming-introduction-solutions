def list_sum(nums1: list[int], nums2: list[int]):
    sums = []
    for i in range(len(nums1)):
        sums.append(nums1[i] + nums2[i])
    return sums