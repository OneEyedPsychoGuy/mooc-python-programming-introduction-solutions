nums = [1, 2, 3, 4, 5]
while True:
    index = int(input("Index: "))
    if index == -1:
        break
    if index < 0 or index >= len(nums):
        print("Index is out of range")
    value = int(input("New value: "))
    nums[index] = value
    print(nums)