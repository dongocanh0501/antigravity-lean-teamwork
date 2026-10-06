---
name: lean-teamwork
description: Kích hoạt quy trình điều phối đa tác tử tinh gọn (Lean Multi-Agent Protocol), tối ưu hóa quota/token với Independent Evidence Gates, Inspect First và Native Modal tương tác trên Antigravity CLI. Sử dụng khi cần làm việc theo mô hình Lean Teamwork, tối ưu token, hoặc chia việc đa agent có kiểm soát chặt chẽ.
---

# Lean Teamwork Skill — Antigravity CLI Edition

Hệ thống điều phối tinh gọn kết hợp kỷ luật thép từ **Superpowers** và cơ chế tối ưu hóa Quota & Token từ **Lean Teamwork Protocol**, được tối ưu hóa cho Antigravity CLI trên Linux.

---

## 1. 3 Thiết Luật Bất Biến (The 3 Iron Laws)

Mọi agent và phiên làm việc kích hoạt skill này bắt buộc phải tuân thủ 3 thiết luật:

1. **Thiết Luật Nghiệm Thu (Iron Law of Verification)**:
   > *"NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE"*
   - Không được tuyên bố code chạy, bug đã sửa hay test đã pass nếu chưa chạy lệnh kiểm chứng trực tiếp ngay trong lượt làm việc.
   - Cấm tuyệt đối các từ ngữ phỏng đoán: *"should work"*, *"probably"*, *"looks correct"*, *"tôi tin rằng"*.
2. **Thiết Luật Nguyên Nhân Gốc & Làm Đúng Lần Đầu (Root Cause & First-Time Right Protocol)**:
   > *"NO FIXES WITHOUT ROOT CAUSE — FIRST-TIME RIGHT OVER TRIAL-AND-ERROR"*
   - Cấm sửa mò, thử sai hay sửa triệu chứng (symptom fixing). Phải đọc stacktrace, tái hiện lỗi ổn định và khoanh vùng chính xác trước khi chạm vào code.
   - **Khai tử tư duy "Blind Lean"**: Lean KHÔNG PHẢI là mù quáng không đọc tài liệu. Khi chạm vào kiến trúc, framework hay mã nguồn mới, **BẮT BUỘC phải đọc tài liệu chuẩn (Inspect First đầy đủ)** để hiểu rõ mọi ràng buộc ngầm.
   - **Cấm đoán mò vì sợ tốn token đọc tài liệu**: Tiết kiệm vài trăm token đọc tài liệu ở đầu phiên mà để phát sinh >2 lượt chat thử-sai do đoán mò là **phạm luật Quota nghiêm trọng**.
3. **Thiết Luật Tự Quyết Định & Hướng Đi Tốt Nhất (Ruling & Best-Path Fallback)**:
   > *"A RUNNING PLAN DOES NOT WAIT ON A HUMAN FOR MINOR CHOICES"*
   - Tự ra phán quyết cho các vấn đề vi mô kèm ghi chú rủi ro (`Ruling: <Quyết định> — <Lý do> — <Hệ quả nếu sai>`).
   - **Tự quyết khi quá thời gian chờ (Timeout Best-Path Fallback)**:
     - Thời gian chờ mặc định: **2.5 phút (150 giây)**.
     - Khi đứng trước ngã rẽ kỹ thuật, hiển thị rõ ràng các lựa chọn qua `ask_question` kèm phương án `(Recommended)`.
     - Đồng thời đặt hẹn giờ `schedule(DurationSeconds=150, TimerCondition="any", Prompt="Hết thời gian 2.5 phút, tự động thi hành phương án Recommended")`.
     - Hết 2.5 phút không có phản hồi: Tự động thi hành phương án khuyến nghị, không để phiên bị treo.
   - Chỉ dừng lại chờ người dùng tuyệt đối khi gặp: (1) Thao tác phá hủy/xóa dữ liệu, (2) Thay đổi Auth/Security, (3) Tác động ngoài workspace, hoặc (4) Yêu cầu mâu thuẫn hoàn toàn.

---

## 2. Hai Chế Độ Vận Hành

### Chế Độ 1: Daily Lean Mode (Sửa Bug & Tác Vụ Hàng Ngày 1–3 Files)
1. **Systematic Debugging & Pattern Retrieval**:
   - Khi gặp lỗi phức tạp: Liếc nhanh [`~/.gemini/config/learned_patterns.md`](file:///home/dongocanh/.gemini/config/learned_patterns.md) để tái sử dụng giải pháp thành công.
   - Đọc kỹ stacktrace/mã lỗi và tái hiện lỗi qua test case tối thiểu (Red Phase).
2. **Minimal Compatible Diff**:
   - Sửa đúng nguyên nhân gốc trong 1 thao tác diff nhỏ nhất.
   - Tự sửa lỗi cú pháp vi mô trong 1 lượt duy nhất (Zero-Spawn Minor Remediation).
3. **Green Verification**: Chạy lại test -> Xác nhận PASS (Exit Code 0).
4. **Cổng Nghiệm Thu**: Xuất kết quả và mở cổng nghiệm thu qua `ask_question`.

### Chế Độ 2: Multi-Agent Lean Mode (Tác Vụ Lớn / Tái Cấu Trúc Đa Module)
1. **Intent Architect**: Phỏng vấn tạo và khóa [Execution Brief](./templates/execution_brief_template.md).
2. **Subagent Cap (2–4 Subagents)**: 1 Lead Orchestrator, tối đa 2 Workers song song sở hữu file độc quyền, 1 Gatekeeper / Independent Auditor.
3. **Model Tiering**:
   - `Model: "flash"` hoặc `"flash_lite"`: Dùng cho Explorer khảo sát, Gatekeeper chạy test, kiểm tra log, Synthesizer đúc kết bài học.
   - `Model: "inherit"` hoặc `"pro"`: Dành riêng cho Lead Orchestrator và Worker viết thuật toán phức tạp.
4. **Compact Handoff**: Báo cáo giữa các agent bắt buộc dưới 20 dòng theo mẫu [Compact Handoff](./templates/compact_handoff_template.md).

---

## 3. Quy Trình 2 Cổng Native Modal Trên Antigravity CLI (Pure CLI Two-Phase)

### 1. 🧭 [CHẾ ĐỘ ĐỀ XUẤT KỸ THUẬT & KẾ HOẠCH TRIỂN KHAI TRÊN CLI (CLI-FIRST)] (Two-Phase Workflow)
- **Khi nào kích hoạt**: Khi vừa nhận yêu cầu mới, phân tích hướng đi, lập kế hoạch (`/plan`), hoặc đứng trước các ngã rẽ kỹ thuật quan trọng.
- **Quy chuẩn 2 nhịp bắt buộc**:
  1. **NHỊP 1 (XUẤT TOÀN BỘ BÀI PHÂN TÍCH, MA TRẬN 5 CỘT & KẾ HOẠCH CHI TIẾT RA CLI)**:
     - AI BẮT BUỘC xuất toàn bộ bài phân tích kỹ thuật, Bảng Ma Trận So Sánh 5 Cột, và **Kế Hoạch Triển Khai Chi Tiết (Full Implementation Plan)** trực tiếp ra màn hình CLI bằng Markdown:
       `| Phương Án | Cơ Chế Hoạt Động | Ưu Điểm | Nhược Điểm & Đánh Đổi | Rủi Ro & Lý Do Đề Xuất |`
     - Phương án tối ưu nhất bắt buộc đánh dấu tiền tố `(Recommended)`.
     - **CẤM TUYỆT ĐỐI**: CẤM giấu kế hoạch trong file artifact `.md` rồi chỉ dẫn link tóm tắt. CẤM gọi tool `ask_question` trong nhịp này khi chưa xuất bài phân tích/kế hoạch đầy đủ ra CLI.
  2. **NHỊP 2 (CỔNG LỰA CHỌN PHƯƠNG ÁN & HẸN GIỜ TỰ QUYẾT)**:
     - Sau khi nội dung phân tích & kế hoạch đã hiển thị trọn vẹn trên màn hình CLI ở Nhịp 1, mới mở công cụ `ask_question` để người dùng lựa chọn phương án.
     - Kết hợp đặt hẹn giờ `schedule(DurationSeconds=150, TimerCondition="any", Prompt="Hết thời gian 2.5 phút, tự động thi hành phương án Recommended")` tự quyết nếu người dùng vắng mặt.

### 2. 💎 [CHẾ ĐỘ NGHIỆM THU HOÀN THIỆN] (Acceptance Gate)
- **Khi nào kích hoạt**: Khi code đã viết xong, toàn bộ kiểm thử tích hợp đạt 100% PASS (Exit Code 0).
- **Quy trình 2 nhịp bắt buộc**:
  - **NHỊP 1 (IN ĐỦ 2 BẢNG BÁO CÁO & ĐỐI CHỨNG RA CLI)**: BẮT BUỘC in ĐỦ 2 BẢNG trực tiếp ra màn hình CLI bằng Markdown trước khi mở modal nghiệm thu:
    1. *Bảng Ma Trận Đối Chứng Thực Nghiệm* (Hạng mục, Lệnh test, Exit Code, Rủi ro, Trạng thái).
    2. *Bảng Giải Nghĩa Chi Tiết 2 Lựa Chọn Nghiệm Thu* (`[100% HOÀN TẤT]` vs `[SUPERPOWERS DEBUG]`).
    Nếu có ảnh screenshot (UI/Web preview), BẮT BUỘC chạy ngầm `/usr/bin/eog <đường_dẫn_ảnh> &` để mở ảnh trực tiếp trên màn hình!
  - **NHỊP 2 (MỞ CỔNG NGHIỆM THU QUA `ask_question`)**:
    Chỉ mở modal `ask_question` lựa chọn 2 trạng thái sau khi đã in đủ 2 bảng chi tiết ở Nhịp 1 ra CLI. CẤM TUYỆT ĐỐI mở modal hỏi khi chưa in đối chứng ra màn hình CLI!

### 3. Chuẩn Hóa Mật Mã Nghiệm Thu (`OK 💎` / `ok::`)
- **Tín hiệu nghiệm thu chuẩn hóa**: Chỉ kích hoạt khi nhận được mật mã **`OK 💎`** (hoặc `ok::`, `[ACCEPT] 💎`).
- **Quy tắc Chống Nhầm Lẫn (Anti-False-Acceptance)**: Các từ "ok" trao đổi thông thường (*"ok làm tiếp đi", "ok nhé"...*) KHÔNG PHẢI là lệnh nghiệm thu.
- Khi bắt được mật mã `OK 💎` hoặc `ok::`: Agent kích hoạt Subagent (`flash`, role: `Knowledge Synthesizer`) thực thi **Tự Vấn 6 Chiều** và nạp bài học vào `~/.gemini/config/learned_patterns.md`.

### 4. 🖼️ [THIẾT LUẬT ĐỐI CHỨNG TRỰC QUAN] (Visual Inspection On Linux)
- Khi AI thực hiện chụp ảnh màn hình nghiệm thu (UI, Web preview, visual artifact):
  - BẮT BUỘC kích hoạt lệnh chạy ngầm: `run_command(CommandLine="/usr/bin/eog <đường_dẫn_ảnh> &")`.
  - Cửa sổ xem ảnh sẽ tự động bật lên màn hình Ubuntu GNOME để người dùng đối chứng trực quan ngay tức thì, ngang ngửa trải nghiệm Desktop App!

---

## 4. Nguyên Tắc Cách Ly Tri Thức & Khử Phình Quy Tắc (Anti-Rule-Bloat)

1. **SKILL.md Chỉ Chứa Luật Điều Phối (<150 dòng)**: Tuyệt đối không nhồi nhét log sửa lỗi, code mẫu hay bài học tình huống vào đây.
2. **Kho Tri Thức Nằm Bên Ngoài**: Lưu tại [`~/.gemini/config/learned_patterns.md`](file:///home/dongocanh/.gemini/config/learned_patterns.md).
3. **Bộ Tự Vấn Phản Tư 6 Chiều**:
   - Q1: *Tại sao lần trước phải làm lại?*
   - Q2: *Làm sao để lần sau làm chuẩn xác 100% ngay từ lượt 1?*
   - Q3: *Có bước nào làm lãng phí token không? Cắt giảm ra sao?*
   - Q4: *Có thể tự động hóa quy tắc này thành script/hook không?*
   - Q5: *Có bài học cũ nào thừa hoặc trùng lặp cần GỘP (Merge) hoặc XÓA (Prune) không?*
   - Q6: *Có điểm nghẽn nào cần khắc phục dứt điểm không?*
4. **Khóa Trần 10 Patterns**: Kho tri thức được giới hạn tối đa 10 patterns tinh hoa để giữ bộ não AI luôn nhẹ và sắc bén.
