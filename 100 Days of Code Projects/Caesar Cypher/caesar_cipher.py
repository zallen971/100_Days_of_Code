alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#defines encrypt and decrypt function
def caesar(message, shift_num, ciph_direction):
    text_message = ""
    if ciph_direction == "decode":
        shift_num *= -1
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_num
            text_message += alphabet[new_position]
        else:
            text_message += char
    print(f"The encrypted text is: {text_message}")

#The logo
from art import logo
print(logo)
should_continue = True

# Creates a while loop on whether the user wants to continue
# Takes input for encode/decode, the messane, and the shift number
while should_continue:
    direction = input("Type 'encode' to encrypt. Type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    # Makes sure the shift is within the number of the alphabet
    shift = shift % 26
    caesar(message=text, shift_num=shift, ciph_direction=direction)

    # Asks if the user wants to go again or not and exits if no
    result = input("Type 'yes' if you want to go again, or type 'no' to exit.\n")
    if result == "no":
        should_continue = False
        print("now Exiting...")