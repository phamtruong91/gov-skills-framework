# Nhật ký thay đổi

## v1.0.1 — 10/10/2026 — Rà soát chi tiết input/quy trình/output

Đợt rà soát chi tiết toàn bộ 315 skill theo yêu cầu: kiểm tra tự động 100% + rà soát ngữ nghĩa mẫu 86 skill (26 Tầng 1, 60 mẫu 3 cấp).

### Sửa lỗi kỹ thuật (kiểm tra tự động 315/315)
- Chuẩn hóa 39 trường input: cột "Bắt buộc" chỉ còn Có/Không (điều kiện chuyển vào mô tả).
- Chuẩn hóa ký hiệu thời gian ⏱ cho 611 bước (trước đây ghi bằng văn xuôi).
- Chuẩn hóa 45 tên trường input về snake_case (đồng bộ cả bảng input và tham chiếu trong quy trình).
- Gắn 58 trường bắt buộc bị bỏ quên (người ký, đơn vị chủ trì, thời hạn...) vào đúng bước sử dụng.
- Sửa định dạng: tách dòng "- Vai trò", gộp mảnh ⏱ rời, xóa dấu câu thừa, đánh số section 5–10 còn thiếu (19 skill).

### Sửa lỗi ngữ nghĩa (rà soát mẫu 86 skill)
- Mâu thuẫn thẩm quyền: Tờ trình Chính phủ về nghị định do Bộ trưởng ký (không phải Thứ trưởng); chương trình PCTP do Thứ trưởng phê duyệt; kiểm tra văn bản QPPL áp Luật Ban hành VBQPPL (không áp NĐ 30).
- Luồng logic: tách bước lấy ý kiến giải trình trong thanh tra chuyên ngành; đưa lấy ý kiến/thẩm định lên trước áp thể thức (soan-to-trinh, soan-quyet-dinh-hc); nhánh đột xuất, nhánh hồ sơ chưa đạt quay lại B1.
- Truy nguyên input/output: bổ sung phiếu trình ký, giấy mời họp, sổ theo dõi đơn thư, trường input còn thiếu (`bien_ban_hop`, `yeu_cau_tra_cuu`, `so_lieu_don_vi`...).
- Ghi chú thích ứng đa cấp cho 20 skill Tầng 1; ghi chú "chỉ áp dụng cấp trung ương" cho 6 skill tw-*.
- Kết quả kiểm tra tự động sau sửa: 1.728 trường input, 1.541 bước quy trình, 0 lỗi.

## v1.0 — 10/10/2026

Phiên bản phát hành đầu tiên: bộ 315 skill AI khối cơ quan hành chính nhà nước.

### Thêm mới
- 315 skill (Tầng 1: 26 · Cấp xã: 49 · Cấp tỉnh: 106 · Cấp trung ương: 134), bao phủ 34 đơn vị từ trung ương đến địa phương.
- Chuẩn cấu trúc 10 mục cho mọi skill: frontmatter, khi nào dùng, đầu vào, quy trình, sơ đồ luồng, đầu ra, checklist, ví dụ mô phỏng, human gate, giới hạn, căn cứ pháp lý.
- Chỉ mục tra cứu thống nhất: 29 cặp nghiệp vụ song sinh xã↔tỉnh, 11 chuỗi liên thông 3 cấp.
- Tài liệu kèm theo: Word mô tả chi tiết, HTML tra cứu tương tác, CSV bảng ưu tiên nghiệp vụ.
- Checklist chuẩn tài liệu đầu ra trong mục "Đầu ra" của skill:
  - 140 skill văn bản hành chính thông thường: 9 thành phần thể thức NĐ 30/2020/NĐ-CP.
  - 56 skill biểu mẫu chuyên ngành và khối BQP/BCA: checklist phân tầng (chuẩn riêng ngành/cơ quan ưu tiên, NĐ 30/2020 cho phần không có quy chuẩn riêng).
  - Skill xây dựng VBQPPL tuân theo Luật Ban hành văn bản QPPL, không áp NĐ 30.
- `docs/QUY-CACH-DAU-RA.md`: quy cách chuẩn tài liệu đầu ra.
- `scripts/validate_skills.py`: công cụ kiểm tra cấu trúc skill.

### Lưu ý
- Một số căn cứ pháp lý mới (NĐ 303/2025/NĐ-CP, NĐ 25/2025/NĐ-CP...) còn điểm chưa kiểm chứng chắc chắn về ngày ban hành — cần rà soát lại trước khi dùng làm căn cứ tư vấn pháp lý chính thức.
- Các đơn vị đặc thù cấp tỉnh (Sở Ngoại vụ, Sở Dân tộc và Tôn giáo, Ban Quản lý KCN/KKT...) chưa nằm trong phạm vi phiên bản này.
