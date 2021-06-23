import math

from ciphers.cipher.base_cipher import BaseCipher
from ciphers.commons.alphabet import Alphabet
from ciphers.commons.constants import languages


class AffineCipher(BaseCipher):
    '''Class that defines the Affine Cipher for a language. Uses english by
    default but accepts custom languages.
    
    Paramters
    ---------
    __a: int
        One of the keys of the cipher.

    __b: int
        One of the keys of the cipher.
    '''

    __slots__ = ['__a', '__b']

    def __init__(self, a: int=1, b: int=1, language: Alphabet=None) -> None:
        '''Create a Atbash Cipher class.
        '''
        # Add language
        if language:
            self.language = language
        else:
            self.language = languages['en']
        # Add keys
        self.a = a
        self.b = b

    @property
    def language(self) -> Alphabet:
        return self._language

    @language.setter
    def language(self, language: Alphabet) -> None:
        self._language = language

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
        if math.gcd(a, len(self.language)) == 1:
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
            self.language[
                (
                    (
                        pow(self.a, -1, len(self.language))
                        * (self.language[character] - self.b)
                    ) 
                    % len(self.language)
                ),
                'lower'
            ]
            if character.islower()
            else self.language[
                (
                    (
                        pow(self.a, -1, len(self.language))
                        * (self.language[character] - self.b)
                    ) % len(self.language)
                ),
                'upper'
            ]
            if character.isupper()
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
            self.language[
                (
                    ((self.a * self.language[character]) + self.b) 
                    % len(self.language)
                ),
                'lower'
            ]
            if character.islower()
            else self.language[
                (
                    ((self.a * self.language[character]) + self.b) 
                    % len(self.language)
                ),
                'upper'
            ]
            if character.isupper()
            else character
            for character in text
        )
        # Return the decrypted text
        return ''.join(encrypted_generator)