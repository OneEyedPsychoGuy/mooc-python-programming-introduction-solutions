def length_of_longest(words: list[str]) -> int:
    longest = -1
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest