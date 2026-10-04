#!/usr/bin/env bash
# ====================================================================
# Antigravity Lean Teamwork — 1-Click Installer for Linux & macOS
# ====================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VERSION="1.6.0"

if [ -f "$SCRIPT_DIR/VERSION" ]; then
    VERSION="$(cat "$SCRIPT_DIR/VERSION" | tr -d '[:space:]')"
fi

echo "============================================================"
echo "  🚀 CÀI ĐẶT ANTIGRAVITY LEAN TEAMWORK v$VERSION (PURE CLI TWO-PHASE)"
echo "============================================================"

# 1. Kiểm tra Python
echo -e "\n[1/3] Kiểm tra môi trường Python..."
if command -v python3 &>/dev/null; then
    PY_CMD="python3"
elif command -v python &>/dev/null; then
    PY_CMD="python"
else
    echo -e "❌ [ERROR] Không tìm thấy Python 3! Vui lòng cài đặt Python 3.10+ trước."
    exit 1
fi

PY_VER="$($PY_CMD --version 2>&1)"
echo "  ✓ Tìm thấy: $PY_VER"

# 2. Cấp quyền thực thi các script
echo -e "\n[2/3] Cấp quyền thực thi các script..."
chmod +x "$SCRIPT_DIR/scripts/lean_teamwork_hook.py" 2>/dev/null || true
chmod +x "$SCRIPT_DIR/scripts/sync_lean_teamwork.py" 2>/dev/null || true

# 3. Đồng bộ Skill & Hook vào Antigravity
echo -e "\n[3/3] Nạp Lean Teamwork Protocol & PreInvocation Hook vào Antigravity..."
$PY_CMD "$SCRIPT_DIR/scripts/sync_lean_teamwork.py"

echo -e "\n============================================================"
echo "  🎉 CÀI ĐẶT HOÀN TẤT 100%! HỆ THỐNG ĐÃ SẴN SÀNG!"
echo "  • Phiên bản: v$VERSION (Pure CLI Two-Phase Edition)"
echo "  • Skill: ~/.agents/skills/lean-teamwork"
echo "  • Lifecycle Hook: ~/.gemini/config/hooks.json"
echo "  • Zero Blind Decisions: Bảng ma trận 5 cột kích hoạt tự động"
echo "============================================================"
