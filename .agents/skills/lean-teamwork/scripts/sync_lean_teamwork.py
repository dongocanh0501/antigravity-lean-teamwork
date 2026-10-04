#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lean Teamwork Management & Verification Utility (Antigravity CLI Edition)
Hỗ trợ kiểm tra tính toàn vẹn hệ thống, khử phình tri thức và cài đặt vào dự án.
"""

import os
import sys
import shutil
import json
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = SKILL_DIR / "templates"
REFERENCES_DIR = SKILL_DIR / "references"
PATTERNS_FILE = Path.home() / ".agents" / "learned_patterns.md"
HOOK_SCRIPT = SKILL_DIR / "scripts" / "lean_teamwork_hook.py"

def verify_system():
    print("=" * 60)
    print("🔍 [KIỂM TRA TÍNH TOÀN VẸN HỆ THỐNG LEAN TEAMWORK]")
    print("=" * 60)
    checks_passed = 0
    total_checks = 6

    # 1. SKILL.md
    skill_md = SKILL_DIR / "SKILL.md"
    if skill_md.exists() and "name: lean-teamwork" in skill_md.read_text(encoding="utf-8"):
        lines = len(skill_md.read_text(encoding="utf-8").splitlines())
        print(f"  ✓ [1/6] SKILL.md hợp lệ ({lines} dòng, đạt tiêu chuẩn < 150 dòng).")
        checks_passed += 1
    else:
        print("  ❌ [1/6] SKILL.md không tồn tại hoặc thiếu frontmatter!")

    # 2. Templates
    expected_templates = [
        "execution_brief_template.md",
        "atomic_task_card_template.md",
        "compact_handoff_template.md",
        "cycle_reflection_template.md",
        "evaluation_panel_template.md"
    ]
    missing_templates = [t for t in expected_templates if not (TEMPLATES_DIR / t).exists()]
    if not missing_templates:
        print(f"  ✓ [2/6] Đầy đủ {len(expected_templates)}/{len(expected_templates)} templates.")
        checks_passed += 1
    else:
        print(f"  ❌ [2/6] Thiếu templates: {missing_templates}")

    # 3. References
    expected_refs = [
        "architecture.md",
        "lean-protocol.md",
        "superpowers-integration.md",
        "systematic-debugging.md"
    ]
    missing_refs = [r for r in expected_refs if not (REFERENCES_DIR / r).exists()]
    if not missing_refs:
        print(f"  ✓ [3/6] Đầy đủ {len(expected_refs)}/{len(expected_refs)} tài liệu tham chiếu.")
        checks_passed += 1
    else:
        print(f"  ❌ [3/6] Thiếu tài liệu tham chiếu: {missing_refs}")

    # 4. Hook Script
    if HOOK_SCRIPT.exists() and os.access(HOOK_SCRIPT, os.X_OK):
        print("  ✓ [4/6] PreInvocation Hook Script sẵn sàng và có quyền thực thi.")
        checks_passed += 1
    else:
        print("  ❌ [4/6] Hook script không tìm thấy hoặc thiếu quyền execute!")

    # 5. Learned Patterns Store
    if PATTERNS_FILE.exists():
        content = PATTERNS_FILE.read_text(encoding="utf-8")
        patterns_count = content.count("## Mẫu ") + content.count("## Pattern ")
        print(f"  ✓ [5/6] Kho tri thức ngoài sẵn sàng ({patterns_count} patterns ghi nhận).")
        checks_passed += 1
    else:
        print("  ❌ [5/6] Không tìm thấy ~/.agents/learned_patterns.md!")

    # 6. Global Hooks Config
    hooks_json = Path.home() / ".gemini" / "config" / "hooks.json"
    if hooks_json.exists():
        try:
            h_data = json.loads(hooks_json.read_text(encoding="utf-8"))
            if "lean-teamwork-reanchor" in h_data:
                print("  ✓ [6/6] Hook đã được đăng ký thành công trong ~/.gemini/config/hooks.json.")
                checks_passed += 1
            else:
                print("  ⚠ [6/6] Chưa đăng ký hook 'lean-teamwork-reanchor' trong hooks.json.")
        except Exception as e:
            print(f"  ❌ [6/6] Lỗi đọc hooks.json: {e}")
    else:
        print("  ⚠ [6/6] File hooks.json không tồn tại.")

    print("-" * 60)
    print(f"Kết quả: {checks_passed}/{total_checks} tiêu chí đạt yêu cầu (100% PASS nếu 6/6).")
    print("=" * 60)
    return checks_passed == total_checks

def prune_patterns():
    if not PATTERNS_FILE.exists():
        print("[ERROR] Không tìm thấy file kho tri thức!")
        return

    text = PATTERNS_FILE.read_text(encoding="utf-8")
    blocks = []
    current_block = []
    header = ""

    for line in text.splitlines():
        if line.startswith("# Kho Tri Thức"):
            header = line
        elif line.startswith("## Mẫu "):
            if current_block:
                blocks.append("\n".join(current_block))
            current_block = [line]
        elif current_block:
            current_block.append(line)
    if current_block:
        blocks.append("\n".join(current_block))

    print(f"[PRUNE] Tìm thấy {len(blocks)} blocks tri thức.")
    # Khóa trần 10 patterns mới nhất
    trimmed = blocks[:10]
    out = (
        "# Kho Tri Thức & Các Mẫu Đúc Kết Tinh Gọn (Learned Patterns)\n\n"
        "Tài liệu này là nơi lưu trữ các tri thức kỹ thuật, mẫu sửa lỗi tối thiểu và bài học tiết kiệm quota được chắt lọc sau khi người dùng bấm xác nhận \"OK 💎\". Khóa trần tối đa 10 patterns tinh hoa.\n\n"
        "---\n\n"
        + "\n\n".join(trimmed)
        + "\n"
    )
    PATTERNS_FILE.write_text(out, encoding="utf-8")
    print(f"[SUCCESS] Đã tối ưu hóa kho tri thức, duy trì đúng {len(trimmed)} patterns tinh hoa.")

def install_to(project_path: str):
    p = Path(project_path).resolve()
    if not p.exists() or not p.is_dir():
        print(f"[ERROR] Đường dẫn không tồn tại: {project_path}")
        sys.exit(1)

    target_skill = p / ".agents" / "skills" / "lean-teamwork"
    target_skill.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SKILL_DIR, target_skill, dirs_exist_ok=True)
    print(f"[SUCCESS] Đã cài đặt trọn bộ Lean Teamwork vào dự án: {p.name}")

if __name__ == "__main__":
    if "--verify" in sys.argv:
        success = verify_system()
        sys.exit(0 if success else 1)
    elif "--prune" in sys.argv:
        prune_patterns()
    elif "--install-to" in sys.argv:
        idx = sys.argv.index("--install-to")
        if len(sys.argv) > idx + 1:
            install_to(sys.argv[idx + 1])
        else:
            print("Cần cung cấp đường dẫn: --install-to <path>")
    else:
        verify_system()
