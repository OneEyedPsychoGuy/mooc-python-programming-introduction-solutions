def line(times: int, character: str):
    if character == "":
        character = "*"
    print(character[0] * times)

def square_of_hashes(length: int):
    height = length
    while height > 0:
        line(length, "#")
        height -= 1