word = input("Please type in a word: ")
char = input("Please type in a character: ")

while char in word:
    index = word.find(char)
    if index + 3 <= len(word):
        print(word[index:index + 3])
    
    word = word[index + 1:]