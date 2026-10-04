<p align="center">
  <img src="assets/demo.gif" alt="Antigravity Lean Teamwork Live Demo" width="100%">
</p>

<p align="center">
  <a href="https://github.com/dongocanh0501/antigravity-lean-teamwork"><img src="https://img.shields.io/badge/target-Google%20Antigravity%20(Gemini%203.7%2F3.8)-4285F4.svg?style=for-the-badge&logo=google" alt="Google Antigravity Only"></a>
  <a href="https://github.com/dongocanh0501/antigravity-lean-teamwork"><img src="https://img.shields.io/badge/role-Phanh%20H%C3%A3m%20%E1%BA%A8u%20ABS-FF6D00.svg?style=for-the-badge" alt="Phanh Hãm Ẩu ABS"></a>
  <a href="https://github.com/dongocanh0501/antigravity-lean-teamwork/releases"><img src="https://img.shields.io/badge/version-1.6.0-00C853.svg?style=for-the-badge" alt="Version"></a>
  <a href="https://github.com/dongocanh0501/antigravity-lean-teamwork/releases"><img src="https://img.shields.io/badge/release-v1.6.0-blue.svg?style=for-the-badge&logo=github" alt="Release"></a>
  <a href="https://github.com/dongocanh0501/antigravity-lean-teamwork"><img src="https://img.shields.io/badge/tests-passing%20(100%25)-brightgreen.svg?style=for-the-badge" alt="Tests"></a>
  <a href="https://github.com/dongocanh0501/antigravity-lean-teamwork"><img src="https://img.shields.io/badge/license-MIT-purple.svg?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <b>⚡ Bộ Đôi Kỹ Năng Tinh Gọn + Desktop Widget HUD Dành Riêng Cho Google Antigravity & Antigravity CLI.</b><br/>
  <i>Chữa dứt điểm tật làm ẩu và cãi cọ với AI. Minh bạch hóa 100% gợi ý & nghiệm thu (Zero Blind Decisions) trên cả Terminal dòng lệnh lẫn Desktop Widget.</i>
</p>

---

> [!IMPORTANT]
> ### 📢 LƯU Ý ĐẶC BIỆT DÀNH CHO BẠN (DỰ ÁN XÂY DỰNG 100% TỰ ĐỘNG BỞI AI)
>
> 🤖 **100% AI-Native Development & Tự Động Git Push**:
> Toàn bộ mã nguồn, tính năng Desktop Widget HUD, hệ thống lifecycle hook và các bản cập nhật trên repo này đều do **AI (Antigravity Agent)** tự động lập trình, tự chạy kiểm thử và tự động `git push` trực tiếp trong quá trình pair-programming thực tế cùng tác giả.
>
> 🚀 **Cách Tốt Nhất: Hãy Kêu Chính AI Của Bạn Tự Tối Ưu Lại Cho Vừa Khít Máy Bạn**:
> Khi tải repo này về máy tính mới hoặc laptop của bạn, bạn chỉ cần mở thư mục này trong **Antigravity CLI** hoặc **Antigravity IDE** và ra lệnh:
>
> > 💬 *"Dự án này được build tự động trên máy khác. Hãy kiểm tra lại toàn bộ đường dẫn, môi trường khởi động trên máy tính của tôi, tối ưu và cài đặt hoàn thiện để chạy mượt mà 100% trên máy này!"*
>
> AI trên máy của bạn sẽ tự động đọc [`AGENTS.md`](AGENTS.md) / [`GEMINI.md`](GEMINI.md), nhận diện hệ điều hành (Linux/macOS/Windows), kiểm tra Python và tự động chạy script cài đặt từ A -> Z!

---

## 🌟 Có Gì Mới Ở Bản v1.6.0 (Pure CLI Two-Phase Edition)?

Bản nâng cấp **v1.6.0** giải quyết dứt điểm vấn đề lớn nhất khi sử dụng Antigravity CLI trên dòng lệnh: **AI đưa ra lựa chọn hoặc nghiệm thu cộc lốc khiến người dùng bị ép ra quyết định mù (Blind Decisions)**.

### 1. Chế Độ Pure CLI Two-Phase (Linux / macOS / Terminal)
- **Minh Bạch Gợi Ý (Proposal Gate — Bảng Ma Trận 5 Cột)**:  
  Trước khi người dùng chọn phương án, AI **BẮT BUỘC** in ra bảng ma trận so sánh đầy đủ 5 cột trực tiếp trong màn hình chat:
  `| Phương Án | Cơ Chế Hoạt Động | Ưu Điểm | Nhược Điểm & Đánh Đổi | Rủi Ro & Lý Do Đề Xuất |`
- **Minh Bạch Nghiệm Thu (Acceptance Gate — Kiến Trúc Twin-Table)**:  
  Trước khi nghiệm thu, AI **BẮT BUỘC** in đủ 2 bảng:
  1. *Bảng Ma Trận Đối Chứng Thực Nghiệm*: Liệt kê lệnh test, exit code 0, bằng chứng log và rủi ro còn lại.
  2. *Bảng Giải Nghĩa Chi Tiết 2 Lựa Chọn*: Giải thích cặn kẽ ý nghĩa kỹ thuật của `[100% HOÀN TẤT]` và `[SUPERPOWERS DEBUG]`.
- **Đối Chứng Trực Quan Tức Thì**:  
  Khi sinh ảnh screenshot kiểm thử (UI/Web/E2E), AI tự động kích hoạt tiến trình nền `/usr/bin/eog <đường_dẫn_ảnh> &` để mở ảnh lên màn hình cho bạn đối chứng ngay lập tức.
- **Giám Sát Phiên Siêu Tốc (<5ms)**:  
  PreInvocation Hook tự động nhận diện Model (`Gemini 3.8 Flash`) và Account đang hoạt động từ `google_accounts.json` và `cli.log`, hiển thị banner trạng thái ở đầu mỗi lượt chat.

### 2. Chế Độ Desktop Widget HUD Decoupled (Windows)
- Giữ nguyên sức mạnh của thanh kính mờ HUD nổi ngoài màn hình dành cho Antigravity Desktop App trên Windows: popover lựa chọn, đếm ngược Spectrum 2.5 phút và tương tác không che khuất khung chat.

---

## ⚡ Hướng Dẫn Cài Đặt Toàn Diện (1-Click Install)

### 🐧 Cách 1: Cài đặt trên Linux & macOS (1 Lệnh Duy Nhất)

Mở terminal và chạy lệnh:

```bash
git clone https://github.com/dongocanh0501/antigravity-lean-teamwork.git
cd antigravity-lean-teamwork
./install.sh
```

Hoặc chạy trực tiếp qua Python:
```bash
python3 scripts/sync_lean_teamwork.py
```

### 🪟 Cách 2: Cài đặt trên Windows (PowerShell 1-Click)

Mở PowerShell tại thư mục dự án và chạy:

```powershell
git clone https://github.com/dongocanh0501/antigravity-lean-teamwork.git
cd antigravity-lean-teamwork
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

*Script sẽ tự động nạp Skill, cấu hình Hook, tạo lối tắt ngoài Desktop và khởi động Desktop Widget.*

### 🤖 Cách 3: Cài đặt tự động qua Antigravity (AI-Driven)

Chỉ cần mở thư mục dự án trong Antigravity và gõ:
> **"Hãy cài đặt và sử dụng Lean Teamwork cho tôi"**

---

## 🗑️ Cách Gỡ Bỏ (Uninstall)

Khi bạn muốn đưa hệ thống về trạng thái ban đầu của Antigravity:

- **Trên Linux / macOS**:
  ```bash
  rm -rf ~/.agents/skills/lean-teamwork
  # Xóa entry "lean-teamwork-reanchor" trong ~/.gemini/config/hooks.json
  ```
- **Trên Windows**:
  ```powershell
  powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
  ```

---

## 🎯 Sự Thật Đằng Sau Bộ Kỹ Năng Này (The Naked Truth)

- 🏎️ **Tại sao lại cần Lean Teamwork?**  
  Gemini 3.7 và 3.8 trên Google Antigravity có tốc độ tư duy cực nhanh, nhưng cái tật cố hữu là **"quá nhanh quá nguy hiểm"**:
  - **Hay làm ẩu**: Lười đọc tài liệu/mã nguồn gốc ở lượt đầu vì sợ tốn token, dẫn đến đoán mò.
  - **Gây ức chế**: Đoán mò thì code lỗi, khiến **người dùng phải cãi lộn với AI**, bực bội bắt AI sửa đi sửa lại 5–10 lượt chat.
  - **Lean Teamwork chính là chiếc "phanh ABS"**: Buộc AI phải **Inspect First** (đọc kỹ trước khi sửa), in bảng ma trận so sánh chi tiết, kiểm thử độc lập phải đạt **Exit Code 0**, và chỉ kết thúc khi người dùng xác nhận nghiệm thu.

- 💡 **Tại sao không dùng cho Claude Code hay Cursor?**  
  Vì chỉ có Gemini 3.7 / 3.8 bị tật "hấp tấp, làm ẩu" này nên mới cần bộ phanh hãm chặt chẽ như vậy. Claude 3.7 hay OpenAI Codex vốn dĩ đã có tư duy chậm rãi, điềm đạm nên không cần lắp thêm phanh.

---

## 🏛️ Sơ Đồ Quy Trình Vận Hành (Diagon GraphDAG Standard)

```text
┌──────────┐                                         
│Turn Start│                                         
└┬─────────┘                                         
┌▽─────────────────────────────────────────────┐     
│PreInvocation Hook (auto-detect model/account)│     
└┬─────────────────────────────────────────────┘     
┌▽─────────────────┐                                 
│Re-Anchor Injected│                                 
└┬─────────────────┘                                 
┌▽──────────────────────────────────────┐            
│Proposal Gate (5-Column Matrix in Chat)│            
└┬──────────────────────────────────────┘            
┌▽───────────────────────────┐                       
│User Decision / 150s Timeout│                       
└┬───────────────────────────┘                       
┌▽──────────────────────────┐                        
│Inspect First & Code & Test│                        
└┬──────────────────────────┘                        
┌▽──────────────────────────────────────────────────┐
│Acceptance Gate (Evidence Table + Choice Semantics)│
└┬──────────────────────────────────────────────────┘
┌▽─────────────┐                                     
│OK 💎 Approved│                                     
└┬─────────────┘                                     
┌▽────────────────────────────────────┐              
│6-Dimensional Reflection (Pattern 11)│              
└─────────────────────────────────────┘              
```

---

## 🧪 Kết Quả Kiểm Thử Toàn Vẹn Hệ Thống (Integrity Test)

Chạy lệnh kiểm thử sau khi cài đặt:

```bash
python3 scripts/sync_lean_teamwork.py --verify
```

Kết quả thực tế đạt chuẩn 100%:

```text
============================================================
🔍 [KIỂM TRA TÍNH TOÀN VẸN HỆ THỐNG LEAN TEAMWORK]
============================================================
  ✓ [1/6] SKILL.md hợp lệ (105 dòng, đạt tiêu chuẩn < 150 dòng).
  ✓ [2/6] Đầy đủ 5/5 templates.
  ✓ [3/6] Đầy đủ 4/4 tài liệu tham chiếu.
  ✓ [4/6] PreInvocation Hook Script sẵn sàng và có quyền thực thi.
  ✓ [5/6] Kho tri thức ngoài sẵn sàng (48 patterns ghi nhận).
  ✓ [6/6] Hook đã được đăng ký thành công trong ~/.gemini/config/hooks.json.
------------------------------------------------------------
Kết quả: 6/6 tiêu chí đạt yêu cầu (100% PASS nếu 6/6).
============================================================
```

---

## 📁 Cấu Trúc Dự Án (Repository Structure)

```text
antigravity-lean-teamwork/
├── .agents/
│   └── skills/
│       └── lean-teamwork/
│           ├── SKILL.md               # Bộ luật điều phối tinh gọn (<150 dòng)
│           ├── references/            # Tài liệu tham chiếu sâu (Superpowers, Debugging)
│           ├── templates/             # Các mẫu brief, cycle audit, evaluation panel
│           └── scripts/               # Hook script & sync script
├── docs/
│   ├── learned_patterns.md            # Kho tri thức ngoài (đúc kết Pattern 11)
│   ├── self-evolution.md              # Đặc tả Tự Vấn 6 Chiều & Khử Phình Quy Tắc
│   ├── comparative-study.md           # Nghiên cứu so sánh chi tiết
│   └── architecture.md                # Kiến trúc tách biệt Core & Skill
├── scripts/
│   ├── lean_teamwork_hook.py          # PreInvocation Hook nhận diện model/account & re-anchor
│   ├── sync_lean_teamwork.py          # Script cài đặt & kiểm thử toàn vẹn 6/6
│   └── teamwork_bridge.py             # Cầu nối 2 chiều Lean Teamwork <-> Desktop Widget
├── widget/                            # Mã nguồn Desktop Widget HUD kính mờ (Windows)
│   ├── core/                          # GDI+, Popover, Window Tracker
│   └── main.py                        # Điểm khởi chạy Widget
├── install.sh                         # Script cài đặt 1-click cho Linux / macOS
├── install.ps1                        # Script cài đặt 1-click cho Windows
├── INSTALL.md                         # Hướng dẫn cài đặt chi tiết A-Z
├── CHANGELOG.md                       # Lịch sử nâng cấp phiên bản (v1.6.0)
├── VERSION                            # Phiên bản hiện hành (1.6.0)
└── LICENSE                            # Giấy phép mã nguồn mở MIT
```

---

## 📜 Giấy Phép (License)

Phát hành theo giấy phép **MIT License**. Xem chi tiết tại [LICENSE](LICENSE).

---
⭐ **Gắn Star cho repo nếu nó giúp bạn không còn phải cãi lộn với Gemini 3.7 / 3.8 nữa!** ⭐
