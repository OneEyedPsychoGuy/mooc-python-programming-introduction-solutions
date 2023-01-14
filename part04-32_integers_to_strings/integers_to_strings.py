def formatted(floats: list[float]):
    formatted = []
    for num in floats:
        formatted.append(f"{num:.2f}")
    return formatted