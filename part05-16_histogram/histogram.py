def histogram(word: str) -> None:
    chars = {}
    for char in word:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    
    for char, count in chars.items():
        print(f"{char} {'*' * count}")