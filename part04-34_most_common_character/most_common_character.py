def most_common_character(string: str) -> str:
    common = string[0]
    for char in string:
        if string.count(char) > string.count(common):
            common = char
    return common