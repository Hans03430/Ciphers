from ciphers.cipher.base_cipher import BaseCipher
from ciphers.commons.alphabet import Alphabet
from ciphers.commons.constants import LANGUAGES


class AtbashCipher(BaseCipher):
    '''Class that defines the Atbash Cipher for a alphabet. Uses english by
    default but accepts custom alphabets.
    '''

    def __init__(self, alphabet: Alphabet=None) -> None:
        '''Create a Atbash Cipher class.
        '''
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
        '''Decrypt a encrypted text using the Atbash cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to decrypt.
        '''
        decrypted_generator = (
            self.alphabet[
                ((-1 * self.alphabet[character]) - 1) % len(self.alphabet),
                'lower'
            ]
            if self.alphabet.is_lower(character)
            else self.alphabet[
                ((-1 * self.alphabet[character]) - 1) % len(self.alphabet),
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
        return self.decrypt(text)