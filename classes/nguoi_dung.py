"""
classes/nguoi_dung.py
Phụ trách: TV1 - Lưu Trọng Ngân (nhóm trưởng)
Lớp cha chung cho người có tài khoản: GiamDoc, NhanVienTuyenDung.
"""

import hashlib
import secrets


class NguoiDung:
    """Lớp cha chung cho người có tài khoản trong hệ thống (Giám đốc, Nhân viên)."""

    def __init__(self, id, ho_ten, username, password, vai_tro):
        self.id = id
        self.ho_ten = ho_ten
        self.username = username
        self.vai_tro = vai_tro  # "giam_doc" hoặc "nhan_vien"
        # Không lưu mật khẩu thô: lưu bản băm + salt riêng
        self._salt = secrets.token_hex(8)
        self._password_hash = self._bam(password, self._salt)

    @staticmethod
    def _bam(password, salt):
        return hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt.encode("utf-8"), 100_000
        ).hex()

    def dang_nhap(self, username, password):
        """Xác thực, trả về True/False."""
        if username != self.username:
            return False
        return secrets.compare_digest(self._bam(password, self._salt), self._password_hash)
