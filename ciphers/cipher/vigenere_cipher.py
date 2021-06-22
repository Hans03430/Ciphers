from ciphers.cipher.base_cipher import BaseCipher
from ciphers.cipher.caesar_cipher import CaesarCipher
from ciphers.commons.alphabet import Alphabet
from ciphers.commons.constants import languages


class VigenereCipher(BaseCipher):
    '''Class that defines the Vigenere Cipher for a language. Uses english by
    default but accepts custom languages.
    
    Attributes
    ----------
    language: Alphabet
        The letters of an alphabet the Cipher will work upon.

    key: str
        Keyword to encrypt/decrypt the text.

    shifts: CaesarCipher
        The Caesar cipher that simulate the tabula recta.

    key_ord: List[int]
        Numeric order for each letter of the key.
    '''
    __slots__ = ['__language', '__key', 'shifts', 'key_ord']

    def __init__(self, key='LEMON', language: Alphabet=None) -> None:
        '''Create a Vigenere Cipher class.
        '''
        if len(key) == 0:
            raise AttributeError('The key can\'t be empty.')
        # Add language
        if language:
            self.language = language
        else:
            self.language = languages['en']

        self.key = key

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str) -> None:
        self.__key = key
        self.key_ord = [
            self.language.order_lower[c]
            if c.islower()
            else self.language.order_upper[c]
            for c in self.key
        ]

    @property
    def language(self) -> Alphabet:
        return self.__language

    @language.setter
    def language(self, language: Alphabet) -> None:
        self.__language = language
        # Create the a caesar cipher
        self.shifts = CaesarCipher(language=self.language)
        

    def decrypt(self, text:str) -> str:
        '''Decrypt a encrypted text using the Vigenere cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to decrypt.
        '''
        decrypted = [] # Empty list to hold the decrypted letters
        key_length = len(self.key)
        # Iterate all the text
        for i, character in enumerate(text):
            if character.isalpha():
                self.shifts.shift = self.key_ord[i % key_length]
                decrypted.append(
                    self.shifts.decrypt(character)
                )
            else:
                decrypted.append(character)

        return ''.join(decrypted)

    def encrypt(self, text:str) -> str:
        '''encrypt a encrypted text using the Vigenere cipher, using the shift
        given to the class.
        
        Parameters
        ----------
        text: str
            The text to encrypt.
        '''
        encrypted = [] # Empty list to hold the encrypted letters
        key_length = len(self.key)
        # Iterate all the text
        for i, character in enumerate(text):
            if character.isalpha():
                self.shifts.shift = self.key_ord[i % key_length]
                encrypted.append(
                    self.shifts.encrypt(character)
                )
            else:
                encrypted.append(character)

        return ''.join(encrypted)