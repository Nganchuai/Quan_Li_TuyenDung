"""
demo.py - Phụ trách: TV1
Chạy thử toàn bộ luồng nghiệp vụ bằng các class:  python demo.py
(Đặt cùng cấp với thư mục classes/)
"""

from datetime import date

from classes import (
    GiamDoc, NhanVienTuyenDung, UngVien, LoiNghiepVu, PV_DAT,
)

gd = GiamDoc(1, "Lưu Trọng Ngân", "gd", "123456", "Phòng IT")
nv = NhanVienTuyenDung(2, "Nguyễn Nhân Viên", "nv1", "abcdef", chuyen_mon="IT")

print("Đăng nhập đúng:", nv.dang_nhap("nv1", "abcdef"), "| sai:", nv.dang_nhap("nv1", "sai"))

yc = gd.tao_yeu_cau_tuyen_dung("IT Security", 2, "Biết pentest", date(2099, 12, 31))
gd.gan_nhan_vien_phu_trach(yc, nv)
tin = nv.dang_tin_tuyen_dung(yc, "Tuyển IT Security", "Lương thưởng tốt", "jd.pdf")

a = UngVien("Lê Văn A", "a@mail.com", "0901", kenh_nhan_tin=("email", "sms"))
b = UngVien("Phạm Thị B", "b@mail.com", "0902")
hs_a = a.nop_ho_so(tin, "3 năm kinh nghiệm")
hs_b = b.nop_ho_so(tin, "Mới ra trường")

try:
    a.nop_ho_so(tin, "nộp lại lần nữa")
except LoiNghiepVu as e:
    print("Chặn nộp trùng:", e)

nv.duyet_ho_so(hs_a, "phu_hop")
nv.duyet_ho_so(hs_b, "tu_choi", "Chưa đủ kinh nghiệm")
pv = nv.xep_lich_phong_van(hs_a, "10:00 30/12", "Phòng họp A")
nv.nhap_ket_qua_phong_van(pv, PV_DAT, "Giỏi")
gd.phe_duyet_ket_qua_cuoi(hs_a)

print("\n--- Hộp thư của A ---")
for tb in a.hop_thu:
    print(tb)
print("\n--- Hộp thư của B ---")
for tb in b.hop_thu:
    print(tb)

print("\nTra cứu của A:", a.tra_cuu_trang_thai("a@mail.com"))
print("Slot:", [(s.so_thu_tu, s.trang_thai) for s in yc.slots], "| Yêu cầu:", yc.trang_thai)
print("\nBáo cáo giám đốc:", gd.xem_bao_cao_thong_ke())
