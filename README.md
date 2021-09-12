# fake-ransomware
Utility represent a ransomware for educational purposes to my engineer students

## Installation

```bash
# traditional
pip install -r requirements.txt

# or if you have pipenv installed
pipenv install
```

## Usage example

```python
import time
from crypter.ransomware import FakeRansomware

ransomware = FakeRansomware()

# Generate a new key, backup the key to restore files
ransomware.generate_key()

# Show Key file location
print(ransomware.keyfile_path)

# In action
print(f'Encrypting files in {ransomware.target_dir}')
ransomware.encrypt_files()

print('Waiting')
time.sleep(5)

print(f'Decrypting files in {ransomware.target_dir}')
ransomware.decrypt()

# or pass a key as byte string
my_key = b'3xmxI-fQu51kTX9aCHHIfeKHRlbl8iW4UEAkAHo8CSw='
my_ransomware = FakeRansomware(key=my_key)
# ...
```

## Note

Files are encrypted in directory:

```bash
TARGET/
```