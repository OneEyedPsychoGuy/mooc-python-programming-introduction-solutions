def longest(strings: list[str]) -> str:
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest