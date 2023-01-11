def column_correct(sudoku: list[list[int]], col: int) -> bool:
    nums = []
    for row in sudoku:
        num = row[col]
        if num > 0 and num in nums:
            return False
        nums.append(num)
    return True