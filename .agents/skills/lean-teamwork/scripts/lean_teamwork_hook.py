#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Antigravity PreInvocation Lifecycle Hook — Lean Teamwork (Pure CLI Two-Phase Edition)
Tự động tiêm thông điệp Re-Anchor tàng hình trước MỖI lượt gọi model.
Tích hợp:
1. Giám sát Account & Active Model thời gian thực.
2. Thiết Luật Minh Bạch Gợi Ý (BẮT BUỘC in bảng ma trận chi tiết trước khi mở cổng hỏi).
3. Thiết Luật Đối Chứng Trực Quan (Tự động mở /usr/bin/eog khi có ảnh screenshot).
"""

import sys
import json
import os
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def get_session_info():
    """Trích xuất tài khoản và model hiện hành siêu tốc (<5ms)."""
    acc = "aiagentmmo@gmail.com"
    acc_file = Path.home() / ".gemini" / "google_accounts.json"
    if acc_file.exists():
        try:
            data = json.loads(acc_file.read_text(encoding="utf-8"))
            acc = data.get("active", acc)
        except Exception:
            pass

    model = "Gemini 3.8 Flash (High)"
    log_file = Path.home() / ".gemini" / "antigravity-cli" / "cli.log"
    if log_file.exists():
        try:
            with open(log_file, "rb") as f:
                f.seek(0, 2)
                size = f.tell()
                f.seek(max(0, size - 50000))
                chunk = f.read().decode("utf-8", errors="ignore")
                for line in reversed(chunk.splitlines()):
                    if "Propagating selected model override to backend: label=" in line:
                        model = line.split("label=")[1].strip("\"' ")
                        break
        except Exception:
            pass

    return acc, model

def main():
    try:
        raw_input = sys.stdin.read() if not sys.stdin.isatty() else ""
        payload = json.loads(raw_input) if raw_input.strip() else {}
    except Exception:
        payload = {}

    acc, model = get_session_info()

    anchor_msg = (
        f"⚡ [MANDATORY RE-ANCHOR — Lean Teamwork Protocol (Pure CLI Two-Phase Edition)]:\n"
        f"📌 [STATUS]: Model: {model} | Account: {acc} | Status: Active\n"
        "1. 🔍 [INSPECT FIRST & ROOT CAUSE]: Cấm đoán mò! Đọc kỹ tài liệu/mã nguồn gốc trước khi đề xuất hoặc sửa. First-Time Right over trial-and-error.\n"
        "2. 🧭 [CHẾ ĐỘ ĐỀ XUẤT KỸ THUẬT & MINH BẠCH GỢI Ý]:\n"
        "   - BẮT BUỘC: TRƯỚC KHI gọi ask_question, AI PHẢI in ra BẢNG MA TRẬN PHÂN TÍCH CHI TIẾT toàn bộ các gợi ý gồm 5 cột:\n"
        "     | Phương Án | Cơ Chế Hoạt Động | Ưu Điểm | Nhược Điểm & Đánh Đổi | Rủi Ro & Lý Do Đề Xuất |\n"
        "   - CẤM TUYỆT ĐỐI hỏi cộc lốc hoặc chỉ đưa vài gạch đầu dòng vắn tắt khiến người dùng không đủ cơ sở để chọn!\n"
        "   - Phương án tối ưu bắt buộc có tiền tố '(Recommended)'. Gọi schedule 150s tự quyết nếu user vắng mặt.\n"
        "3. 🖼️ [ĐỐI CHỨNG TRỰC QUAN]: Khi sinh ảnh screenshot nghiệm thu (UI/Web/Test), BẮT BUỘC chạy lệnh shell '/usr/bin/eog <đường_dẫn_ảnh> &' trong nền để bật ảnh lên cho người dùng xem ngay!\n"
        "4. 💎 [CỔNG NGHIỆM THU HOÀN THIỆN & MINH BẠCH LỰA CHỌN]:\n"
        "   - BẮT BUỘC: TRƯỚC KHI gọi ask_question nghiệm thu, AI PHẢI in ra ĐỦ 2 BẢNG:\n"
        "     Bảng 1: Bảng Ma Trận Đối Chứng Thực Nghiệm (Hạng Mục, Lệnh Test, Exit Code, Rủi Ro Còn Lại, Trạng Thái).\n"
        "     Bảng 2: Bảng Giải Nghĩa Chi Tiết 2 Lựa Chọn:\n"
        "     | Lựa Chọn | Ý Nghĩa Kỹ Thuật | Hành Động Tiếp Theo Của AI | Khi Nào Nên Chọn? |\n"
        "   - CẤM TUYỆT ĐỐI hỏi cộc lốc hoặc mở modal nghiệm thu khi chưa in đủ 2 bảng chi tiết trên!\n"
        "5. 🔑 [MẬT MÃ NGHIỆM THU]: Tín hiệu hoàn tất là 'OK 💎' hoặc 'ok::'. Khi nhận mật mã, chạy Subagent Flash tự vấn 6 chiều và đúc kết vào ~/.agents/learned_patterns.md."
    )

    response = {
        "injectSteps": [
            {
                "ephemeralMessage": anchor_msg
            }
        ]
    }

    try:
        sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
        sys.stdout.flush()
    except Exception:
        pass
    sys.exit(0)

if __name__ == "__main__":
    main()
