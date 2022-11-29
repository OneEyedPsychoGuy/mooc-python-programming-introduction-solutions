def line(times, characters):
    if characters == "":
        characters = "*"
    print(characters[0] * times)

def triangle(height):
    length = 1
    while length <= height:
        line(length, "#")
        length += 1