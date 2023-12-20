alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#defines encrypt and decrypt function
def caesar(message, shift_num, ciph_direction):
    text_message = ""
    if ciph_direction == "decode":
        shift_num *= -1
    for letter in message:
        position = alphabet.index(letter)
        new_position = position + shift_num
        text_message += alphabet[new_position]
    print(f"The encrypted text is: {text_message}")

# takes input for encode/decode, the messane, and the shift number
direction = input("Type 'encode' to encrypt. Type 'decode' to decrypt:\n")
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))


#The logo
from art import logo
print(logo)


#Calls the function that corresponds with the users direction input
caesar(message=text, shift_num=shift, ciph_direction=direction)