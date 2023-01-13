def first_word(sentence: str):
    return sentence.split(" ")[0]

def second_word(sentence: str):
    return sentence.split(" ")[1]

def last_word(sentence: str):
    words = sentence.split(" ")
    return words[len(words) - 1]