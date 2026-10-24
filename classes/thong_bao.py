"""
classes/thong_bao.py
Phụ trách: TV1 - Lưu Trọng Ngân (nhóm trưởng)
ThongBao: hệ thống tự sinh mỗi khi hồ sơ đổi trạng thái, gửi cho ứng viên.
"""

from datetime import datetime

from classes.hang_so import KENH_HOP_LE, LoiNghiepVu


class ThongBao:
    """Hồ sơ liên quan, kênh gửi (app, email, sms), nội dung, trạng thái gửi."""

    def __init__(self, ho_so_ung_vien, kenh, noi_dung):
        if kenh not in KENH_HOP_LE:
            raise LoiNghiepVu(f"Kênh thông báo không hợp lệ: {kenh}")
        self.ho_so_ung_vien = ho_so_ung_vien
        self.kenh = kenh  # "app" | "email" | "sms"
        self.noi_dung = noi_dung
        self.trang_thai_gui = "chờ gửi"
        self.thoi_gian_gui = None

    def gui(self):
        """Đẩy nội dung tới đúng kênh. Hiện chỉ giả lập bằng cách ghi vào hộp thư của ứng viên;
        sau này thay phần này bằng smtplib (email) hoặc API SMS thật."""
        uv = self.ho_so_ung_vien.ung_vien
        dich = {"email": uv.email, "sms": uv.sdt, "app": uv.ho_ten}[self.kenh]
        uv.hop_thu.append(f"[{self.kenh.upper()} -> {dich}] {self.noi_dung}")
        self.trang_thai_gui = "đã gửi"
        self.thoi_gian_gui = datetime.now()
