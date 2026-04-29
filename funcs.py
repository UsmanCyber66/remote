import hashlib
from cryptography.fernet import Fernet
import base64
import getpass # <--- Add this

def sha(x):
    return hashlib.sha256(x.encode()).digest()

def baseify(x):
    return base64.urlsafe_b64encode(x)

def encrypt(password, data ):
    key = 
    f= Fernet(key)
    return f.encrypt(data.encode())
