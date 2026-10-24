"""
classes/giam_doc.py
Phụ trách: TV1 - Lưu Trọng Ngân (nhóm trưởng)
GiamDoc: người ra quyết định - tạo nhu cầu tuyển dụng, phân công, theo dõi toàn cảnh.
"""

from datetime import date

from classes.hang_so import HS_TRUNG_TUYEN, LoiNghiepVu, LoiQuyenHan
from classes.nguoi_dung import NguoiDung
from classes.yeu_cau_tuyen_dung import YeuCauTuyenDung
from classes.nhan_vien_tuyen_dung import NhanVienTuyenDung


class GiamDoc(NguoiDung):
    """
    Tạo yêu cầu tuyển dụng, gán nhân viên phụ trách, xem thống kê, xác nhận kết quả cuối.
    KHÔNG trực tiếp đăng tin hay duyệt hồ sơ (nhân viên tuyển dụng tự phê duyệt).
    """

    def __init__(self, id, ho_ten, username, password, phong_ban_phu_trach=None):
        super().__init__(id, ho_ten, username, password, vai_tro="giam_doc")
        self.phong_ban_phu_trach = phong_ban_phu_trach
        self.cac_yeu_cau_da_tao = []

    def tao_yeu_cau_tuyen_dung(self, vi_tri, so_luong, mo_ta, han_tuyen):
        """Nhiệm vụ 1: khởi tạo YeuCauTuyenDung mới (hệ thống tự sinh đủ Slot)."""
        if so_luong <= 0:
            raise LoiNghiepVu("Số lượng cần tuyển phải lớn hơn 0.")
        yc = YeuCauTuyenDung(None, vi_tri, so_luong, mo_ta, han_tuyen)
        self.cac_yeu_cau_da_tao.append(yc)
        return yc

    def gan_nhan_vien_phu_trach(self, yeu_cau, nhan_vien):
        """Nhiệm vụ 2: chọn NhanVienTuyenDung phù hợp để xử lý yêu cầu."""
        if yeu_cau not in self.cac_yeu_cau_da_tao:
            raise LoiQuyenHan("Bạn chỉ được giao việc cho yêu cầu do chính mình tạo.")
        if not isinstance(nhan_vien, NhanVienTuyenDung):
            raise LoiNghiepVu("Chỉ giao việc cho nhân viên tuyển dụng.")
        cu = yeu_cau.nguoi_phu_trach
        if cu is not None and yeu_cau in cu.cac_yeu_cau_duoc_giao:
            cu.cac_yeu_cau_duoc_giao.remove(yeu_cau)  # đổi người thì gỡ khỏi người cũ
        yeu_cau.nguoi_phu_trach = nhan_vien
        nhan_vien.cac_yeu_cau_duoc_giao.append(yeu_cau)

    def xem_bao_cao_thong_ke(self, bo_loc=None):
        """Nhiệm vụ 3: dashboard tổng hợp. bo_loc: chuỗi lọc theo tên vị trí (tuỳ chọn)."""
        ds = [
            yc for yc in self.cac_yeu_cau_da_tao
            if not bo_loc or bo_loc.lower() in yc.vi_tri.lower()
        ]
        theo_vi_tri, theo_nhan_vien = [], {}
        tong_ho_so = tong_trung_tuyen = 0
        for yc in ds:
            ho_so = yc.tat_ca_ho_so()
            trung = sum(1 for hs in ho_so if hs.trang_thai == HS_TRUNG_TUYEN)
            tong_ho_so += len(ho_so)
            tong_trung_tuyen += trung
            ten = yc.nguoi_phu_trach.ho_ten if yc.nguoi_phu_trach else "Chưa giao"
            theo_vi_tri.append({
                "vi_tri": yc.vi_tri, "da_tuyen": yc.so_da_tuyen(), "so_luong": yc.so_luong,
                "nguoi_phu_trach": ten, "trang_thai": yc.trang_thai,
            })
            tk = theo_nhan_vien.setdefault(ten, {"ho_so": 0, "trung_tuyen": 0})
            tk["ho_so"] += len(ho_so)
            tk["trung_tuyen"] += trung
        return {
            "tong_yeu_cau": len(ds),
            "tong_ho_so": tong_ho_so,
            "tong_trung_tuyen": tong_trung_tuyen,
            "ti_le_trung_tuyen": round(tong_trung_tuyen / tong_ho_so * 100, 1) if tong_ho_so else 0.0,
            "theo_vi_tri": theo_vi_tri,
            "theo_nhan_vien": theo_nhan_vien,
        }

    def phe_duyet_ket_qua_cuoi(self, ho_so_ung_vien):
        """Nhiệm vụ 4: xác nhận lần cuối hồ sơ đã trúng tuyển.
        Bước này chỉ GHI NHẬN + báo ứng viên, không chặn luồng (nhân viên đã tự phê duyệt)."""
        yc = ho_so_ung_vien.tin_tuyen_dung.yeu_cau
        if yc not in self.cac_yeu_cau_da_tao:
            raise LoiQuyenHan("Hồ sơ này không thuộc yêu cầu do bạn tạo.")
        if ho_so_ung_vien.trang_thai != HS_TRUNG_TUYEN:
            raise LoiNghiepVu("Chỉ xác nhận hồ sơ đã trúng tuyển.")
        if ho_so_ung_vien.giam_doc_xac_nhan is not None:
            raise LoiNghiepVu("Hồ sơ này đã được xác nhận rồi.")
        ho_so_ung_vien.giam_doc_xac_nhan = date.today()
        ho_so_ung_vien.gui_thong_bao(
            f"Giám đốc đã xác nhận kết quả trúng tuyển vị trí '{yc.vi_tri}'."
        )
