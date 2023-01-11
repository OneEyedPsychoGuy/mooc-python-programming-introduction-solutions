def shortest(words):
    shortest = ""
    for word in words:
        if len(word) < len(shortest) or shortest == "":
            shortest = word
    return shortest