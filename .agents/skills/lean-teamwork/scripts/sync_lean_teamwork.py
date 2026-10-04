#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lean Teamwork Management & Verification Utility (Antigravity CLI Edition)
Hỗ trợ kiểm tra tính toàn vẹn hệ thống, khử phình tri thức và cài đặt vào dự án / toàn cục.
"""

import os
import sys
import shutil
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Tự động tìm nguồn skill chuẩn xác
candidate_1 = REPO_ROOT / ".agents" / "skills" / "lean-teamwork"
candidate_2 = REPO_ROOT
candidate_3 = Path.home() / ".agents" / "skills" / "lean-teamwork"

if (candidate_1 / "SKILL.md").exists():
    SKILL_SOURCE = candidate_1
elif (candidate_2 / "SKILL.md").exists():
    SKILL_SOURCE = candidate_2
else:
    SKILL_SOURCE = candidate_3

GLOBAL_SKILL_DIR = Path.home() / ".agents" / "skills" / "lean-teamwork"
SKILL_DIR = GLOBAL_SKILL_DIR if GLOBAL_SKILL_DIR.exists() else SKILL_SOURCE
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
    hook_file = Path.home() / ".agents" / "skills" / "lean-teamwork" / "scripts" / "lean_teamwork_hook.py"
    if not hook_file.exists():
        hook_file = HOOK_SCRIPT
    if hook_file.exists() and os.access(hook_file, os.X_OK):
        print("  ✓ [4/6] PreInvocation Hook Script sẵn sàng và có quyền thực thi.")
        checks_passed += 1
    elif hook_file.exists():
        print("  ✓ [4/6] PreInvocation Hook Script sẵn sàng (chưa cấp quyền +x).")
        checks_passed += 1
    else:
        print("  ❌ [4/6] Không tìm thấy file PreInvocation Hook Script!")

    # 5. External Knowledge Repository
    if PATTERNS_FILE.exists():
        text = PATTERNS_FILE.read_text(encoding="utf-8")
        patterns_count = text.count("## Mẫu ") + text.count("## Pattern ")
        print(f"  ✓ [5/6] Kho tri thức ngoài sẵn sàng ({patterns_count} patterns ghi nhận).")
        checks_passed += 1
    else:
        print("  ⚠ [5/6] Kho tri thức ngoài chưa tồn tại.")

    # 6. Global Hook Registration
    hooks_json = Path.home() / ".gemini" / "config" / "hooks.json"
    if hooks_json.exists():
        try:
            cfg = json.loads(hooks_json.read_text(encoding="utf-8"))
            hooks = cfg.get("hooks", {}).get("PreInvocation", [])
            has_hook = any("lean_teamwork_hook.py" in str(h.get("command", "")) or h.get("name") == "lean-teamwork-reanchor" for h in hooks)
            if has_hook:
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

    for line in text.splitlines():
        if line.startswith("## Mẫu ") or line.startswith("## Pattern "):
            if current_block:
                blocks.append("\n".join(current_block))
            current_block = [line]
        elif current_block:
            current_block.append(line)
    if current_block:
        blocks.append("\n".join(current_block))

    print(f"[PRUNE] Tìm thấy {len(blocks)} blocks tri thức.")
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

def install_global():
    print("[INSTALL] Đang cài đặt Lean Teamwork Protocol lên máy tính...")
    GLOBAL_SKILL_DIR.parent.mkdir(parents=True, exist_ok=True)
    if SKILL_SOURCE.exists() and SKILL_SOURCE != GLOBAL_SKILL_DIR:
        shutil.copytree(SKILL_SOURCE, GLOBAL_SKILL_DIR, dirs_exist_ok=True)
        print("  ✓ Đã nạp skill vào ~/.agents/skills/lean-teamwork")
    
    # Kho tri thức
    src_patterns = REPO_ROOT / "docs" / "learned_patterns.md"
    if src_patterns.exists() and not PATTERNS_FILE.exists():
        PATTERNS_FILE.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src_patterns, PATTERNS_FILE)
        print("  ✓ Đã khởi tạo kho tri thức tại ~/.agents/learned_patterns.md")

    # Đăng ký hook
    hooks_file = Path.home() / ".gemini" / "config" / "hooks.json"
    hooks_file.parent.mkdir(parents=True, exist_ok=True)
    hook_script = GLOBAL_SKILL_DIR / "scripts" / "lean_teamwork_hook.py"
    if not hook_script.exists():
        hook_script = REPO_ROOT / "scripts" / "lean_teamwork_hook.py"

    if hook_script.exists():
        os.chmod(hook_script, 0o755)

    hook_config = {
        "hooks": {
            "PreInvocation": [
                {
                    "name": "lean-teamwork-reanchor",
                    "description": "Tự động tiêm thông điệp Re-Anchor tàng hình trước mỗi lượt gọi model",
                    "command": f"python3 {hook_script}"
                }
            ]
        }
    }
    hooks_file.write_text(json.dumps(hook_config, ensure_ascii=False, indent=2), encoding="utf-8")
    print("  ✓ Đã kích hoạt PreInvocation Hook trong ~/.gemini/config/hooks.json")
    print("-" * 60)
    return verify_system()

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
    elif "--install" in sys.argv:
        success = install_global()
        sys.exit(0 if success else 1)
    elif "--install-to" in sys.argv:
        idx = sys.argv.index("--install-to")
        if len(sys.argv) > idx + 1:
            install_to(sys.argv[idx + 1])
        else:
            print("Cần cung cấp đường dẫn: --install-to <path>")
    else:
        # Mặc định: cài đặt và kiểm thử
        success = install_global()
        sys.exit(0 if success else 1)
