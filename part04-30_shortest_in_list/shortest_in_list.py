def shortest(words: list[str]) -> str:
    shortest = ""
    for word in words:
        if shortest == "" or len(word) < len(shortest):
            shortest = word
    return shortest