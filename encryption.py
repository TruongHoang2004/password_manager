# encryption.py
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

def get_key():
    # Tạo key file nếu chưa tồn tại
    if not os.path.exists('key.key'):
        # Tạo salt ngẫu nhiên
        salt = os.urandom(16)
        # Sử dụng PBKDF2 để tạo key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(b"your-secret-password"))
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
    else:
        # Đọc key từ file
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
    
    return key

def encrypt_password(password):
    # Lấy key để mã hóa
    key = get_key()
    f = Fernet(key)
    # Mã hóa mật khẩu
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password.decode()

def decrypt_password(encrypted_password):
    # Lấy key để giải mã
    key = get_key()
    f = Fernet(key)
    # Giải mã mật khẩu
    decrypted_password = f.decrypt(encrypted_password.encode())
    return decrypted_password.decode()