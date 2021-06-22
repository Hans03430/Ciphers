# Ciphers
Ciphers is a Python module that implements ciphers for plain text. A custom
language can be used but by default, it uses English.

# Available Ciphers
* Atbash Cipher
* Caesar Cipher
* Vigenère Cipher

# Example
## Default language
    from ciphers.cipher.caesar_cipher import CaesarCipher


    ce = CaesarCipher(shift=3)
    print(ce.encrypt('Hello world'))

## Custom language
    from ciphers.cipher.caesar_cipher import CaesarCipher
    from ciphers.commons.alphabet import Alphabet


    a = Alphabet(
        language='es',
        lower='abcdefghijklmnñopqrstuvwxyz',
        upper='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    )
    ce = CaesarCipher(shift=3, language=a)
    print(ce.encrypt('Hello world'))