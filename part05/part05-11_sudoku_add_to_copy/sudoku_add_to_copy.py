def copy_and_add(sudoku: list[list[int]], row: int, col: int, num: int) -> list[list[int]]:
    copy = []
    for sudoku_row in sudoku:
        copy.append(sudoku_row[:])
    copy[row][col] = num
    return copy