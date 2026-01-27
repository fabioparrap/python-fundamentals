"""
Cifrado César
Ejercicio de manipulación de cadenas
"""

def caesar_cipher(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text.lower():
        if char == " ":
            result += char
        else:
            result += alphabet[(alphabet.index(char) + shift) % 26]

    return result


print(caesar_cipher("hello world", 3))
