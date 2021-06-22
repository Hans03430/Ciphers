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
    language: Alphabet
        The letters of an alphabet the Cipher will work upon.
    '''
    __slots__ = ['shift', 'language']

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

    def decrypt(self, text:str) -> str:
        '''Decrypt a encrypted text using the Caesar cipher, using the shift
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
                    (self.language[character] - self.shift) % vocabulary_length,
                    'lower'
                ]
                decrypted.append(new_char)
            elif character.isupper():
                new_char = self.language[
                    (self.language[character] - self.shift) % vocabulary_length,
                    'upper'
                ]
                decrypted.append(new_char)
            else:
                decrypted.append(character)
        # Return the text
        return ''.join(decrypted)

    def encrypt(self, text:str) -> str:
        '''encrypt a encrypted text using the Caesar cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to encrypt.
        '''
        encrypted = [] # Empty list with the encrypted letters
        vocabulary_length = len(self.language)
        # iterate over the text
        for character in text:
            # Encrypt the character
            if character.islower():
                new_char = self.language[
                    (self.language[character] + self.shift) % vocabulary_length,
                    'lower'
                ]
                encrypted.append(new_char)
            elif character.isupper():
                new_char = self.language[
                    (self.language[character] + self.shift) % vocabulary_length,
                    'upper'
                ]
                encrypted.append(new_char)
            else:
                encrypted.append(character)
        # Return the text
        return ''.join(encrypted)