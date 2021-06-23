from ciphers.cipher.base_cipher import BaseCipher
from ciphers.commons.alphabet import Alphabet
from ciphers.commons.constants import languages


class AtbashCipher(BaseCipher):
    '''Class that defines the Atbash Cipher for a language. Uses english by
    default but accepts custom languages.
    '''

    def __init__(self, language: Alphabet=None) -> None:
        '''Create a Atbash Cipher class.
        '''
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
        '''Decrypt a encrypted text using the Atbash cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to decrypt.
        '''
        decrypted_generator = (
            self.language[
                ((-1 * self.language[character]) - 1) % len(self.language),
                'lower'
            ]
            if character.islower()
            else self.language[
                ((-1 * self.language[character]) - 1) % len(self.language),
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
        return self.decrypt(text)