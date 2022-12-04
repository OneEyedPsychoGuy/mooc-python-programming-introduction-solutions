def print_sudoku(sudoku: list[list[int]]) -> None:
    output = ""
    for row in range(9):
        if row == 3 or row == 6:
            output += "\n"
        
        for col in range(9):
            if col == 3 or col == 6:
                output += " "

            cell = sudoku[row][col]
            if cell == 0:
                output += "_ "
            else:
                output += str(cell) + " "
        output += "\n"
        
    print(output)

def add_number(sudoku: list[list[int]], row: int, col: int, num: int) -> None:  
    sudoku[row][col] = num