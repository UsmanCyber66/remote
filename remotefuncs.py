import hashlib
from cryptography.fernet import Fernet
import base64
import getpass
def sha(x):
    return hashlib.sha256(x.encode()).digest()

def baseify(x):
    return base64.urlsafe_b64encode(x)
class attr:
    password = "default"

    @classmethod
    def get_key(cls):
        # This calculates the key "on the fly" using the CURRENT password
        return baseify(sha(cls.password))

def encrypt(data) :
    f = Fernet(attr.get_key())
    return f.encrypt(data.encode())
    