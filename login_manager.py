# login_manager.py
import json
import os
from encryption import encrypt_password, decrypt_password

class LoginManager:
    def __init__(self):
        self.file_path = "login_info.json"
        self.initialize_login()
    
    def initialize_login(self):
        """Khởi tạo file login nếu chưa tồn tại"""
        if not os.path.exists(self.file_path):
            default_password = encrypt_password("admin")  # Mật khẩu mặc định
            login_info = {"password": default_password}
            with open(self.file_path, "w") as file:
                json.dump(login_info, file)
    
    def verify_password(self, password):
        """Xác thực mật khẩu"""
        try:
            with open(self.file_path, "r") as file:
                login_info = json.load(file)
                stored_password = login_info["password"]
                decrypted_password = decrypt_password(stored_password)
                return password == decrypted_password
        except:
            return False
    
    def change_password(self, new_password):
        """Thay đổi mật khẩu"""
        encrypted_password = encrypt_password(new_password)
        login_info = {"password": encrypted_password}
        with open(self.file_path, "w") as file:
            json.dump(login_info, file)