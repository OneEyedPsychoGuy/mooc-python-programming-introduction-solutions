layers = int(input("Layers: "))
layer = layers
text = ""
for i in range(64 + layers, 64, -1):
    for j in range(64 + layers, i, -1):
        text += chr(j)
    text += chr(i) * (layer * 2 - 1)
    layer -= 1
    for j in range(i + 1, 64 + layers + 1, 1):
        text += chr(j)
    text += "\n"

layer = 2
for i in range(66, 65 + layers, 1):
    for j in range(64 + layers, i, -1):
        text += chr(j)
    text += chr(i) * (layer * 2 - 1)
    layer += 1
    for j in range(i + 1, 64 + layers + 1, 1):
        text += chr(j)
    text += "\n"

print(text)