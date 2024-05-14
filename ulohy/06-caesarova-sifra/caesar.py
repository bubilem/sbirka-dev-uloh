def caesar_encrypt(input_text: str, offset: int = 3)->str:
    output = ""
    for char in input_text:
        output += chr((ord(char) + offset - ord("A")) % 26 + ord("A")) if char.isalpha() else char        
    return output

def caesar_decrypt(input_text: str, offset: int = 3)->str:
    output = ""
    for char in input_text:
        output += chr((ord(char) - offset - ord("A")) % 26 + ord("A")) if char.isalpha() else char
    return output


open_text = "AHOJ, JAK SE VEDE?"
print(open_text)
crypted_text = caesar_encrypt(open_text)
print(crypted_text)
decrypted_text = caesar_decrypt(crypted_text)
print(decrypted_text)