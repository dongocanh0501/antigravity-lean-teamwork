#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Antigravity Lean Teamwork - Proposal Choice Listener
Lắng nghe tương tác chọn đề xuất từ Desktop Widget (qua teamwork_bridge.json)
hoặc tự động kích hoạt Phương án [1] (Khuyên dùng) khi hết giờ (timeout).
Đảm bảo Antigravity tiếp tục thực thi ngay lập tức, không bao giờ bị dừng phiên.
"""

import sys
import time
import json
import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import teamwork_bridge


def main():
    parser = argparse.ArgumentParser(description="Wait for proposal choice on Desktop Widget or timeout fallback.")
    parser.add_argument("--timeout", type=int, default=150, help="Timeout in seconds (default: 150)")
    parser.add_argument("--default-option", type=int, default=1, help="Default option ID on timeout (default: 1)")
    parser.add_argument("--interval", type=float, default=0.5, help="Polling interval in seconds (default: 0.5)")
    args = parser.parse_args()

    start_time = time.time()
    deadline = start_time + args.timeout

    print(f"⏳ [PROPOSAL_LISTENER]: Đang lắng nghe lựa chọn từ Desktop Widget (Hạn chót: {args.timeout}s)...", flush=True)

    while time.time() < deadline:
        resp = teamwork_bridge.check_user_response(mark_handled=True)
        if resp:
            resp_ts = resp.get("timestamp", 0.0)
            # Chỉ nhận phản hồi mới sinh ra trong hoặc ngay trước phiên lắng nghe này
            if resp_ts >= (start_time - 0.5):
                act = resp.get("action")
                if act == "SELECT_OPTION":
                    opt_id = resp.get("selected_option_id", args.default_option)
                    note = resp.get("note", "")
                    print(f"[WIDGET_SELECTION]: Người dùng đã chọn Phương án [{opt_id}] ('{note}') trên Desktop Widget!", flush=True)
                    sys.exit(0)
                elif act == "PAUSE":
                    print("[WIDGET_PAUSE]: Người dùng đã yêu cầu tạm dừng đồng hồ để nhập phản hồi riêng.", flush=True)
                    sys.exit(0)
        time.sleep(args.interval)

    # Hết hạn thời gian (Timeout fallback)
    teamwork_bridge.submit_user_response(
        action="SELECT_OPTION",
        selected_option_id=args.default_option,
        note=f"Tự động kích hoạt Phương án [{args.default_option}] (Khuyên dùng) do hết {args.timeout}s"
    )
    print(f"[TIMEOUT]: Đã hết {args.timeout}s chờ. Tự động kích hoạt Phương án [{args.default_option}] (Khuyên dùng)!", flush=True)
    sys.exit(0)


if __name__ == "__main__":
    main()
