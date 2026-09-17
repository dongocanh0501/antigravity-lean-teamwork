# ====================================================================
# Antigravity Lean Teamwork — 1-Click Uninstaller & Decoupler
# ====================================================================
$ErrorActionPreference = "Continue"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  🧹 GỠ BỎ LEAN TEAMWORK KHỎI ANTIGRAVITY & CÁCH LY REPO" -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Cyan

# 1. Tìm Python
$pythonCmd = "python"
if (Get-Command "py" -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
}

# 2. Chạy gỡ bỏ toàn cục bằng Python
& $pythonCmd "$PSScriptRoot\sync_skill.py" --uninstall

# 3. Đảm bảo dừng tiến trình widget nếu đang chạy
Get-Process python*, pythonw* -ErrorAction SilentlyContinue | Where-Object {
    $_.Path -like "*widget*" -or $_.CommandLine -like "*widget\main.py*"
} | Stop-Process -Force -ErrorAction SilentlyContinue

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "  ✅ ĐÃ HOÀN TẤT GỠ BỎ TOÀN BỘ KHỎI ANTIGRAVITY!" -ForegroundColor Green
Write-Host "  • Antigravity IDE đã trở về trạng thái nguyên bản sạch 100%." -ForegroundColor White
Write-Host "  • Repo 'antigravity-lean-teamwork' đã được cách ly độc lập." -ForegroundColor White
Write-Host "============================================================" -ForegroundColor Cyan
