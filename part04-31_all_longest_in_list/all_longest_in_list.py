def all_the_longest(words: list[str]) -> list[str]:
    longest_words = []
    longest = -1

    for word in words:
        if len(word) > longest:
            longest = len(word)
    for word in words:
        if len(word) == longest:
            longest_words.append(word)
    
    return longest_words