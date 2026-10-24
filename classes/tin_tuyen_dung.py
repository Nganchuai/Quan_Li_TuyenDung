"""
classes/tin_tuyen_dung.py
Phụ trách: TV3
TinTuyenDung: do NhanVienTuyenDung tạo từ 1 YeuCauTuyenDung - nội dung ứng viên nhìn thấy.
"""

import itertools
from datetime import date

from classes.hang_so import YC_DA_DU, LoiNghiepVu, lay_id


class TinTuyenDung:
    """Yêu cầu liên quan, mô tả, quyền lợi, file đính kèm, công khai hay nội bộ."""

    _dem = itertools.count(1)

    def __init__(self, id, yeu_cau, mo_ta, quyen_loi, file_dinh_kem=None, cong_khai=True):
        self.id = lay_id(self._dem, id)
        self.yeu_cau = yeu_cau
        self.mo_ta = mo_ta
        self.quyen_loi = quyen_loi
        self.file_dinh_kem = file_dinh_kem
        self.cong_khai = cong_khai
        self.ngay_dang = date.today()
        self.cac_ho_so = []

    def dong_tin(self):
        self.cong_khai = False

    def nhan_ho_so(self, ho_so):
        """Kiểm tra điều kiện nhận hồ sơ (cũng là chốt chặn chống nộp trùng/spam)."""
        if not self.cong_khai:
            raise LoiNghiepVu("Tin tuyển dụng này đã đóng.")
        if self.yeu_cau.trang_thai == YC_DA_DU:
            raise LoiNghiepVu("Vị trí đã tuyển đủ người.")
        han = self.yeu_cau.han_tuyen
        if isinstance(han, date) and date.today() > han:
            raise LoiNghiepVu("Đã hết hạn nộp hồ sơ.")
        uv = ho_so.ung_vien
        for hs in self.cac_ho_so:
            if hs.ung_vien.email == uv.email or hs.ung_vien.sdt == uv.sdt:
                raise LoiNghiepVu("Email hoặc số điện thoại này đã nộp hồ sơ cho tin này.")
        self.cac_ho_so.append(ho_so)
