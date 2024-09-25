'''
Challenge: In a hidden message, each letter is represented by a specific sequence of bits. Given a string of bits, decode the message by converting each group of 7 bits into its corresponding ASCII character. Return the decoded message as a string. Note that the input string is guaranteed to be a valid sequence of 7-bit ASCII characters.
'''

binary_string = "010010000110100100101100"
decoded_message = ""

for i in range(0, len(binary_string), 7):
    binary_char = binary_string[i:i+7]
    decimal_char = int(binary_char, 2)
    decoded_message += chr(decimal_char)

print(decoded_message)
