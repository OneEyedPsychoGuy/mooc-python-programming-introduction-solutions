def no_shouting(strings):
    lowers = []
    for string in strings:
        if not string.isupper():
            lowers.append(string)
    return lowers