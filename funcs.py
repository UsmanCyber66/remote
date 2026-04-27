import hashlib

def sha(x):
    return hashlib.sha256(x.encode()).hexdigest()