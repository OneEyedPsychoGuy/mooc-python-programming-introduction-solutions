def formatted(floats: list[float]) -> list[str]:
    formatted = []
    for num in floats:
        formatted.append(f"{num:.2f}")
    return formatted