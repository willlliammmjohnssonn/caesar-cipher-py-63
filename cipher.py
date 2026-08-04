def encrypt(text, shift):
    res = ''
    for char in text:
        if char.isalpha():