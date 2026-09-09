from collections.abc import Iterator
from itertools import cycle
from string import ascii_uppercase

ALPHABET = ascii_uppercase
ALPHABET_LENGTH = len(ALPHABET)


def _text_to_ints(text: str) -> list[int]:
    """
    Converts a text string to an integer list (A=0,B=1,...).
    Characters outside A-Z/a-z are removed.

    Raise:
        ValueError if the text contains no letters.
    """
    text_nums = [ALPHABET.index(c) for c in text.upper() if c in ALPHABET]

    if not text_nums:
        raise ValueError(f"The text must contain at least one letter. Got {text}")

    return text_nums


def _get_key_stream(key_nums: list[int]) -> Iterator[int]:
    """Returns a stream of the converted key numbers."""
    return cycle(key_nums)


def encrypt(plaintext: str, key: str) -> str:
    """
    Encrypts plaintext with the given key. Characters outside A-Z/a-z are removed.

    Args:
        plaintext (str): The text to encrypt
        key (str): The key to use
    Returns:
        str: The encrypted text
    """
    plain_text_nums = _text_to_ints(plaintext)
    key_nums = _text_to_ints(key)
    key_stream = _get_key_stream(key_nums)

    cipher = [
        ALPHABET[(p + next(key_stream)) % ALPHABET_LENGTH] for p in plain_text_nums
    ]
    return "".join(cipher)


def decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypts ciphertext with the given key. Characters outside A-Z/a-z are removed.

    Args:
        ciphertext (str): The text to decrypt
        key (str): The key to use
    Returns:
        str: The decrypted text
    """
    cipher_text_nums = _text_to_ints(ciphertext)
    key_nums = _text_to_ints(key)
    key_stream = _get_key_stream(key_nums)

    plaintext = [
        ALPHABET[(c - next(key_stream)) % ALPHABET_LENGTH] for c in cipher_text_nums
    ]
    return "".join(plaintext)
