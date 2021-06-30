from ciphers.cipher.base_cipher import BaseCipher
from ciphers.cipher.caesar_cipher import CaesarCipher
from ciphers.commons.alphabet import Alphabet
from ciphers.commons.constants import LANGUAGES
from typing import Generator


class VigenereCipher(BaseCipher):
    '''Class that defines the Vigenere Cipher for a alphabet. Uses english by
    default but accepts custom alphabets.
    
    Attributes
    ----------
    key: str
        Keyword to encrypt/decrypt the text.

    __shifts: CaesarCipher
        The Caesar cipher that simulate the tabula recta.

    __key_ord: List[int]
        Numeric order for each letter of the key.
    '''
    __slots__ = ['__key', '__shifts', '__key_ord']

    def __init__(self, key='LEMON', alphabet: Alphabet=None) -> None:
        '''Create a Vigenere Cipher class.
        '''
        if len(key) == 0:
            raise AttributeError('The key can\'t be empty.')
        # Add alphabet
        if alphabet:
            self.alphabet = alphabet
        else:
            self.alphabet = LANGUAGES['en']

        self.key = key

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str) -> None:
        self.__key = key
        self.__key_ord = [
            self.alphabet[c]
            if c.islower()
            else self.alphabet[c]
            for c in self.key
        ]

    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet

    @alphabet.setter
    def alphabet(self, alphabet: Alphabet) -> None:
        self._alphabet = alphabet
        # Create the a caesar cipher
        self.__shifts = CaesarCipher(alphabet=self.alphabet)
        
    def decrypt(self, text:str) -> str:
        '''Decrypt a encrypted text using the Vigenere cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to decrypt.
        '''
        def __decrypt_generator(text: str) -> Generator:
            '''Generator tha returns each character decrypted.
            
            Parameters
            ----------
            text: str
                The text to decrypt.

            Yields
            ------
            character: str
                The decrypted character
            '''
            for i, character in enumerate(text):
                # Find decryption in tabula recta
                self.__shifts.shift = self.__key_ord[i % len(self.key)]
                # Yield result
                yield self.__shifts.decrypt(character)
        
        return ''.join(__decrypt_generator(text))


    def encrypt(self, text:str) -> str:
        '''encrypt a encrypted text using the Vigenere cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to encrypt.
        '''
        def __encrypt_generator(text: str) -> Generator:
            '''Generator tha returns each character encrypted.
            
            Parameters
            ----------
            text: str
                The text to encrypt.

            Yields
            ------
            character: str
                The encrypted character
            '''
            for i, character in enumerate(text):
                # Find decryption in tabula recta
                self.__shifts.shift = self.__key_ord[i % len(self.key)]
                # Yield result
                yield self.__shifts.encrypt(character)
        
        return ''.join(__encrypt_generator(text))