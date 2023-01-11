def sudoku_grid_correct(sudoku: list[list[int]]) -> bool:
    for i in range(9):
        if not (row_correct(sudoku, i) and column_correct(sudoku, i)):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_correct(sudoku, i, j):
                return False
    return True

def row_correct(sudoku: list[list[int]], row: int) -> bool:
    nums = []
    for num in sudoku[row]:
        if num > 0 and num in nums:
            return False
        nums.append(num)
    return True

def column_correct(sudoku: list[list[int]], col: int) -> bool:
    nums = []
    for row in sudoku:
        num = row[col]
        if num > 0 and num in nums:
            return False
        nums.append(num)
    return True

def block_correct(sudoku: list[list[int]], row: int, col: int) -> bool:
    nums = []
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            num = sudoku[i][j]
            if num > 0 and num in nums:
                return False
            nums.append(num)
    return True