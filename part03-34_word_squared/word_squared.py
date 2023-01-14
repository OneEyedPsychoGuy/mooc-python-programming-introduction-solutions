def squared(text: str, size: int) -> None:
    rows = 0
    index = 0
    while rows < size:
        row = ""
        while len(row) < size:
            if index >= len(text):
                index = 0
            row += text[index]
            index += 1
        print(row)
        rows += 1