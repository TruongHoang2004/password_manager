# main.py
from password_manager import PasswordManager
from encryption import encrypt_password, decrypt_password

def main():
    password_manager = PasswordManager()
    
    while True:
        print("\n=== QUẢN LÝ MẬT KHẨU ===")
        print("1. Thêm mật khẩu mới")
        print("2. Xem tất cả mật khẩu")
        print("3. Tìm kiếm mật khẩu")
        print("4. Cập nhật mật khẩu")
        print("5. Xóa mật khẩu")
        print("6. Thoát")
        
        choice = input("\nNhập lựa chọn của bạn: ")
        
        if choice == "1":
            service = input("Nhập tên dịch vụ: ")
            username = input("Nhập tên người dùng: ")
            password = input("Nhập mật khẩu: ")
            password_manager.add_password(service, username, password)
            
        elif choice == "2":
            password_manager.view_all_passwords()
            
        elif choice == "3":
            service = input("Nhập tên dịch vụ cần tìm: ")
            password_manager.search_password(service)
            
        elif choice == "4":
            service = input("Nhập tên dịch vụ cần cập nhật: ")
            new_password = input("Nhập mật khẩu mới: ")
            password_manager.update_password(service, new_password)
            
        elif choice == "5":
            service = input("Nhập tên dịch vụ cần xóa: ")
            password_manager.delete_password(service)
            
        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại!")

if __name__ == "__main__":
    main()