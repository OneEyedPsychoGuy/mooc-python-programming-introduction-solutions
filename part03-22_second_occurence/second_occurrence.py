text = input("Please type in a string: ")
sub = input("Please type in a substring: ")
index1 = text.find(sub)
index2 = -1

if index1 != -1:
    text = text[len(sub) + index1:]
    index2 = text.find(sub)

if index2 != -1:
    print(f"The second occurrence of the substring is at index {index1 + index2 + len(sub)}.")
else:
    print("The substring does not occur twice in the string.")