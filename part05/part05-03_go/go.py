def who_won(board: list[list[int]]) -> int:
    p1, p2 = 0, 0
    for row in board:
        for cell in row:
            if cell == 1:
                p1 += 1
            elif cell == 2:
                p2 += 1
    
    if p1 > p2:
        return 1
    elif p1 < p2:
        return 2
    else:
        return 0