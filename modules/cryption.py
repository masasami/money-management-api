from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

import os
from dotenv import load_dotenv
load_dotenv()

CRYPTO_PASSWORD = os.getenv('CRYPTO_PASSWORD')


class Cryption:
    # 暗号化
    def encrypt(decrypted_data: str):
        sha = SHA256.new()
        sha.update(CRYPTO_PASSWORD.encode())
        key = sha.digest()

        iv = Random.new().read(AES.block_size)

        aes = AES.new(key, AES.MODE_CFB, iv)
        return iv + aes.encrypt(decrypted_data.encode('utf-8'))

    # 複合化
    def decrypt(encrypted_data: bytes):
        sha = SHA256.new()
        sha.update(CRYPTO_PASSWORD.encode())
        key = sha.digest()

        iv = encrypted_data[:AES.block_size]
        cipher = encrypted_data[AES.block_size:]

        aes = AES.new(key, AES.MODE_CFB, iv)
        return aes.decrypt(cipher)
