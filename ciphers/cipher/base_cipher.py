from abc import ABC
from abc import abstractmethod
from ciphers.commons.alphabet import Alphabet


class BaseCipher(ABC):
    '''Base Cipher the others must implement.
    
    Attributes
    ----------
    _language: Alphabet
        The alphabet the cipher uses to encrypt/decrypt.
    '''

    __slots__ = ['_language']
    
    @abstractmethod
    def decrypt(self, text=str) -> str:
        return NotImplementedError

    @abstractmethod
    def encrypt(self, text=str) -> str:
        return NotImplementedError
