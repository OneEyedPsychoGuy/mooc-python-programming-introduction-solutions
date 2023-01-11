def line(times, characters):
    if characters == "":
        characters = "*"
    print(characters[0] * times)

def box_of_hashes(height):
    while height > 0:
        line(10, "#")
        height -= 1