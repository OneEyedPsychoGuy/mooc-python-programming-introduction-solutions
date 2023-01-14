def line(times: int, character: str) -> None:
    if character == "":
        character = "*"
    print(character[0] * times)

def square_of_hashes(length: int) -> None:
    height = length
    while height > 0:
        line(length, "#")
        height -= 1