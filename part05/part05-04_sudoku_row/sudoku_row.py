def row_correct(sudoku: list[list[int]], row: int) -> bool:
    nums = []
    for num in sudoku[row]:
        if num > 0 and num in nums:
            return False
        nums.append(num)
    return True