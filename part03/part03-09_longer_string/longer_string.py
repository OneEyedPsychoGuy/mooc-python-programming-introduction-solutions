text1 = input("Please type in string 1: ")
text2 = input("Please type in string 2: ")

if len(text1) > len(text2):
    print(f"{text1} is longer")
elif len(text1) < len(text2):
    print(f"{text2} is longer")
else:
    print("The strings are equally long")