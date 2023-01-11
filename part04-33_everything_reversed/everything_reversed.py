def everything_reversed(strings):
    reversed = []
    for string in strings[::-1]:
        reversed.append(string[::-1])
    return reversed