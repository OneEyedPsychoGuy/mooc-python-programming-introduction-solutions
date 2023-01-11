def count_matching_elements(matrix: list[list[int]], search: int) -> int:
    count = 0
    for row in matrix:
        for cell in row:
            if cell == search:
                count += 1
    return count