text = input("Please type in a string: ")

if len(text) > 1 and text[1] == text[-2]:
    print(f"The second and the second to last characters are {text[1]}")
else:
    print("The second and the second to last characters are different")