# Bộ Skill AI — Khối cơ quan hành chính nhà nước
**Phiên bản 1.0 — Tháng 10/2026**

Bộ 315 skill AI mô tả quy trình nghiệp vụ của khối cơ quan hành chính nhà nước Việt Nam
từ trung ương đến địa phương, xây dựng theo văn bản pháp luật mới nhất đến tháng 10/2026.

## Quy mô

| Phạm vi | Số lượng |
|---|---|
| Tầng 1 — Skill lõi dùng chung (soạn thảo, họp, báo cáo, tiếp dân, một cửa...) | 26 |
| Cấp xã — X1 Văn phòng, X2 Kinh tế, X3 Văn hóa–Xã hội, X4 PVHCC | 49 |
| Cấp tỉnh — T1–T12 (10 sở, Thanh tra tỉnh, Văn phòng UBND tỉnh) | 106 |
| Cấp trung ương — TW1–TW17 (14 bộ + 3 cơ quan ngang bộ) | 134 |
| **Tổng** | **315** |

## Cấu trúc gói

```
release-v1.0/
├── README.md                  # File này
├── VERSION                    # Phiên bản
├── CHI-MUC-SKILL.md           # Chỉ mục tra cứu 315 skill + bảng cặp song sinh xã↔tỉnh
│                              # + chuỗi liên thông 3 cấp
├── skills/                    # 315 thư mục skill, mỗi thư mục 1 file SKILL.md
│   └── <ma-skill>/SKILL.md
├── docs/                      # Khung kiến trúc, khung từng cấp, kho căn cứ pháp lý,
│                              # quy ước dữ liệu mô phỏng
└── tai-lieu/                  # Tài liệu mô tả chi tiết (Word), danh mục tương tác (HTML),
                               # bảng ưu tiên nghiệp vụ (CSV)
```

## Cách sử dụng

1. **Tra cứu nhanh**: mở `tai-lieu/danh-muc-skill-tuong-tac.html` trên trình duyệt —
   click từng phòng ban để xem các skill tiêu biểu, lọc theo cấp, tìm kiếm theo tên.
2. **Đọc chi tiết**: mở `tai-lieu/Bo_skill_AI_co_quan_hanh_chinh_Mo_ta_chi_tiet.docx`
   (8 phần: tổng quan, kiến trúc, khung pháp lý, danh mục chi tiết 315 skill...).
3. **Dùng từng skill**: mở `skills/<ma-skill>/SKILL.md`. Mỗi skill gồm 10 mục chuẩn:
   frontmatter → Khi nào dùng → Đầu vào → Quy trình (mỗi bước: việc làm, input dùng,
   vai trò + AI hỗ trợ + thời gian, lưu ý nghiệp vụ, kết quả) → sơ đồ luồng →
   Đầu ra + Cấu trúc output chuẩn (thể thức NĐ 30/2020/NĐ-CP) → Checklist →
   Ví dụ mô phỏng → Human gate → Giới hạn → Căn cứ pháp lý.
4. **Ưu tiên triển khai**: xem `tai-lieu/uu-tien-nghiep-vu.csv` — 20 skill ưu tiên 1
   (việc hàng ngày, chưa có phần mềm đáp ứng) nên pilot trước.

## Nguyên tắc cốt lõi

- AI chỉ **hỗ trợ**, không ra quyết định hành chính thay người có thẩm quyền;
  không tự ký, không tự phát hành văn bản.
- Mọi skill có **human gate**: điểm dừng bắt buộc con người kiểm tra/phê duyệt.
- Mọi số liệu, căn cứ pháp lý do con người cung cấp và kiểm chứng.
- Văn bản hành chính tuân thủ thể thức Nghị định 30/2020/NĐ-CP.
- Mọi dữ liệu ví dụ trong skill là **giả lập 100%**, không dùng tên địa phương/cá nhân có thật.

## Cập nhật

Khi có văn bản pháp luật mới, rà soát mục "Căn cứ & lưu ý" của skill liên quan
và cập nhật quy trình. Kho văn bản tham chiếu: `docs/tai-lieu-moi-nhat.md`.

## Liên hệ

Phạm Văn Trường — 0911471191 — truongpv.cesglobal@gmail.com
