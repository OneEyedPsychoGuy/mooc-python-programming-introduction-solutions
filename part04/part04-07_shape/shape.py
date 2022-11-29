def line(times, characters):
    if characters == "":
        characters = "*"
    print(characters[0] * times)

def rectangle(length, height, character):
    while height > 0:
        line(length, character)
        height -= 1

def triangle(height, character):
    length = 1
    while length <= height:
        line(length, character)
        length += 1

def shape(length, tri_char, height, rect_char):
    triangle(length, tri_char)
    rectangle(length, height, rect_char)