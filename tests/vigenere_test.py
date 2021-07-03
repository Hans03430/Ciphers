import unittest

from ciphers.cipher.vigenere_cipher import VigenereCipher

class VigenereTest(unittest.TestCase):
    cipher = VigenereCipher()
    plain_text = 'Hello World'
    encrypted_text = 'Sixzb Aafyo'

    def test_encrypt(self):
        self.assertEqual(
            self.cipher.encrypt(self.plain_text),
            self.encrypted_text
        )

    def test_decrypt(self):
        self.assertEqual(
            self.cipher.decrypt(self.encrypted_text),
            self.plain_text
        )

if __name__ == '__main__':
    unittest.main()