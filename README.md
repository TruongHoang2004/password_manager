# Password Manager

Ứng dụng quản lý mật khẩu được xây dựng bằng Python với giao diện đồ họa, có khả năng mã hóa và bảo vệ dữ liệu.

## Tính năng

- 🔐 Mã hóa mật khẩu sử dụng thuật toán Fernet
- 🔒 Bảo vệ ứng dụng bằng mật khẩu đăng nhập
- ➕ Thêm, xóa, sửa thông tin mật khẩu
- 🔍 Tìm kiếm và xem danh sách mật khẩu
- 💾 Lưu trữ dữ liệu dưới dạng file JSON được mã hóa
- 🔄 Đổi mật khẩu đăng nhập
- 📱 Giao diện người dùng thân thiện

## Cài đặt

### Yêu cầu

- Python 3.6 trở lên
- pip (Python package manager)

### Các bước cài đặt

1. Clone repository:
```bash
git clone https://github.com/your-username/password-manager.git
cd password-manager
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

### Sử dụng trực tiếp từ source code

Chạy file gui.py:
```bash
python gui.py
```

### Sử dụng file .exe (Windows)

1. Tải file .exe từ phần Releases
2. Giải nén và chạy file "Password Manager.exe"

## Cách sử dụng

1. Đăng nhập:
   - Mật khẩu mặc định: "admin"
   - Có thể thay đổi mật khẩu sau khi đăng nhập

2. Thêm mật khẩu mới:
   - Chọn tab "Thêm Mật Khẩu"
   - Điền thông tin dịch vụ, tên người dùng và mật khẩu
   - Nhấn "Thêm mật khẩu"

3. Xem và quản lý mật khẩu:
   - Chọn tab "Xem Mật Khẩu"
   - Danh sách mật khẩu được hiển thị trong bảng
   - Có thể cập nhật hoặc xóa mật khẩu đã chọn

4. Đổi mật khẩu đăng nhập:
   - Chọn "Cài đặt" > "Đổi mật khẩu đăng nhập"
   - Nhập mật khẩu hiện tại và mật khẩu mới

## Cấu trúc dự án

```
password-manager/
├── gui.py              # Giao diện người dùng
├── password_manager.py # Quản lý mật khẩu
├── login_manager.py    # Xác thực đăng nhập
├── encryption.py       # Mã hóa/giải mã
├── requirements.txt    # Thư viện cần thiết
└── README.md          # Tài liệu hướng dẫn
```

## Bảo mật

- Mật khẩu được mã hóa sử dụng thuật toán Fernet
- Key được tạo ngẫu nhiên và lưu trữ riêng
- Mật khẩu đăng nhập được mã hóa
- Dữ liệu được lưu dưới dạng mã hóa

## Góp ý và báo lỗi

Nếu bạn phát hiện lỗi hoặc có ý tưởng cải thiện, vui lòng:
1. Tạo issue mới
2. Hoặc gửi pull request

## License

MIT License - Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## Tác giả

- Your Name
- GitHub: [@your-username](https://github.com/your-username)
