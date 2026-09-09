import pytest

from vigenere import _text_to_ints, decrypt, encrypt


def test_text_to_ints_raises_value_error_on_only_non_az():
    with pytest.raises(ValueError):
        _text_to_ints("12345")


def test_text_to_ints_returns_correct_ints():
    assert _text_to_ints("AZ") == [0, 25]
    assert _text_to_ints("HelloYou") == [7, 4, 11, 11, 14, 24, 14, 20]


def test_text_to_ints_ignores_non_az():
    assert _text_to_ints("17AZ+=27") == [0, 25]
    assert _text_to_ints("//Hello _you_!") == [7, 4, 11, 11, 14, 24, 14, 20]


@pytest.mark.parametrize("invalid_key", ["", "123", "!!"])
def test_encrypt_throws_value_error_on_invalid_key(invalid_key):
    with pytest.raises(ValueError):
        encrypt("Test", invalid_key)


@pytest.mark.parametrize("invalid_text", ["", "234", "!!!"])
def test_encrypt_raises_value_error_on_invalid_plaintext(invalid_text):
    with pytest.raises(ValueError):
        encrypt("", invalid_text)


def test_encrypt_returns_correct_cipher():
    assert encrypt("A B C D", "B") == "BCDE"


@pytest.mark.parametrize("invalid_key", ["", "123", "!!"])
def test_decrypt_raises_value_error_on_invalid_key(invalid_key):
    with pytest.raises(ValueError):
        decrypt("Test", invalid_key)


@pytest.mark.parametrize("invalid_text", ["", "234", "!!!"])
def test_decrypt_raises_value_error_on_invalid_plaintext(invalid_text):
    with pytest.raises(ValueError):
        decrypt(invalid_text, "Test")


def test_decrypt_returns_correct_cipher():
    assert decrypt("XYZ", "B") == "WXY"


def test_decrypt_returns_encrypted_with_same_key():
    assert (
        decrypt(encrypt("Testing Vigenere Symmetry", "TEST"), "TEST")
        == "TESTINGVIGENERESYMMETRY"
    )
