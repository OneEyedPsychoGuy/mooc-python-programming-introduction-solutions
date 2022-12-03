def block_correct(sudoku: list[list[int]], row: int, col: int) -> bool:
    nums = []
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            num = sudoku[i][j]
            if num > 0 and num in nums:
                return False
            nums.append(num)
    return True