text = input("Please type in a string: ")
vowels = "aeo"
index = 0

while index < len(vowels):
    vowel = vowels[index]
    if vowel in text:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
    index += 1