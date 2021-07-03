import unittest

from ciphers.cipher.affine_cipher import AffineCipher

class AffineCipher(unittest.TestCase):
    cipher = AffineCipher()
    plain_text = 'Hello World'
    encrypted_text = 'Ifmmp Xpsme'

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