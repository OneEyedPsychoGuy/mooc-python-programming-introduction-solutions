def line(times: int, character: str):
    if character == "":
        character = "*"
    print(character[0] * times)