#remotefuncs.py
import hashlib
from cryptography.fernet import Fernet
import base64
import getpass

def sha(x):
    return hashlib.sha256(x.encode()).digest()

def baseify(x):
    return base64.urlsafe_b64encode(x)
class attr:
    password: str| bytes= "default"
    username:  str | bytes = "default"
    messages = {"ls":"os.listdir()", "pwd":"os.getcwd()", "cat":"open(args).read()"}
    @classmethod
    def get_key(cls):
        # This calculates the key "on the fly" using the CURRENT password
        return baseify(sha(cls.password))

def encrypt(data) :
    f = Fernet(attr.get_key())
    return f.encrypt(data.encode())

def byte(file):
    with open(file, "rb") as f:
        return f.read() 
def get(x):
    try:    
        with open(x, "r") as f:
            return f.read()
    except FileNotFoundError as e:
        return "File not found."