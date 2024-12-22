# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from password_manager import PasswordManager
from login_manager import LoginManager

class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Đăng Nhập")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        self.login_manager = LoginManager()
        
        # Center window
        self.center_window()
        
        # Login frame
        login_frame = ttk.Frame(self.root, padding="20")
        login_frame.pack(fill="both", expand=True)
        
        # Password entry
        ttk.Label(login_frame, text="Nhập mật khẩu:").pack(pady=(20,5))
        self.password_entry = ttk.Entry(login_frame, show="*")
        self.password_entry.pack(pady=5)
        
        # Login button
        ttk.Button(login_frame, text="Đăng nhập", command=self.login).pack(pady=20)
        
        # Bind Enter key
        self.password_entry.bind('<Return>', lambda e: self.login())
        
        # Focus password entry
        self.password_entry.focus()

    def center_window(self):
        """Đặt cửa sổ ở giữa màn hình"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 300) // 2
        y = (screen_height - 200) // 2
        self.root.geometry(f"300x200+{x}+{y}")
        
    def login(self):
        password = self.password_entry.get()
        if self.login_manager.verify_password(password):
            self.root.destroy()
            app = PasswordManagerApp()
            app.run()
        else:
            messagebox.showerror("Lỗi", "Mật khẩu không đúng!")
            self.password_entry.delete(0, tk.END)

class PasswordManagerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quản Lý Mật Khẩu")
        self.root.geometry("600x400")
        
        self.password_manager = PasswordManager()
        self.login_manager = LoginManager()
        
        # Menu bar
        self.create_menu()
        
        # Notebook để chứa các tab
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)
        
        # Tab thêm mật khẩu
        self.add_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.add_frame, text="Thêm Mật Khẩu")
        self.setup_add_tab()
        
        # Tab xem mật khẩu
        self.view_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.view_frame, text="Xem Mật Khẩu")
        self.setup_view_tab()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menu Cài đặt
        settings_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Cài đặt", menu=settings_menu)
        settings_menu.add_command(label="Đổi mật khẩu đăng nhập", command=self.show_change_password_dialog)
        settings_menu.add_separator()
        settings_menu.add_command(label="Thoát", command=self.root.quit)

    def show_change_password_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Đổi Mật Khẩu Đăng Nhập")
        dialog.geometry("300x250")  # Tăng chiều cao để chứa nút
        dialog.transient(self.root)
        dialog.resizable(False, False)  # Không cho phép thay đổi kích thước
        
        # Center dialog
        dialog.geometry("+%d+%d" % (self.root.winfo_x() + 150, 
                                self.root.winfo_y() + 100))
        
        frame = ttk.Frame(dialog, padding="20")
        frame.pack(fill="both", expand=True)
        
        # Current password
        ttk.Label(frame, text="Mật khẩu hiện tại:").pack(pady=(0,5))
        current_pwd = ttk.Entry(frame, show="*")
        current_pwd.pack(pady=(0,10))
        current_pwd.focus()  # Focus vào ô mật khẩu hiện tại
        
        # New password
        ttk.Label(frame, text="Mật khẩu mới:").pack(pady=(0,5))
        new_pwd = ttk.Entry(frame, show="*")
        new_pwd.pack(pady=(0,20))
        
        # Button frame
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=(0,10))
        
        def change_password():
            if self.login_manager.verify_password(current_pwd.get()):
                if new_pwd.get():
                    self.login_manager.change_password(new_pwd.get())
                    messagebox.showinfo("Thành công", "Đã đổi mật khẩu đăng nhập!")
                    dialog.destroy()
                else:
                    messagebox.showerror("Lỗi", "Vui lòng nhập mật khẩu mới!")
            else:
                messagebox.showerror("Lỗi", "Mật khẩu hiện tại không đúng!")
        
        def cancel():
            dialog.destroy()
        
        # Thêm hai nút Submit và Cancel
        ttk.Button(btn_frame, text="Đổi mật khẩu", command=change_password, width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Hủy", command=cancel, width=15).pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key cho cả hai entry
        current_pwd.bind('<Return>', lambda e: new_pwd.focus())
        new_pwd.bind('<Return>', lambda e: change_password())
        
        # Bind Escape key để đóng dialog
        dialog.bind('<Escape>', lambda e: dialog.destroy())
        
        # Đảm bảo dialog luôn ở trên cùng
        dialog.grab_set()
        dialog.focus_force()

    # [Các phương thức khác giữ nguyên như cũ]
    def setup_add_tab(self):
        # Frame cho form nhập liệu
        form_frame = ttk.LabelFrame(self.add_frame, text="Thông tin mật khẩu")
        form_frame.pack(padx=20, pady=20, fill="x")
        
        # Service
        ttk.Label(form_frame, text="Tên dịch vụ:").grid(row=0, column=0, padx=5, pady=5)
        self.service_entry = ttk.Entry(form_frame, width=40)
        self.service_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Username
        ttk.Label(form_frame, text="Tên người dùng:").grid(row=1, column=0, padx=5, pady=5)
        self.username_entry = ttk.Entry(form_frame, width=40)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Password
        ttk.Label(form_frame, text="Mật khẩu:").grid(row=2, column=0, padx=5, pady=5)
        self.password_entry = ttk.Entry(form_frame, width=40, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Nút thêm
        ttk.Button(form_frame, text="Thêm mật khẩu", command=self.add_password).grid(row=3, column=0, columnspan=2, pady=20)

    def setup_view_tab(self):
        # Frame cho danh sách mật khẩu
        list_frame = ttk.Frame(self.view_frame)
        list_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Tạo Treeview
        self.tree = ttk.Treeview(list_frame, columns=("Service", "Username", "Password"), show="headings")
        self.tree.heading("Service", text="Dịch vụ")
        self.tree.heading("Username", text="Tên người dùng")
        self.tree.heading("Password", text="Mật khẩu")
        
        # Thêm scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack các widget
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons frame
        btn_frame = ttk.Frame(self.view_frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Làm mới", command=self.refresh_passwords).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Xóa", command=self.delete_password).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Cập nhật", command=self.show_update_dialog).pack(side="left", padx=5)
        
        # Load dữ liệu ban đầu
        self.refresh_passwords()

    def add_password(self):
        service = self.service_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if service and username and password:
            self.password_manager.add_password(service, username, password)
            messagebox.showinfo("Thành công", "Đã thêm mật khẩu mới!")
            
            # Clear entries
            self.service_entry.delete(0, tk.END)
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            
            # Refresh view tab
            self.refresh_passwords()
        else:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")

    def refresh_passwords(self):
        # Xóa dữ liệu cũ
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Load dữ liệu mới
        for service, data in self.password_manager.passwords.items():
            decrypted_password = self.password_manager.decrypt_password(data["password"])
            self.tree.insert("", "end", values=(service, data["username"], decrypted_password))

    def delete_password(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một mục để xóa!")
            return
            
        service = self.tree.item(selected_item[0])["values"][0]
        if messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa mật khẩu cho {service}?"):
            self.password_manager.delete_password(service)
            self.refresh_passwords()

    def show_update_dialog(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một mục để cập nhật!")
            return
            
        service = self.tree.item(selected_item[0])["values"][0]
        
        # Tạo dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Cập nhật mật khẩu")
        dialog.geometry("300x150")
        
        ttk.Label(dialog, text="Mật khẩu mới:").pack(pady=10)
        new_password_entry = ttk.Entry(dialog, show="*")
        new_password_entry.pack(pady=5)
        
        def update():
            new_password = new_password_entry.get()
            if new_password:
                self.password_manager.update_password(service, new_password)
                self.refresh_passwords()
                dialog.destroy()
                messagebox.showinfo("Thành công", "Đã cập nhật mật khẩu!")
            else:
                messagebox.showerror("Lỗi", "Vui lòng nhập mật khẩu mới!")
        
        ttk.Button(dialog, text="Cập nhật", command=update).pack(pady=20)

    def run(self):
        self.root.mainloop()

def main():
    login = LoginWindow()
    login.root.mainloop()

if __name__ == "__main__":
    main()