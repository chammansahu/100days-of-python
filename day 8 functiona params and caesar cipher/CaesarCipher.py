

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type encode to encrypt ,type decode to decrypt:\n")
#take input
text = input("Enter Text You want to encrypt\n")
shift= int(input("Type the shift number:\n"))

def encrypt(text,shift):
    str2=""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        str2+=new_letter;
    print(f"the encrypted message is {str2}")
    decode=str2    
    return decode  


def decrypt(cipher_text,shift):
    str3=""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        str3+=new_letter;
    print(f"the  message is {str3}")

if direction == "encode":
    encrypt(text, shift)
else:    
    decode = encrypt(text, shift)
    decrypt(decode,shift)
    
