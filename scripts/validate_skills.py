#!/usr/bin/env python3
"""Kiểm tra cấu trúc các skill trong bộ gov-skills-framework.

Kiểm tra: frontmatter (name khớp thư mục, có description), tiêu đề,
đủ mục chuẩn, bảng đầu vào (tên trường snake_case, cột Bắt buộc Có/Không),
đánh số bước quy trình, đủ 6 thành phần mỗi bước (chấp nhận nhãn in đậm),
ký hiệu thời gian ⏱, sơ đồ mermaid khớp số bước, mục Đầu ra có
"Cấu trúc output chuẩn", input bắt buộc được bước quy trình sử dụng.

Checklist NĐ 30/2020 chỉ là CẢNH BÁO (không phải lỗi): chỉ các output là
văn bản hành chính mới cần checklist thể thức; biểu mẫu chuyên ngành dùng
chuẩn riêng của ngành (xem docs/QUY-CACH-DAU-RA.md).

Chạy từ thư mục gốc của repository:
    python3 scripts/validate_skills.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")

REQUIRED_SECTIONS = [
    "Khi nào dùng", "Đầu vào (Input)", "Quy trình", "Đầu ra (Output)",
    "Checklist", "Ví dụ mô phỏng", "Human gate", "Giới hạn", "Căn cứ",
    "Luồng quy trình",
]

# chấp nhận cả "- Làm gì:" và "- **Làm gì**:"
STEP_PARTS = [
    ("làm gì", r"^-\s*(\*\*)?Làm gì(\*\*)?:"),
    ("dùng input", r"^-\s*(\*\*)?Dùng input(\*\*)?:"),
    ("AI hỗ trợ", r"AI"),
    ("thời gian ⏱", r"⏱"),
    ("lưu ý", r"^-\s*(\*\*)?Lưu ý(\*\*)?"),
    ("kết quả bước", r"→ Kết quả"),
]


def check_skill(code):
    errors, warnings = [], []
    path = os.path.join(SKILLS_DIR, code, "SKILL.md")
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        return [f"không đọc được file: {e}"], []

    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append("thiếu frontmatter")
    else:
        fm = m.group(1)
        nm = re.search(r"^name:\s*(\S+)", fm, re.M)
        if not nm or nm.group(1).strip() != code:
            errors.append("frontmatter name không khớp thư mục")
        if not re.search(r"^description:", fm, re.M):
            errors.append("thiếu description")
    if "# Skill:" not in text[:600]:
        errors.append("thiếu tiêu đề '# Skill:'")

    for sec in REQUIRED_SECTIONS:
        if sec not in text:
            errors.append(f"thiếu mục '{sec}'")

    input_fields = {}
    mi = re.search(r"##\s*\d*\.?\s*Đầu vào \(Input\)(.*?)(?=\n## |\Z)", text, re.S)
    if mi:
        for m in re.finditer(r"^\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$",
                             mi.group(1), re.M):
            f, desc, req = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
            if not f or "---" in f:
                continue
            if f in input_fields:
                errors.append(f"trùng trường input '{f}'")
            input_fields[f] = req
            if not re.match(r"^[a-z0-9_]+$", f):
                errors.append(f"tên trường input '{f}' không đúng snake_case")
            if not desc:
                errors.append(f"trường '{f}' thiếu mô tả")
            if req not in ("Có", "Không"):
                errors.append(f"cột Bắt buộc của '{f}' phải là Có/Không (đang: '{req}')")
        if not input_fields:
            errors.append("bảng đầu vào không có trường nào")

    mp = re.search(r"##\s*\d*\.?\s*Quy trình(.*?)(?=\n## |\Z)", text, re.S)
    step_count = 0
    if mp:
        nums = [int(x) for x in re.findall(r"\*\*Bước (\d+)\.", mp.group(1))]
        step_count = len(nums)
        if nums != list(range(1, len(nums) + 1)):
            errors.append(f"đánh số bước sai: {nums}")
        for i, s in enumerate(re.split(r"\*\*Bước \d+\.", mp.group(1))[1:], 1):
            missing = [name for name, pat in STEP_PARTS
                       if not re.search(pat, s, re.M)]
            if missing:
                errors.append(f"Bước {i} thiếu: {', '.join(missing)}")

    mm = re.search(r"```mermaid(.*?)```", text, re.S)
    if not mm:
        errors.append("thiếu sơ đồ mermaid")
    elif step_count:
        nodes = {int(x) for x in re.findall(r"\bB(\d+)\b", mm.group(1))}
        if nodes and nodes != set(range(1, step_count + 1)):
            errors.append(f"mermaid không khớp số bước: {sorted(nodes)}")

    mo = re.search(r"##\s*\d*\.?\s*Đầu ra \(Output\)(.*?)(?=\n## |\Z)", text, re.S)
    if mo:
        sec = mo.group(1)
        if "Cấu trúc output chuẩn" not in sec:
            errors.append("thiếu 'Cấu trúc output chuẩn'")
        if ("Checklist thể thức văn bản theo NĐ 30" not in sec
                and "Chuẩn tài liệu đầu ra" not in sec):
            warnings.append("không có block checklist NĐ 30/phân tầng "
                            "(chỉ cần nếu output là văn bản hành chính)")

    if mi and mp:
        used = set()
        for um in re.finditer(r"- Dùng input:\s*(.*?)(?:\n|$)", mp.group(1)):
            used.update(f.strip() for f in re.findall(r"`([^`]+)`", um.group(1)))
        body = text[:mi.start()] + text[mi.end():]
        for f, req in input_fields.items():
            if req == "Có" and f not in used and f"`{f}`" not in body:
                errors.append(f"trường bắt buộc '{f}' không được bước nào sử dụng")

    return errors, warnings


def main():
    if not os.path.isdir(SKILLS_DIR):
        print("Không tìm thấy thư mục skills/", file=sys.stderr)
        sys.exit(2)
    codes = sorted(d for d in os.listdir(SKILLS_DIR)
                   if os.path.isfile(os.path.join(SKILLS_DIR, d, "SKILL.md")))
    bad, warn_count = 0, 0
    for code in codes:
        errors, warnings = check_skill(code)
        warn_count += len(warnings)
        if errors:
            bad += 1
            print(f"[{code}]")
            for e in errors:
                print(f"  LỖI: {e}")
    print(f"\nKiểm tra {len(codes)} skill: {bad} skill có lỗi, {warn_count} cảnh báo.")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
