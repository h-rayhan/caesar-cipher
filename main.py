import sys
from art import logo
def main():
    print(logo)
    while True:
        direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
        while direction not in ['encode', 'decode']:
            print("Sorry, that's not a valid input. Please try again.\n")
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

        text = input("Type your message:\n").lower()

        while True:
            try:
                shift = int(input("Type the shift number:\n"))
                if shift < 0:
                    raise ValueError
                break
            except ValueError:
                print("Sorry, that's not a valid shift! Please enter a non-negative integer.")

        caesar(given_text=text, shift_amount=shift, cipher_direction=direction)

        again = input("Would you like to run the program again? (y/n)\n")
        if again == 'n':
            break
        else:
            pass


def caesar(given_text, shift_amount, cipher_direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    output = ""
    if cipher_direction == "decode":
        shift_amount *= - 1
    for char in given_text:
        if char in alphabet:
            position = (alphabet.index(char) + shift_amount) % 26
            output += alphabet[position]
        else:
            output += char

    print(f"\nThe {cipher_direction}d text is {output}\n")


main()
