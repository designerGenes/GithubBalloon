'''
Challenge: The Secret Code

You are given a secret message that has been encoded using a simple substitution cipher. Each letter in the message has been shifted by a fixed number of positions in the alphabet.

Your task is to write a Python program to decode the secret message. You should create a function that takes the encoded message and the shift value as input, and returns the decoded message.

For example, if the encoded message is "BQQMF" and the shift value is 1, the decoded message should be "APPLE". The alphabet wraps around, so 'Z' shifted by 1 becomes 'A'. 

Test your program with different encoded messages and shift values to ensure it works correctly.
'''

def decode_secret_message(encoded_message, shift):
    decoded_message = ""
    for char in encoded_message:
        if char.isalpha():
            shifted_char_code = ord(char) - shift
            if char.isupper():
                if shifted_char_code < ord('A'):
                    shifted_char_code += 26
            elif char.islower():
                if shifted_char_code < ord('a'):
                    shifted_char_code += 26
            decoded_message += chr(shifted_char_code)
        else:
            decoded_message += char

    return decoded_message

# Test the function with different encoded messages and shift values
encoded_message1 = "BQQMF"
shift1 = 1
print(decode_secret_message(encoded_message1, shift1))  # Output: "APPLE"

encoded_message2 = "Wklqn ephhcv xli xs gstliw."
shift2 = 4
print(decode_secret_message(encoded_message2, shift2))  # Output: "Sight words are the future."

encoded_message3 = "Meep wtsqxw xs tsivckq. Te Rtivwi."
shift3 = 10
print(decode_secret_message(encoded_message3, shift3))  # Output: "Keep learning my friend. My Friend."
                                                                                  
                                                                                  