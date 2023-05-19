import hashlib

def hash(password) -> str:
    return hashlib.md5(password.encode()).hexdigest()