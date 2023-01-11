def line(times, characters):
    if characters == "":
        characters = "*"
    print(characters[0] * times)

def square(length, character):
    height = length
    while height > 0:
        line(length, character)
        height -= 1