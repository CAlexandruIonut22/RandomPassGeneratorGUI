import bcrypt
from cryptography.fernet import Fernet


def hash_pass(password):
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return password_hashed


def encrypt_pass(key, passwrd):
    fernet = Fernet(key)
    encMessage = fernet.encrypt(passwrd.encode())
    return encMessage


def decrypt_pass(enc_key, enc_passwrd):
    fernet = Fernet(enc_key)
    decMessage = fernet.decrypt(enc_passwrd).decode()
    return decMessage
