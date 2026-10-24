"""
classes/yeu_cau_tuyen_dung.py
Phụ trách: TV2
YeuCauTuyenDung (do GiamDoc tạo) và Slot (chỉ tiêu tuyển dụng, tự sinh theo số lượng).
"""

import itertools

from classes.hang_so import YC_CHO_DANG, YC_DA_DU, LoiNghiepVu, lay_id


class Slot:
    """1 chỉ tiêu tuyển dụng. Yêu cầu tuyển 3 người -> hệ thống sinh 3 Slot."""

    def __init__(self, so_thu_tu):
        self.so_thu_tu = so_thu_tu
        self.trang_thai = "Trống"  # "Trống" | "Đã tuyển"
        self.ho_so = None          # HoSoUngVien trúng tuyển vào slot này

    def gan(self, ho_so):
        if self.trang_thai != "Trống":
            raise LoiNghiepVu("Slot này đã có người.")
        self.trang_thai = "Đã tuyển"
        self.ho_so = ho_so


class YeuCauTuyenDung:
    """Vị trí, số lượng, mô tả, hạn tuyển, người phụ trách, trạng thái."""

    _dem = itertools.count(1)

    def __init__(self, id, vi_tri, so_luong, mo_ta, han_tuyen, nguoi_phu_trach=None):
        self.id = lay_id(self._dem, id)
        self.vi_tri = vi_tri
        self.so_luong = so_luong
        self.mo_ta = mo_ta
        self.han_tuyen = han_tuyen               # kiểu date hoặc None
        self.nguoi_phu_trach = nguoi_phu_trach   # tham chiếu NhanVienTuyenDung
        self.trang_thai = YC_CHO_DANG
        self.slots = [Slot(i) for i in range(1, so_luong + 1)]  # tự sinh slot
        self.cac_tin = []                        # các TinTuyenDung đã đăng

    def slot_trong_dau_tien(self):
        return next((s for s in self.slots if s.trang_thai == "Trống"), None)

    def so_da_tuyen(self):
        return sum(1 for s in self.slots if s.trang_thai == "Đã tuyển")

    def cap_nhat_trang_thai(self):
        """Hết slot trống thì chuyển sang Đã tuyển đủ."""
        if self.slot_trong_dau_tien() is None:
            self.trang_thai = YC_DA_DU

    def tat_ca_ho_so(self):
        return [hs for tin in self.cac_tin for hs in tin.cac_ho_so]
