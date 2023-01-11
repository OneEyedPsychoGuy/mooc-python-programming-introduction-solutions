def play_turn(board: list[list[str]], x: int, y: int, piece: str) -> bool:
    if x < 0 or x > 2 or y < 0 or y > 2 or board[y][x] != "":
        return False
    board[y][x] = piece
    return True