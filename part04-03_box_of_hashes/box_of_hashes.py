def line(times: int, character: str) -> None:
    if character == "":
        character = "*"
    print(character[0] * times)

def box_of_hashes(height: int) -> None:
    while height > 0:
        line(10, "#")
        height -= 1