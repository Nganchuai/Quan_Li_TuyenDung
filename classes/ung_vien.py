"""
classes/ung_vien.py
Phụ trách: TV3
UngVien: xem tin và nộp hồ sơ. KHÔNG kế thừa NguoiDung vì không đăng nhập,
chỉ định danh bằng email/số điện thoại.
"""

from classes.hang_so import HS_MOI_NOP, KENH_HOP_LE, LoiNghiepVu, LoiQuyenHan
from classes.ho_so_ung_vien import HoSoUngVien


class UngVien:
    """Họ tên, email, SĐT; nộp hồ sơ, tra cứu trạng thái (không có tài khoản)."""

    def __init__(self, ho_ten, email, sdt, kenh_nhan_tin=("email",)):
        self.ho_ten = ho_ten
        self.email = email
        self.sdt = sdt
        self.kenh_nhan_tin = tuple(kenh_nhan_tin)  # kênh nhận thông báo, chọn lúc nộp hồ sơ
        self.cac_ho_so = []
        self.hop_thu = []  # nơi ThongBao.gui() ghi vào (giả lập)

    def nop_ho_so(self, tin_tuyen_dung, cv_note, cv_file=None):
        """Nhiệm vụ 1: nộp hồ sơ cho 1 tin cụ thể - tạo ra HoSoUngVien."""
        for kenh in self.kenh_nhan_tin:
            if kenh not in KENH_HOP_LE:
                raise LoiNghiepVu(f"Kênh thông báo không hợp lệ: {kenh}")
        ho_so = HoSoUngVien(None, self, tin_tuyen_dung, cv_note, cv_file)
        tin_tuyen_dung.nhan_ho_so(ho_so)  # ném LoiNghiepVu nếu trùng/đóng/hết hạn
        self.cac_ho_so.append(ho_so)
        ho_so.doi_trang_thai(
            HS_MOI_NOP, f"Đã nhận hồ sơ ứng tuyển '{tin_tuyen_dung.yeu_cau.vi_tri}' của bạn."
        )
        return ho_so

    def tra_cuu_trang_thai(self, email_hoac_sdt):
        """Nhiệm vụ 2: tự kiểm tra tiến độ hồ sơ, xác thực bằng email hoặc số điện thoại."""
        if email_hoac_sdt not in (self.email, self.sdt):
            raise LoiQuyenHan("Email/số điện thoại không khớp với hồ sơ.")
        return [
            {"vi_tri": hs.tin_tuyen_dung.yeu_cau.vi_tri, "trang_thai": hs.trang_thai}
            for hs in self.cac_ho_so
        ]
