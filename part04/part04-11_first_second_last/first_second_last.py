def first_word(sentence):
    return sentence.split(" ")[0]

def second_word(sentence):
    return sentence.split(" ")[1]

def last_word(sentence):
    words = sentence.split(" ")
    return words[len(words) - 1]