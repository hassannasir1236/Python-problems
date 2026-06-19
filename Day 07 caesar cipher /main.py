def caesar_cipher(text, shift):

    small_letters = [
        'a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z'
    ]

    capital_letters = [
        'A','B','C','D','E','F','G','H','I','J',
        'K','L','M','N','O','P','Q','R','S','T',
        'U','V','W','X','Y','Z'
    ]

    encrypt = ""

    for char in text:

        # Uppercase
        if char.isupper():
            if char in capital_letters:
                i = capital_letters.index(char)
                encrypt += capital_letters[(i + shift) % 26]
            else:
                encrypt += char

        # Lowercase
        elif char.islower():
            if char in small_letters:
                i = small_letters.index(char)
                encrypt += small_letters[(i + shift) % 26]
            else:
                encrypt += char

        # Spaces / symbols
        else:
            encrypt += char

    print("Encrypted:", encrypt)


# Input
message = input("Enter message: ")
shift = int(input("Enter shift number: "))

caesar_cipher(message, shift)