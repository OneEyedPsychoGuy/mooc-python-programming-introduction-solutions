def no_vowels(string: str) -> str:
    vowels = "aeiou"
    for vowel in vowels:
        string = string.replace(vowel, "")
    return string