from ciphers.cipher.base_cipher import BaseCipher
from ciphers.commons.alphabet import Alphabet
from ciphers.commons.constants import languages


class AtbashCipher(BaseCipher):
    '''Class that defines the Atbash Cipher for a language. Uses english by
    default but accepts custom languages.
    
    Attributes
    ----------
    language: Alphabet
        The letters of an alphabet the Cipher will work upon.
    '''
    __slots__ = ['language']

    def __init__(self, language: Alphabet=None) -> None:
        '''Create a Atbash Cipher class.
        '''
        # Add language
        if language:
            self.language = language
        else:
            self.language = languages['en']

    def decrypt(self, text:str) -> str:
        '''Decrypt a encrypted text using the Atbash cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to decrypt.
        '''
        decrypted = [] # Empty list with the decrypted letters
        vocabulary_length = len(self.language)
        # iterate over the text
        for character in text:
            # Encrypt the character
            if character.islower():
                new_char = self.language[
                    ((-1 * self.language[character]) - 1) % vocabulary_length,
                    'lower'
                ]
                decrypted.append(new_char)
            elif character.isupper():
                new_char = self.language[
                    ((-1 * self.language[character]) - 1) % vocabulary_length,
                    'upper'
                ]
                decrypted.append(new_char)
            else:
                decrypted.append(character)
        # Return the text
        return ''.join(decrypted)

    def encrypt(self, text:str) -> str:
        '''encrypt a encrypted text using the Atbash cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to encrypt.
        '''
        return self.decrypt(text)