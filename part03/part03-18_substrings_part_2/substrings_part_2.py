text = input("Please type in a string: ")
index = len(text)

while index > 0:
    index -= 1
    print(text[index:])