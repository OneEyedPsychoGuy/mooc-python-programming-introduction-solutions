text = input("Please type in a string: ")

if text[1] == text[len(text) - 2]:
    print(f"The second and the second to last characters are {text[1]}")
else:
    print("The second and the second to last characters are different")