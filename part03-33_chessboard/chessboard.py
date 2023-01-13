def chessboard(length: int):
    rows = 0
    while rows < length:
        if rows % 2 == 0:
            row = "10" * length
        else:
            row = "01" * length
        print(row[0:length])
        rows += 1