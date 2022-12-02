def most_common_character(string):
    most = ""
    for char in string:
        if most == "" or string.count(char) > string.count(most):
            most = char
    return most