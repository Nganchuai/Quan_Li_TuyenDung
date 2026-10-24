"""
classes/nguoi_dung.py
Phụ trách: TV1 - Lưu Trọng Ngân (nhóm trưởng)
Lớp cha chung cho người có tài khoản: GiamDoc, NhanVienTuyenDung.
"""



class NguoiDung:
    """Lớp cha chung cho người có tài khoản trong hệ thống (Giám đốc, Nhân viên)."""

    def __init__(self, id, ho_ten, username, password, vai_tro):
        self.id = id
        self.ho_ten = ho_ten
        self.username = username
        self.password = password
        self.vai_tro = vai_tro  # "giam_doc" hoặc "nhan_vien"

    def dang_nhap(self, username, password):
        """Xác thực, trả về True/False."""
        return username == self.username and password == self.password
