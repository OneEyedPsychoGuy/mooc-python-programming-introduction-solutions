def spruce(size: int) -> None:
    print("a spruce!")
    rows = 1
    while rows <= size:
        spaces = " " * (size - rows)
        stars = "*" * (rows * 2 - 1)
        print(f"{spaces}{stars}{spaces}")
        rows += 1
    print(f"{' ' * (size - 1)}*{' ' * (size - 1)}")