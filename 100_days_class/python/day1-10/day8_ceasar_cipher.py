from day8_ceasar_art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(direction, text, shift):
    if direction == "encode":
        enc_message = []
        for position in text:
            dex_out = (alphabet.index(position) + shift)
            if dex_out > 25:
                dex_out -= 26
            let_out = alphabet[dex_out]
            enc_message.append(let_out)
        print("The encrypted message is " + "".join(enc_message))
    elif direction == "decode":
        dec_message = []
        for position in text:
            dex_out = (alphabet.index(position) + shift)
            if dex_out > 25:
                dex_out -= 26
            let_out = alphabet[dex_out]
            enc_message.append(let_out)
        print("The decrypted message is " + "".join(dec_message))
    else:
        print(f"The entry needs to be encode or decode not {direction}")
        exit()


ceaser(direction, text, shift)
