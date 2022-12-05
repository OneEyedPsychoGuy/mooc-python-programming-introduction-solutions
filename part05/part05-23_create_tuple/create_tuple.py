def create_tuple(x: int, y: int, z: int) -> tuple[int, int, int]:
    return (
        min(x, y, z),
        max(x, y, z),
        x + y + z
    )