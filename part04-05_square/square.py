def line(times: int, character: str) -> None:
    if character == "":
        character = "*"
    print(character[0] * times)

def square(length: int, character: str) -> None:
    height = length
    while height > 0:
        line(length, character)
        height -= 1