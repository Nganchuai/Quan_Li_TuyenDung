"""
classes/nhan_vien_tuyen_dung.py
Phụ trách: TV2
NhanVienTuyenDung: đăng tin, duyệt hồ sơ, xếp lịch phỏng vấn, nhập kết quả phỏng vấn.
Kèm lớp PhongVan (lịch phỏng vấn do nhân viên tạo).
"""

import itertools

from classes.hang_so import (
    HS_MOI_NOP, HS_DA_DUYET, HS_CHO_PV, HS_TRUNG_TUYEN, HS_TU_CHOI,
    YC_DANG_TUYEN, YC_DA_DU, PV_DA_LEN_LICH, PV_DAT, PV_KHONG_DAT,
    LoiNghiepVu, LoiQuyenHan, lay_id,
)
from classes.nguoi_dung import NguoiDung
from classes.tin_tuyen_dung import TinTuyenDung


class PhongVan:
    """Lịch phỏng vấn của 1 hồ sơ."""

    _dem = itertools.count(1)

    def __init__(self, id, ho_so, thoi_gian, dia_diem):
        self.id = lay_id(self._dem, id)
        self.ho_so = ho_so
        self.thoi_gian = thoi_gian
        self.dia_diem = dia_diem
        self.ket_qua = PV_DA_LEN_LICH
        self.ghi_chu = ""


class NhanVienTuyenDung(NguoiDung):
    """
    Người thực thi: nhận yêu cầu được giao, đăng tin, sàng lọc, phỏng vấn, tự phê duyệt.
    KHÔNG có quyền tạo yêu cầu hay gán việc; chỉ làm việc trên yêu cầu được giao cho mình.
    """

    def __init__(self, id, ho_ten, username, password, chuyen_mon=None):
        super().__init__(id, ho_ten, username, password, vai_tro="nhan_vien")
        self.chuyen_mon = chuyen_mon
        self.cac_yeu_cau_duoc_giao = []

    def _kiem_tra_duoc_giao(self, yeu_cau):
        if yeu_cau.nguoi_phu_trach is not self:
            raise LoiQuyenHan("Yêu cầu này không được giao cho bạn.")

    def dang_tin_tuyen_dung(self, yeu_cau, mo_ta, quyen_loi, file_dinh_kem=None):
        """Nhiệm vụ 1: từ yêu cầu được giao, tạo TinTuyenDung công khai."""
        self._kiem_tra_duoc_giao(yeu_cau)
        if yeu_cau.trang_thai == YC_DA_DU:
            raise LoiNghiepVu("Yêu cầu đã tuyển đủ, không đăng thêm tin.")
        tin = TinTuyenDung(None, yeu_cau, mo_ta, quyen_loi, file_dinh_kem)
        yeu_cau.cac_tin.append(tin)
        yeu_cau.trang_thai = YC_DANG_TUYEN
        return tin

    def duyet_ho_so(self, ho_so_ung_vien, ket_qua, ly_do_tu_choi=None):
        """Nhiệm vụ 2: ket_qua = "phu_hop" (mời phỏng vấn) hoặc "tu_choi"."""
        self._kiem_tra_duoc_giao(ho_so_ung_vien.tin_tuyen_dung.yeu_cau)
        if ho_so_ung_vien.trang_thai != HS_MOI_NOP:
            raise LoiNghiepVu("Chỉ duyệt được hồ sơ ở trạng thái 'Mới nộp'.")
        if ket_qua == "phu_hop":
            ho_so_ung_vien.doi_trang_thai(HS_DA_DUYET)
        elif ket_qua == "tu_choi":
            ho_so_ung_vien.ly_do_tu_choi = ly_do_tu_choi
            ho_so_ung_vien.doi_trang_thai(HS_TU_CHOI)
        else:
            raise LoiNghiepVu("ket_qua phải là 'phu_hop' hoặc 'tu_choi'.")

    def xep_lich_phong_van(self, ho_so_ung_vien, thoi_gian, dia_diem):
        """Nhiệm vụ 3: tạo lịch PhongVan cho hồ sơ đã được duyệt."""
        self._kiem_tra_duoc_giao(ho_so_ung_vien.tin_tuyen_dung.yeu_cau)
        if ho_so_ung_vien.trang_thai != HS_DA_DUYET:
            raise LoiNghiepVu("Chỉ xếp lịch cho hồ sơ đã duyệt.")
        pv = PhongVan(None, ho_so_ung_vien, thoi_gian, dia_diem)
        ho_so_ung_vien.phong_van = pv
        ho_so_ung_vien.doi_trang_thai(
            HS_CHO_PV, f"Bạn được mời phỏng vấn lúc {thoi_gian} tại {dia_diem}."
        )
        return pv

    def nhap_ket_qua_phong_van(self, phong_van, ket_qua, ghi_chu=""):
        """Nhiệm vụ 4: ket_qua = "Đạt" hoặc "Không đạt". Đạt -> gán vào slot trống đầu tiên."""
        ho_so = phong_van.ho_so
        yc = ho_so.tin_tuyen_dung.yeu_cau
        self._kiem_tra_duoc_giao(yc)
        if phong_van.ket_qua != PV_DA_LEN_LICH:
            raise LoiNghiepVu("Buổi phỏng vấn này đã có kết quả.")
        if ket_qua == PV_DAT:
            slot = yc.slot_trong_dau_tien()
            if slot is None:  # kiểm tra trước khi đổi bất cứ thứ gì
                raise LoiNghiepVu("Hết slot trống cho vị trí này.")
            phong_van.ket_qua, phong_van.ghi_chu = PV_DAT, ghi_chu
            slot.gan(ho_so)
            ho_so.doi_trang_thai(HS_TRUNG_TUYEN, f"Chúc mừng! Bạn đã trúng tuyển vị trí '{yc.vi_tri}'.")
            yc.cap_nhat_trang_thai()
        elif ket_qua == PV_KHONG_DAT:
            phong_van.ket_qua, phong_van.ghi_chu = PV_KHONG_DAT, ghi_chu
            ho_so.ly_do_tu_choi = "Không đạt phỏng vấn"
            ho_so.doi_trang_thai(HS_TU_CHOI)
        else:
            raise LoiNghiepVu("ket_qua phải là 'Đạt' hoặc 'Không đạt'.")
