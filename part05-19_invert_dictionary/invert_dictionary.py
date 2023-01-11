def invert(dictionary: dict) -> None:
    inverted = {}
    for key, value in dictionary.items():
        inverted[value] = key
    
    dictionary.clear()
    for key, value in inverted.items():
        dictionary[key] = value