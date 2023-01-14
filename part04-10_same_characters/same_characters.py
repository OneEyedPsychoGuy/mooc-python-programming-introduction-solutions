def same_chars(word: str, index1: int, index2: int) -> bool:
    if index1 >= len(word) or index2 >= len(word):
        return False
    return word[index1] == word[index2]