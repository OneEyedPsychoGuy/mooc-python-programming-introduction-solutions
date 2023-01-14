def line(times: int, character: str) -> None:
    if character == "":
        character = "*"
    print(character[0] * times)

def triangle(height: int) -> None:
    length = 1
    while length <= height:
        line(length, "#")
        length += 1