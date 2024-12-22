# password_manager.py
import json
from encryption import encrypt_password, decrypt_password as decrypt_pwd

class PasswordManager:
    def __init__(self):
        self.file_path = "passwords.json"
        try:
            with open(self.file_path, "r") as file:
                self.passwords = json.load(file)
        except FileNotFoundError:
            self.passwords = {}
            
    def save_to_file(self):
        with open(self.file_path, "w") as file:
            json.dump(self.passwords, file, indent=4)
            
    def add_password(self, service, username, password):
        encrypted_password = encrypt_password(password)
        self.passwords[service] = {
            "username": username,
            "password": encrypted_password
        }
        self.save_to_file()
        print(f"Đã thêm mật khẩu cho dịch vụ {service}")
        
    def view_all_passwords(self):
        if not self.passwords:
            print("Không có mật khẩu nào được lưu trữ!")
            return
            
        print("\n=== DANH SÁCH MẬT KHẨU ===")
        for service, data in self.passwords.items():
            decrypted_password = self.decrypt_password(data["password"])
            print(f"\nDịch vụ: {service}")
            print(f"Tên người dùng: {data['username']}")
            print(f"Mật khẩu: {decrypted_password}")
            
    def search_password(self, service):
        if service in self.passwords:
            data = self.passwords[service]
            decrypted_password = self.decrypt_password(data["password"])
            print(f"\nDịch vụ: {service}")
            print(f"Tên người dùng: {data['username']}")
            print(f"Mật khẩu: {decrypted_password}")
        else:
            print(f"Không tìm thấy mật khẩu cho dịch vụ {service}")
            
    def update_password(self, service, new_password):
        if service in self.passwords:
            encrypted_password = encrypt_password(new_password)
            self.passwords[service]["password"] = encrypted_password
            self.save_to_file()
            print(f"Đã cập nhật mật khẩu cho dịch vụ {service}")
        else:
            print(f"Không tìm thấy dịch vụ {service}")
            
    def delete_password(self, service):
        if service in self.passwords:
            del self.passwords[service]
            self.save_to_file()
            print(f"Đã xóa mật khẩu cho dịch vụ {service}")
        else:
            print(f"Không tìm thấy dịch vụ {service}")

    def decrypt_password(self, encrypted_password):
        """Giải mã mật khẩu đã được mã hóa"""
        return decrypt_pwd(encrypted_password)