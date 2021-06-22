from abc import ABC
from abc import abstractmethod


class BaseCipher(ABC):
    @abstractmethod
    def decrypt(self, text=str) -> str:
        return NotImplementedError

    @abstractmethod
    def encrypt(self, text=str) -> str:
        return NotImplementedError
