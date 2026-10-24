"""
classes/hang_so.py
Phụ trách: TV1 - Lưu Trọng Ngân (nhóm trưởng)
Hằng số trạng thái, ngoại lệ nghiệp vụ và hàm cấp id - dùng chung cho mọi class.
"""

# Hồ sơ ứng viên
HS_MOI_NOP = "Mới nộp"
HS_DA_DUYET = "Đã duyệt"
HS_CHO_PV = "Chờ phỏng vấn"
HS_TRUNG_TUYEN = "Trúng tuyển"
HS_TU_CHOI = "Từ chối"

# Yêu cầu tuyển dụng
YC_CHO_DANG = "Chờ đăng"
YC_DANG_TUYEN = "Đang tuyển"
YC_DA_DU = "Đã tuyển đủ"

# Phỏng vấn
PV_DA_LEN_LICH = "Đã lên lịch"
PV_DAT = "Đạt"
PV_KHONG_DAT = "Không đạt"

# Kênh gửi thông báo
KENH_HOP_LE = ("app", "email", "sms")


class LoiNghiepVu(Exception):
    """Vi phạm quy tắc nghiệp vụ (nộp trùng, hết slot, sai trạng thái...)."""


class LoiQuyenHan(LoiNghiepVu):
    """Người dùng làm việc không thuộc quyền của mình."""


def lay_id(bo_dem, id):
    """Dùng id được truyền vào, nếu None thì tự cấp số tiếp theo."""
    return id if id is not None else next(bo_dem)
