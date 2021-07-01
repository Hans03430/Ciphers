import math

from ciphers.cipher.base_cipher import BaseCipher
from ciphers.commons.alphabet import Alphabet
from ciphers.commons.constants import LANGUAGES


class AffineCipher(BaseCipher):
    '''Class that defines the Affine Cipher for a alphabet. Uses english by
    default but accepts custom alphabets.
    
    Paramters
    ---------
    __a: int
        One of the keys of the cipher.

    __b: int
        One of the keys of the cipher.
    '''

    __slots__ = ['__a', '__b']

    def __init__(self, a: int=1, b: int=1, alphabet: Alphabet=None) -> None:
        '''Create a Atbash Cipher class.
        '''
        # Add alphabet
        if alphabet:
            self.alphabet = alphabet
        else:
            self.alphabet = LANGUAGES['en']
        # Add keys
        self.a = a
        self.b = b

    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet

    @alphabet.setter
    def alphabet(self, alphabet: Alphabet) -> None:
        self._alphabet = alphabet

    @property
    def b(self) -> int:
        return self.__b
    
    @b.setter
    def b(self, b: int) -> None:
        self.__b = b

    @property
    def a(self) -> int:
        return self.__a
    
    @a.setter
    def a(self, a: int) -> None:
        # Check if 'a' and the length of the alphabet are coprimes.
        if math.gcd(a, len(self.alphabet)) == 1:
            self.__a = a
        else:
            raise AttributeError(
                f'Key "a" and the length of the Alphabet must be coprimes.'
            )

    def decrypt(self, text:str) -> str:
        '''Decrypt a encrypted text using the Atbash cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to decrypt.
        '''
        decrypted_generator = (
            self.alphabet[
                (
                    (
                        pow(self.a, -1, len(self.alphabet))
                        * (self.alphabet[character] - self.b)
                    ) 
                    % len(self.alphabet)
                ),
                'lower'
            ]
            if self.alphabet.is_lower(character)
            else self.alphabet[
                (
                    (
                        pow(self.a, -1, len(self.alphabet))
                        * (self.alphabet[character] - self.b)
                    ) % len(self.alphabet)
                ),
                'upper'
            ]
            if self.alphabet.is_upper(character)
            else character
            for character in text
        )
        # Return the decrypted text
        return ''.join(decrypted_generator)

    def encrypt(self, text:str) -> str:
        '''encrypt a encrypted text using the Atbash cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to encrypt.
        '''
        encrypted_generator = (
            self.alphabet[
                (
                    ((self.a * self.alphabet[character]) + self.b) 
                    % len(self.alphabet)
                ),
                'lower'
            ]
            if self.alphabet.is_lower(character)
            else self.alphabet[
                (
                    ((self.a * self.alphabet[character]) + self.b) 
                    % len(self.alphabet)
                ),
                'upper'
            ]
            if self.alphabet.is_upper(character)
            else character
            for character in text
        )
        # Return the decrypted text
        return ''.join(encrypted_generator)