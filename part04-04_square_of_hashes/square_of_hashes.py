def line(times, characters):
    if characters == "":
        characters = "*"
    print(characters[0] * times)

def square_of_hashes(length):
    height = length
    while height > 0:
        line(length, "#")
        height -= 1