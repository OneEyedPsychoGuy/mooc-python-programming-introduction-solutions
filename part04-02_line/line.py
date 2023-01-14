def line(times: int, character: str) -> None:
    if character == "":
        character = "*"
    print(character[0] * times)