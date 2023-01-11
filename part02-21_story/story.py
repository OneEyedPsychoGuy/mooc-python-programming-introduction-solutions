story, prev = "", ""

while True:
    next = input("Please type in a word: ")
    if next == prev or next == "end":
        break
    prev = next
    story += next + " "

print(story)