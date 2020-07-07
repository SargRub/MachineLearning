import unicodedata

text_data = [
    'Test!!!! hello. esim. test2...',
    '100% ola!! #HashTag',
    'testText???!!?'
]


def replace_symbols(string: str) -> str:
    new_string = ""
    for character in string:
        if not unicodedata.category(character).startswith('P'):
            new_string += character
    return new_string


new_text = [replace_symbols(string) for string in text_data]
print(new_text)
