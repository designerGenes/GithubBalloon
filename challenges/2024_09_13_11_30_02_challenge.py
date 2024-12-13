'''
Challenge: Secret Message Decoder

You have intercepted a secret message encoded using a simple substitution cipher. The cipher alphabet has been shifted by a certain number of positions. Your task is to decode the secret message by shifting the characters back to their original positions.

Write a Python program that takes the encoded message and the shift value as input, and outputs the decoded message. The encoded message will consist only of uppercase letters (A-Z) and spaces.

Example:
Input:
Encoded message: "WKH HDJOH LV LQ SODB; PH WKH ODVW ZDB."
Shift value: 3

Output:
Decoded message: "THE EAGLE IS IN PLAY; MEET AT NINE."
'''

def decode_secret_message(encoded_message, shift):
    decoded_message = ""
    for char in encoded_message:
        if char == ' ':
            decoded_message += char
        else:
            decoded_message += chr(((ord(char) - shift - 65) % 26) + 65)
    return decoded_message

encoded_message = "WKH HDJOH LV LQ SODB; PH WKH ODVW ZDB."
shift_value = 3
decoded_message = decode_secret_message(encoded_message, shift_value)
print("Decoded message:", decoded_message)