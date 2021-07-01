from ciphers.cipher.base_cipher import BaseCipher
from ciphers.commons.alphabet import Alphabet
from ciphers.commons.constants import LANGUAGES


class CaesarCipher(BaseCipher):
    '''Class that defines the Caesar Cipher for an alphabet. Uses english by
    default but accepts custom alphabets.
    
    Attributes
    ----------
    shift: int
        The amount of letters to shift for the encryption/decryption.
    '''
    __slots__ = ['shift']

    def __init__(self, shift: int=3, alphabet: Alphabet=None) -> None:
        '''Create a Caesar Cipher class.
        '''
        if shift < 0:
            raise AttributeError(
                'The amount of times to shift a letter can\'t be negative.'
            )
            
        self.shift = shift
        # Add alphabet
        if alphabet:
            self.alphabet = alphabet
        else:
            self.alphabet = LANGUAGES['en']

    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet

    @alphabet.setter
    def alphabet(self, alphabet: Alphabet) -> None:
        self._alphabet = alphabet

    def decrypt(self, text:str) -> str:
        '''Decrypt a encrypted text using the Caesar cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to decrypt.
        '''
        decrypted_generator = (
            self.alphabet[
                (self.alphabet[character] - self.shift) % len(self.alphabet),
                'lower'
            ]
            if self.alphabet.is_lower(character)
            else self.alphabet[
                (self.alphabet[character] - self.shift) % len(self.alphabet),
                'upper'
            ]
            if self.alphabet.is_upper(character)
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
            self.alphabet[
                (self.alphabet[character] + self.shift) % len(self.alphabet),
                'lower'
            ]
            if self.alphabet.is_lower(character)
            else self.alphabet[
                (self.alphabet[character] + self.shift) % len(self.alphabet),
                'upper'
            ]
            if self.alphabet.is_upper(character)
            else character
            for character in text
        )
        # Return the text
        return ''.join(encrypted_generator)