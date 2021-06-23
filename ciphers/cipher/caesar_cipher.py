from ciphers.cipher.base_cipher import BaseCipher
from ciphers.commons.alphabet import Alphabet
from ciphers.commons.constants import languages


class CaesarCipher(BaseCipher):
    '''Class that defines the Caesar Cipher for a language. Uses english by
    default but accepts custom languages.
    
    Attributes
    ----------
    shift: int
        The amount of letters to shift for the encryption/decryption.
    '''
    __slots__ = ['shift']

    def __init__(self, shift: int=3, language: Alphabet=None) -> None:
        '''Create a Caesar Cipher class.
        '''
        if shift < 0:
            raise AttributeError(
                'The amount of times to shift a letter can\'t be negative.'
            )
            
        self.shift = shift
        # Add language
        if language:
            self.language = language
        else:
            self.language = languages['en']

    @property
    def language(self) -> Alphabet:
        return self._language

    @language.setter
    def language(self, language: Alphabet) -> None:
        self._language = language

    def decrypt(self, text:str) -> str:
        '''Decrypt a encrypted text using the Caesar cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to decrypt.
        '''
        decrypted_generator = (
            self.language[
                (self.language[character] - self.shift) % len(self.language),
                'lower'
            ]
            if character.islower()
            else self.language[
                (self.language[character] - self.shift) % len(self.language),
                'upper'
            ]
            if character.isupper()
            else character
            for character in text
        )
        # Return the text
        return ''.join(decrypted_generator)

    def encrypt(self, text:str) -> str:
        '''encrypt a encrypted text using the Caesar cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to encrypt.
        '''
        encrypted_generator = (
            self.language[
                (self.language[character] + self.shift) % len(self.language),
                'lower'
            ]
            if character.islower()
            else self.language[
                (self.language[character] + self.shift) % len(self.language),
                'upper'
            ]
            if character.isupper()
            else character
            for character in text
        )
        # Return the text
        return ''.join(encrypted_generator)