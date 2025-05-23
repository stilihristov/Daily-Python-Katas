def remove_whitespaces(str):
    return str.replace(' ', '')

spaces = "Hey, this was a test string, full of white spaces"

no_spaces = remove_whitespaces(spaces)

print(no_spaces)