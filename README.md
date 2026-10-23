# Quan_Li_Tuyen_Dung
Đồ án PyThon Quản lí tuyển dụng
# HR Flow — Hệ thống Quản Lý Tuyển Dụng

> **Bài tập lớn — Lớp Python 04 — Nhóm [SỐ NHÓM]**

Ứng dụng desktop quản lý quy trình tuyển dụng của doanh nghiệp, viết bằng **Python**, giao diện **CustomTkinter**, dữ liệu lưu cục bộ bằng **SQLite**.

---

## 1. Thành viên nhóm

| STT | Họ và tên | MSSV | Vai trò | Tài khoản GitHub |
|:---:|-----------|------|---------|------------------|
| 1 | [Họ tên nhóm trưởng] | [MSSV] | Nhóm trưởng | [@username] |
| 2 | [Họ tên thành viên 2] | [MSSV] | [Vai trò] | [@username] |
| 3 | [Họ tên thành viên 3] | [MSSV] | [Vai trò] | [@username] |


---

## 2. Giới thiệu đề tài

Doanh nghiệp cần một công cụ để theo dõi toàn bộ vòng đời tuyển dụng: từ lúc Giám đốc đưa ra nhu cầu nhân sự, đến khi ứng viên được nhận. Hệ thống giúp:

- Giám đốc tạo yêu cầu tuyển dụng và giao cho nhân viên tuyển dụng phụ trách
- Nhân viên tuyển dụng đăng tin, duyệt hồ sơ, hẹn và chấm phỏng vấn
- Ứng viên nộp hồ sơ vào vị trí đang tuyển
- Số lượng cần tuyển được quản lý bằng **SLOT**, tự cập nhật khi có người trúng tuyển

### Quy trình nghiệp vụ

```
GIÁM ĐỐC → Tạo yêu cầu tuyển dụng → Giao nhân viên phụ trách → Hệ thống tự sinh SLOT
NHÂN VIÊN TUYỂN DỤNG → Đăng tin tuyển dụng (kèm file JD)
ỨNG VIÊN → Nộp hồ sơ
NHÂN VIÊN TUYỂN DỤNG → Duyệt hồ sơ → (Từ chối | Hẹn phỏng vấn)
PHỎNG VẤN → (Không đạt: Từ chối | Đạt: Tuyển dụng thành công → Cập nhật SLOT)
```

---

## 3. Phân quyền

| Chức năng | Giám đốc | Nhân viên tuyển dụng |
|-----------|:--------:|:--------------------:|
| Xem tổng quan toàn công ty + hiệu suất từng nhân viên | ✓ | |
| Xem tổng quan phần việc của mình | | ✓ |
| Tạo yêu cầu tuyển dụng, giao việc | ✓ | |
| Đăng tin tuyển dụng, đính kèm file | | ✓ |
| Xem slot tuyển dụng | ✓ | ✓ |
| Xem hồ sơ ứng viên | ✓ | ✓ |
| Duyệt hồ sơ, hẹn phỏng vấn | | ✓ |
| Nhập kết quả phỏng vấn | | ✓ |

---

## 4. Tính năng đã hoàn thành

- Đăng nhập, phân quyền theo vai trò (mật khẩu được băm bằng PBKDF2 + salt)
- Tạo yêu cầu tuyển dụng, tự sinh SLOT, giao cho nhân viên phụ trách
- Soạn và đăng tin tuyển dụng kèm file đính kèm (JD)
- Nộp hồ sơ ứng viên
- Duyệt hồ sơ: từ chối (ghi lý do) hoặc hẹn phỏng vấn
- Nhập kết quả phỏng vấn, tự gán ứng viên vào SLOT trống đầu tiên
- Dashboard thống kê, biểu đồ, tiến độ từng vị trí, hiệu suất nhân viên

## 5. Hướng phát triển

- Trang web công khai để ứng viên xem tin và nộp hồ sơ không cần tài khoản
- Chống nộp hồ sơ trùng lặp / spam
- Gửi thông báo kết quả cho ứng viên qua email / SMS
- Đánh giá, chấm điểm ứng viên sau phỏng vấn

---

## 6. Công nghệ sử dụng

| Thành phần | Công nghệ |
|-----------|-----------|
| Ngôn ngữ | Python 3.9+ (khuyến nghị 3.10 – 3.12) |
| Giao diện | CustomTkinter |
| Biểu đồ | Matplotlib |
| Cơ sở dữ liệu | SQLite |

---

## 7. Cấu trúc dự án

```
tuyendung_app/
├── main.py              # Điểm khởi chạy, cửa sổ chính, sidebar, phân quyền menu
├── database.py          # Toàn bộ thao tác SQLite + xác thực đăng nhập
├── theme.py             # Bảng màu, font dùng chung
├── widgets.py           # Widget tái sử dụng: StatCard, Badge, Table, Toast, Dialog
├── requirements.txt
├── README.md
├── PHANCONG.md
└── pages/
    ├── __
    ├── login.py         # Màn hình đăng nhập
    ├──
    ..........................
    
```

---



| Tên đăng nhập | Mật khẩu | Vai trò |
|---------------|----------|---------|
| `admin` | `admin123` | Giám đốc |

> Nên đổi mật khẩu sau lần đăng nhập đầu tiên. Tài khoản nhân viên tuyển dụng được tạo bằng hàm `create_user()` trong `database.py`.

---

## 9. Quy ước làm việc nhóm

- Mỗi thành viên commit file theo đúng phân công trong `PHANCONG.md`
- Commit message viết rõ ràng, ví dụ: `Thêm trang duyệt hồ sơ (review.py)`
- Không commit file `tuyendung.db` chứa dữ liệu thật và thư mục `attachments/`
