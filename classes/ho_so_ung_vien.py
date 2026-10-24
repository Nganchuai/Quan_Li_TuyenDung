"""
classes/ho_so_ung_vien.py
Phụ trách: TV1 - Lưu Trọng Ngân (nhóm trưởng)
HoSoUngVien: sinh ra khi UngVien nộp hồ sơ - trung tâm của luồng duyệt/phỏng vấn.
Trạng thái nằm ở đây (không nằm ở UngVien) vì 1 ứng viên có thể nộp nhiều tin.
"""

import itertools
from datetime import date

from classes.hang_so import HS_MOI_NOP, lay_id
from classes.thong_bao import ThongBao


class HoSoUngVien:
    """Ứng viên, tin ứng tuyển, trạng thái, lý do từ chối."""

    _dem = itertools.count(1)

    def __init__(self, id, ung_vien, tin_tuyen_dung, cv_note="", cv_file=None):
        self.id = lay_id(self._dem, id)
        self.ung_vien = ung_vien
        self.tin_tuyen_dung = tin_tuyen_dung
        self.cv_note = cv_note
        self.cv_file = cv_file
        self.ngay_nop = date.today()
        self.trang_thai = HS_MOI_NOP
        self.ly_do_tu_choi = None
        self.phong_van = None
        self.giam_doc_xac_nhan = None  # ngày giám đốc xác nhận kết quả cuối (nếu có)

    def gui_thong_bao(self, noi_dung):
        """Sinh và gửi ThongBao qua mọi kênh ứng viên đã chọn khi nộp hồ sơ."""
        for kenh in self.ung_vien.kenh_nhan_tin:
            ThongBao(self, kenh, noi_dung).gui()

    def doi_trang_thai(self, trang_thai, noi_dung=None):
        """Đổi trạng thái và tự gửi thông báo cho ứng viên."""
        self.trang_thai = trang_thai
        vi_tri = self.tin_tuyen_dung.yeu_cau.vi_tri
        self.gui_thong_bao(
            noi_dung or f"Hồ sơ '{vi_tri}' của bạn chuyển sang trạng thái: {trang_thai}."
        )
