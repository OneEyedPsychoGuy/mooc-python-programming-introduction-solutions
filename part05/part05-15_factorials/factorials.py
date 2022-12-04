def factorials(n: int) -> dict[int, int]:
    facts = {1 : 1}
    for i in range(2, n+1):
        facts[i] = facts[i - 1] * i
    return facts