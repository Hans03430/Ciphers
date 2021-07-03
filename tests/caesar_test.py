import unittest

from ciphers.cipher.caesar_cipher import CaesarCipher

class CaesarTest(unittest.TestCase):
    cipher = CaesarCipher()
    plain_text = 'Hello World'
    encrypted_text = 'Khoor Zruog'

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