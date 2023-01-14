def no_shouting(strings: list[str]):
    lowers = []
    for string in strings:
        if not string.isupper():
            lowers.append(string)
    return lowers