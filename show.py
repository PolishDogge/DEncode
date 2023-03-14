from Dbase import DEncode, DDecode

def main():
    print('Welcome to the Dbase Encryption Program')
    print('Would you like to encrypt or decrypt a message?')
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Exit')
    x = int(input())
    if x == 1:
        encrypt()
    elif x == 2:
        decrypt()
    elif x == 3:
        exit()
    else:
        print('Please enter a valid number')
        main()
    

def decrypt():
    print('Please enter a message to decrypt')
    x = input()
    print('Your decrypted message is:')
    print(DDecode(x))
    exit()


def encrypt():
    print('Please enter a message to encrypt')
    x = input()
    print('Please enter a number to move the characters by')
    y = int(input())
    print('Your encrypted message is:')
    print(DEncode(x, y))
    exit()


main()
