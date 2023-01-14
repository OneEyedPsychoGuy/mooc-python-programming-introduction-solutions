def no_vowels(string: str):
    vowels = "aeiou"
    for vowel in vowels:
        string = string.replace(vowel, "")
    return string