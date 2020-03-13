import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
#Encryption
password_provided = raw_input("Enter Your Password: ") # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes
salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
file = open('key.key', 'a+')
file.write(password_provided+":"+key+'\n') # The key is type bytes still
file.close()
input_file = 'test.txt'
output_file = 'test.encrypted'
with open(input_file, 'rb') as f:
    data = f.read()
fernet = Fernet(key)
encrypted = fernet.encrypt(data)
with open(output_file, 'wb') as f:
    f.write(encrypted)
    
#Decryption
from cryptography.fernet import Fernet
input_file = 'test.encrypted'
output_file = 'tester.txt'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

#Email
