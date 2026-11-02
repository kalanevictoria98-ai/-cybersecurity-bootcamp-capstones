"""
cipher.py - Caesar Cipher Encoder

This module encodes a message by shifting each alphabetical character
15 places forward. The alphabet is treated as cyclical.
"""


def encode_message(message):
    """
    Encodes a message using a Caesar cipher with a shift of 15.

    Each letter is replaced by the 15th letter after it in the alphabet.
    The shift wraps around from z to a. Uppercase and lowercase are
    handled separately. Non-alphabetic characters are left unchanged.

    Args:
        message (str): The string to be encoded.

    Returns:
        str: The encoded string.
    """
    encoded = ""
    shift = 15

    for char in message:
        # Handle lowercase letters
        if 'a' <= char <= 'z':
            new_char_code = (ord(char) - ord('a') + shift) % 26 + ord('a')
            encoded += chr(new_char_code)
        # Handle uppercase letters
        elif 'A' <= char <= 'Z':
            new_char_code = (ord(char) - ord('A') + shift) % 26 + ord('A')
            encoded += chr(new_char_code)
        else:
            # Keep spaces and punctuation unchanged
            encoded += char

    return encoded


if __name__ == "__main__":
    """Main execution block to get user input and print the encoded message."""
    my_message = input("Enter message to encode: ")
    print("Encoded message:", encode_message(my_message))
