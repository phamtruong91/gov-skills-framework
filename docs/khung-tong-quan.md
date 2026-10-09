# KHUNG TỔNG QUAN — Bộ Skill AI khối cơ quan hành chính (3 cấp: xã + tỉnh + trung ương)

> Chỉ mục chi tiết: `skills/README.md` · Khung xã: `khung-skill-tong-the.md` ·
> Khung tỉnh: `khung-skill-tong-the-tinh.md` · Khung trung ương: `khung-skill-tong-the-trung-uong.md` ·
> Đơn vị xã: `khung-phong-ban-cap-xa.md` · Đơn vị tỉnh: `khung-phong-ban-cap-tinh.md` ·
> Đơn vị trung ương: `khung-bo-nganh-trung-uong.md` · Dữ liệu giả lập: `quy-uoc-du-lieu-demo.md` ·
> Căn cứ pháp lý: `tai-lieu-moi-nhat.md`

## 1. Kiến trúc: chỉ mục chung, nội dung tách theo cấp

```
TẦNG 1 — Skill lõi dùng chung (26 skill)
  15 skill gốc (soạn thảo, họp, báo cáo, tiếp dân, một cửa, số hóa...)
  + 5 skill đặc thù cấp tỉnh (thẩm định QPPL, đánh giá tác động CS, đề án, TT chuyên ngành, BC KT-XH)
  + 6 skill đặc thù trung ương (xây dựng luật/nghị định/thông tư, chiến lược ngành, BC Chính phủ, đánh giá CS)
        │
        ├── TẦNG 2 — Cấp xã (49 skill): X1 Văn phòng HĐND&UBND · X2 Phòng Kinh tế ·
        │                              X3 Phòng VH-XH · X4 Trung tâm PVHCC
        │   Định vị: giải quyết việc trực tiếp cho dân (hộ tịch, sổ đỏ hộ gia đình,
        │   hòa giải cơ sở, trường MN/TH/THCS, một cửa xã...)
        │
        ├── TẦNG 2 — Cấp tỉnh (106 skill): T1–T12 (12 sở/ngành + Thanh tra + VP UBND)
        │   Định vị: tham mưu chính sách, thẩm định, cấp phép đối với tổ chức,
        │   thanh tra, tổng hợp báo cáo ngành, hướng dẫn nghiệp vụ cho cấp xã
        │
        └── TẦNG 2 — Cấp trung ương (134 skill): TW1–TW17 (14 Bộ + 3 cơ quan ngang Bộ)
            Định vị: xây dựng thể chế; quản lý vĩ mô ngành; cấp phép cấp quốc gia;
            thanh tra toàn quốc; tổng hợp, dự báo, báo cáo Chính phủ; đối ngoại ngành;
            hướng dẫn nghiệp vụ cho địa phương
```

**Nguyên tắc đã chốt:**
- Không gộp nội dung skill đa cấp: khác thẩm quyền ký, đối tượng áp dụng, căn cứ pháp lý.
- Tra cứu liên thông qua **bảng cặp song sinh** (xã↔tỉnh) và **chuỗi liên thông 3 cấp**
  trong `skills/README.md`.
- Dữ liệu ví dụ mô phỏng 100% hư cấu theo `quy-uoc-du-lieu-demo.md` (xã: Xã A, ông Nguyễn Văn A...;
  tỉnh: Tỉnh A, ông Phạm Văn P...; trung ương: tên chữ kép AA–FF).
- AI chỉ hỗ trợ; không ra quyết định hành chính thay người có thẩm quyền, không tự ký/phát hành,
  không bịa số liệu/căn cứ pháp lý; văn bản theo thể thức NĐ 30/2020/NĐ-CP.
- BQP/BCA: chỉ nghiệp vụ hành chính, chính sách công khai; không nội dung mật/tác chiến.

## 2. Quy mô hiện tại

| Phạm vi | Skill | Ghi chú |
|---------|-------|---------|
| Tầng 1 dùng chung | 26 | 15 gốc + 5 mới đợt tỉnh + 6 mới đợt trung ương |
| Cấp xã | 49 | X1: 15 · X2: 14 · X3: 16 · X4: 4 |
| Cấp tỉnh | 106 | T1: 15 · T2: 8 · T3: 10 · T4: 8 · T5: 12 · T6: 10 · T7: 10 · T8: 8 · T9: 8 · T10: 8 · T11: 4 · T12: 5 |
| Cấp trung ương | 134 | TW1–TW5: 8 mỗi bộ · TW6: 10 · TW7: 8 · TW8: 10 · TW9: 8 · TW10: 8 · TW11: 10 · TW12: 8 · TW13: 8 · TW14–TW17: 6 mỗi đơn vị |
| **Tổng** | **315** | Chi tiết tại `skills/README.md` |

## 3. Mở rộng trong tương lai

- **Đơn vị đặc thù cấp tỉnh** (ĐB1–ĐB5: Sở Ngoại vụ, Sở Dân tộc và Tôn giáo, Sở Du lịch,
  Sở Quy hoạch – Kiến trúc, Sở An toàn thực phẩm): đóng gói bổ sung theo nhu cầu từng địa phương,
  ghép vào Tầng 2 cấp tỉnh mà không sửa khung.
- **Cơ quan thuộc Chính phủ, đơn vị sự nghiệp công lập trực thuộc bộ**: áp dụng cùng kiến trúc —
  Tầng 1 dùng chung nguyên trạng, Tầng 2 theo chức năng đơn vị.
