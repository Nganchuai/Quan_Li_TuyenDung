# PHÂN CÔNG NHIỆM VỤ - NHÓM 7

**Lớp:** Python 04
**Đề tài:** HR Flow - Hệ thống quản lý tuyển dụng
**Giai đoạn:** Tuần 1 - Viết các class của bài tập lớn

## 1. Thành viên

| STT | Họ và tên | Tài khoản GitHub | Vai trò |
|---|---|---|---|
| TV1 | Lưu Trọng Ngân | Nganchuai| Nhóm trưởng |
| TV2 | [Họ tên TV2] | [github TV2] | Thành viên |
| TV3 | [Họ tên TV3] | [github TV3] | Thành viên |


## 2. Yêu cầu tuần 1

Mỗi thành viên viết 2 class theo bảng dưới. Mỗi class gồm `__init__` (các thuộc tính) và các hàm chức năng (chỉ cần khung hàm kèm chú thích, không cần chạy được). Mỗi class nằm trong 1 file riêng, đặt trong thư mục `classes/`.

## 3. Bảng phân công

| Thành viên | File | Class | Nội dung chính |
|---|---|---|---|
| **Lưu Trọng Ngân** (nhóm trưởng) | `classes/nguoi_dung.py` | `NguoiDung` | Lớp cha chung: id, họ tên, username, password, vai trò; hàm đăng nhập |
| | `classes/giam_doc.py` | `GiamDoc` | Kế thừa `NguoiDung`: tạo yêu cầu tuyển dụng, gán nhân viên phụ trách, xem thống kê, phê duyệt kết quả cuối |
| | `classes/ho_so_ung_vien.py` | `HoSoUngVien` | Ứng viên, tin ứng tuyển, trạng thái, lý do từ chối |
| | `classes/thong_bao.py` | `ThongBao` | Hồ sơ liên quan, kênh gửi (app, email, SMS), nội dung, trạng thái gửi; hàm gửi |
| **TV2** | `classes/nhan_vien_tuyen_dung.py` | `NhanVienTuyenDung` | Kế thừa `NguoiDung`: đăng tin, duyệt hồ sơ, xếp lịch phỏng vấn, nhập kết quả phỏng vấn |
| | `classes/yeu_cau_tuyen_dung.py` | `YeuCauTuyenDung` | Vị trí, số lượng, mô tả, hạn tuyển, người phụ trách, trạng thái |
| **TV3** | `classes/ung_vien.py` | `UngVien` | Họ tên, email, SĐT; hàm nộp hồ sơ, tra cứu trạng thái (không có tài khoản) |
| | `classes/tin_tuyen_dung.py` | `TinTuyenDung` | Yêu cầu liên quan, mô tả, quyền lợi, file đính kèm, công khai hay nội bộ |



## 4. Nhiệm Vụ Đầu

- Tạo repo trên GitHub, tên `Nhom7-python04`, để chế độ Public.
- Add 3 thành viên vào repo (Settings, Collaborators, Add people).
- Upload file `PHANCONG.md` này.
- Cuối tuần: tạo `link.txt` (một dòng là link repo) và nộp.

## 5. Quy ước commit

- Mỗi người chỉ commit 2 file của mình.
- Nội dung commit ghi rõ, ví dụ: `TV2: them class NhanVienTuyenDung`.


## 6. Hạn nộp

Các thành viên commit xong phần của mình trước: [25/11].
