import sys

from vigenere import decrypt, encrypt


def main():
    """ Runs a terminal program to decrypt and encrypt text using the Vigenére cipher."""

    print("\n=========VIGENÉRE ENCRYPTER / DECRYPTER=========\n")
    print("Note: Characters outside A-Z/a-z are removed.\n")

    while True:
        request = input("Enter E to encrypt, D to decrypt: ").strip().upper()
        if request in ["E", "D"]:
            break
        print("Invalid input. Please enter either E to encrypt or D to decrypt")

    if request == "E":
        prompt_text = "Enter plain text: "
        result_label = "Encrypted text: "
        cypher_func = encrypt
    else:
        prompt_text = "Enter cipher text: "
        result_label = "Encrypted text: "
        cypher_func = decrypt

    text = input(prompt_text)
    key_text = input("Enter key: ")

    try:
        result = cypher_func(text, key_text)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print(f"{result_label} {result}")


if __name__ == "__main__":
    main()
