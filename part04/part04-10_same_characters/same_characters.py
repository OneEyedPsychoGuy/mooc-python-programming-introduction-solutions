def same_chars(word, index1, index2):
    if index1 >= len(word) or index2 >= len(word):
        return False
    return word[index1] == word[index2]