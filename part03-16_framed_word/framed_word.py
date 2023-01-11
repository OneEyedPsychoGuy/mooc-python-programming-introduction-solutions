word = input("Word: ")
half = (28 - len(word)) // 2

print("*" * 30)
if len(word) % 2 == 0:
    print("*" + (" " * half) + word + (" " * half) + "*")
else:
    print("*" + (" " * half) + word + (" " * (half + 1)) + "*")
print("*" * 30)