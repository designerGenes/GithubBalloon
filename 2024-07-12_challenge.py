'''
Challenge: Secret Message Decoder

You have intercepted a secret message that is encoded using a simple substitution cipher. Your task is to decode the message by replacing each letter with its corresponding letter from the given substitution key.

The substitution key is provided as a dictionary where keys are the encoded letters and values are the decoded letters. All other characters (such as spaces, punctuation, etc.) should remain unchanged.

Decode the secret message and return the decoded message. The secret message will only contain uppercase letters, spaces, and punctuation.

Example:
Substitution key: {'H': 'A', 'I': 'B', 'S': 'C', 'P': 'D', 'Y': 'E', ' ': ' ', '!': '!'}
Secret message: "HIP HIP HOORAY!"

Decoded message: "ABCD ABC DEEDB!"
'''

substitution_key = {'H': 'A', 'I': 'B', 'S': 'C', 'P': 'D', 'Y': 'E', ' ': ' ', '!': '!'}
secret_message = "HIP HIP HOORAY!"

decoded_message = ''.join([substitution_key.get(char, char) for char in secret_message])
decoded_message
