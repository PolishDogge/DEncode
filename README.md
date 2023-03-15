This repository contains Python code for encoding and decoding a message using a custom algorithm.

# How to Use
## Encoding
To encode a message, call the DEncode function and pass the message and a move value as parameters. The function will return an encoded list.

```
from Dbase import DEncode

message = "Hello, World!"
move = 5
encoded_message = DEncode(message, move)
print(encoded_message)
```
## Decoding
To decode an encoded message, call the DDecode function and pass the encoded list as a parameter. The function will return the original message.

```
from Dbase import DDecode

encoded_message = [[2, 108], [2, 101], [2, 111], [0, 89], [10, 35], [2, 117], [2, 106], [2, 117], [0, -17], [2, 119], [2, 110], [2, 118], [10, 33], 5, 5]
decoded_message = DDecode(encoded_message)
print(decoded_message)
```

# How it Works
The encoding algorithm converts each character in the message into a list of values based on its type. Upper and lowercase letters are differentiated, special characters are converted to their ASCII values, spaces are assigned a random value, and numbers are stored as integers.

A move value is subtracted from the ASCII value of each character, and a random number is added to the result if a condition is met. The resulting values are then stored in a list and returned as the encoded message.

The decoding algorithm takes the encoded list and iterates over each item in the list. If the value is equal to the first value in the item, it determines what type of character it is based on the value and appends the appropriate character to the decoded message. If the value is not equal to the first value in the item, it subtracts the move value from the value and appends the resulting character to the decoded message.
