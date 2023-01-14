def line(times: int, character: str) -> None:
    if character == "":
        character = "*"
    print(character[0] * times)

def rectangle(length: int, height: int, character: str) -> None:
    while height > 0:
        line(length, character)
        height -= 1

def triangle(height: int, character: str) -> None:
    length = 1
    while length <= height:
        line(length, character)
        length += 1

def shape(length: int, tri_char: str, height: int, rect_char: str) -> None:
    triangle(length, tri_char)
    rectangle(length, height, rect_char)