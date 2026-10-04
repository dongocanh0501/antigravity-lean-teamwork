# 🚀 HƯỚNG DẪN CÀI ĐẶT TOÀN DIỆN CHO MÁY MỚI (INSTALLATION GUIDE)

> **Antigravity Lean Teamwork v1.6.0 (Pure CLI Two-Phase & Desktop Widget HUD Monorepo)**  
> Bộ công cụ tối thượng: Kỷ luật kỹ thuật tinh gọn cho Google Antigravity & Antigravity CLI kết hợp thanh trạng thái kính mờ HUD nổi ngoài màn hình trên Windows.

> [!TIP]
> ### 💡 Dành Cho Người Dùng Mới / Máy Mới:
> Khi chuyển sang một máy tính mới hoàn toàn, bạn chỉ cần mở thư mục này trong Antigravity CLI hoặc IDE và chat duy nhất một câu:  
> **"Hãy cài đặt và sử dụng cho tôi"** (hoặc *"setup"*, *"cài đặt"*).  
> AI sẽ tự động kích hoạt script cài đặt ngầm, tự động thiết lập toàn bộ môi trường đạt độ hoàn thiện 100% y hệt máy gốc mà bạn không cần phải làm thêm thao tác nào!

---

## 📋 1. Yêu Cầu Hệ Thống (Prerequisites)

- **Hệ điều hành**: Linux (Ubuntu, Debian, Fedora, Arch...), macOS, hoặc Windows 10/11 (64-bit).
- **Python**: Phiên bản 3.10 trở lên (khuyên dùng Python 3.11, 3.12, 3.13 hoặc 3.14).
  - Không cần cài thêm bất kỳ thư viện pip ngoài nào (100% Python Standard Library).
  - Kiểm tra trong terminal:
    ```bash
    python3 --version
    # hoặc trên Windows
    py --version
    ```
- **Môi trường chạy**: Google Antigravity (Gemini 3.7 / 3.8) hoặc Antigravity CLI (`agy`).

---

## ⚡ 2. Cài Đặt Nhanh 1-Click (Recommended)

### 🐧 A. Trên Linux & macOS (Bash 1-Click):

Sau khi clone repository về máy:

```bash
git clone https://github.com/dongocanh0501/antigravity-lean-teamwork.git
cd antigravity-lean-teamwork
./install.sh
```

Hoặc chạy trực tiếp qua Python:
```bash
python3 scripts/sync_lean_teamwork.py
```

### 🪟 B. Trên Windows (PowerShell 1-Click):

```powershell
git clone https://github.com/dongocanh0501/antigravity-lean-teamwork.git
cd antigravity-lean-teamwork
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

### 🛠️ Script Cài Đặt Sẽ Tự Động Thực Hiện:
1. Nạp **Lean Teamwork Protocol v1.6.0** vào cấu hình Antigravity (`~/.agents/skills/lean-teamwork`).
2. Kích hoạt **PreInvocation Lifecycle Hook** (`~/.gemini/config/hooks.json`) để luôn tự động tuân thủ kỷ luật kỹ thuật (tự động phát hiện model & account active).
3. Hợp nhất kho tri thức kinh nghiệm **Learned Patterns** (`~/.agents/learned_patterns.md`).
4. Trên Linux: Kích hoạt chế độ **Pure CLI Two-Phase** (Bảng 5 cột đề xuất & 2 bảng nghiệm thu).
5. Trên Windows: Khởi động thanh **Antigravity Desktop Widget** nổi ngoài màn hình và tạo lối tắt Desktop.

---

## 🖱️ 3. Cài Đặt Thủ Công Từng Bước (Manual Setup)

Nếu bạn muốn tự tay kiểm soát từng bước mà không chạy script tự động:

### Bước 1: Đồng bộ Skill & Hook vào Antigravity
- Trên Linux / macOS:
  ```bash
  python3 scripts/sync_lean_teamwork.py
  ```
- Trên Windows:
  ```powershell
  py sync_skill.py
  ```

### Bước 2 (Chỉ dành cho Windows): Khởi động Desktop Widget HUD
- Chạy qua Python:
  ```powershell
  pythonw widget\main.py
  ```
- Hoặc double-click trực tiếp vào file:
  `widget\KHOI_DONG_WIDGET.vbs` (chạy ngầm êm ái, không hiện console đen).

---

## 🎯 4. Trải Nghiệm & Vận Hành Thực Tế

### 🧭 A. Đề Xuất Kỹ Thuật (Proposal Mode):
- **Khung chat Terminal / CLI**: AI bắt buộc in **Bảng Ma Trận So Sánh 5 Cột** (`Phương Án | Cơ Chế Hoạt Động | Ưu Điểm | Nhược Điểm & Đánh Đổi | Rủi Ro & Lý Do Đề Xuất`) trước khi hỏi. Bạn có đầy đủ thông tin để chọn `1`, `2` hoặc `3`.
- **Desktop Widget HUD (Windows)**: Bung bảng popover kính mờ với đồng hồ Spectrum đếm ngược 150s.

### 💎 B. Nghiệm Thu Hoàn Thiện (Acceptance Mode):
- Khi code xong và test đạt **100% PASS (Exit Code 0)**:
- **Khung chat Terminal / CLI**: In đủ **2 Bảng** (Bảng Đối Chứng Thực Nghiệm + Bảng Giải Nghĩa Chi Tiết 2 Lựa Chọn).
- **Xem ảnh trực quan**: AI tự động bật `/usr/bin/eog <ảnh> &` để bạn kiểm tra screenshot UI ngay lập tức.
- Bạn chọn `1` (`[100% HOÀN TẤT]`) để kết thúc và kích hoạt chu trình tự tiến hóa.

---

## 🛡️ 5. Kiểm Thử Toàn Vẹn Hệ Thống (Verification)

Bất kỳ lúc nào bạn muốn kiểm tra xem toàn bộ hệ thống có hoạt động chuẩn xác 100% hay không:

- Trên Linux / macOS:
  ```bash
  python3 scripts/sync_lean_teamwork.py --verify
  ```
- Trên Windows:
  ```powershell
  py tests\test_skill_integrity.py
  py tests\test_teamwork_bridge.py
  ```

*Tiêu chuẩn: Toàn bộ 6/6 (CLI) hoặc 14/14 (Windows) kiểm thử phải PASS (Exit Code 0).*

---

## 🧹 6. Gỡ Bỏ Khỏi Antigravity Toàn Cục (Uninstall)

Khi bạn muốn đưa Antigravity về trạng thái nguyên bản sạch sẽ:

- **Trên Linux / macOS**:
  ```bash
  rm -rf ~/.agents/skills/lean-teamwork
  # Xóa hook "lean-teamwork-reanchor" trong ~/.gemini/config/hooks.json
  ```
- **Trên Windows**:
  ```powershell
  powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
  ```
