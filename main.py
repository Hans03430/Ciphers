from ciphers.cipher.atbash_cipher import AtbashCipher
from ciphers.cipher.caesar_cipher import CaesarCipher
from ciphers.cipher.vigenere_cipher import VigenereCipher
from ciphers.commons.alphabet import Alphabet


if __name__ == '__main__':
    vc = VigenereCipher(key='friends')
    print(vc.decrypt('dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!'))
    a = Alphabet(
        language='en',
        lower='abcdefghijklmnopqrstuvwxyz',
        upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )
    print(a[3, 'UPPER'])