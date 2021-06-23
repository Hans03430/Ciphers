import tracemalloc

from ciphers.cipher.affine_cipher import AffineCipher
from ciphers.cipher.atbash_cipher import AtbashCipher
from ciphers.cipher.caesar_cipher import CaesarCipher
from ciphers.cipher.vigenere_cipher import VigenereCipher
from ciphers.commons.alphabet import Alphabet


if __name__ == '__main__':
    tracemalloc.start()
    vc = AffineCipher(a=7, b=2)

    text = 'Hello World!'
    x = vc.encrypt(text)
    print(x)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**3} KB; Peak was {peak / 10**3} KB")
    tracemalloc.stop()