# QUY ƯỚC DỮ LIỆU GIẢ LẬP — Bộ skill AI khối cơ quan hành chính cấp xã

> Bắt buộc áp dụng cho mọi skill trong `gov-skills/skills/`. Mục đích: dữ liệu ví dụ mô phỏng
> phải 100% hư cấu, không trùng tên địa phương/cá nhân có thật, không gắn số liệu thật.

## 1. Địa phương hư cấu

| Loại | Tên mẫu | Ví dụ sử dụng |
|------|---------|---------------|
| Tỉnh | Tỉnh A | "Sở Nội vụ tỉnh A" |
| Xã | Xã A, Xã B | "UBND xã A" |
| Phường | Phường B | "UBND phường B" (dùng khi ví dụ gắn đô thị) |
| Đặc khu | Đặc khu C | Chỉ dùng khi ví dụ gắn hải đảo |

## 2. Đơn vị hư cấu

- "UBND xã A", "HĐND xã A", "Đảng ủy xã A"
- "Văn phòng HĐND và UBND xã A", "Phòng Kinh tế xã A",
  "Phòng Kinh tế, Hạ tầng và Đô thị phường B", "Phòng Văn hóa – Xã hội xã A"
- "Trung tâm Phục vụ hành chính công xã A"
- "Sở Nội vụ tỉnh A", "Sở Nông nghiệp và Môi trường tỉnh A" (khi cần dẫn cấp tỉnh)

## 3. Nhân sự hư cấu

| Vai trò | Tên mẫu |
|---------|---------|
| Chủ tịch UBND xã | Ông Nguyễn Văn A |
| Phó Chủ tịch UBND xã | Bà Trần Thị B |
| Chánh Văn phòng HĐND & UBND | Ông Phạm Văn C |
| Trưởng phòng Kinh tế | Bà Hoàng Thị D |
| Trưởng phòng Văn hóa – Xã hội | Ông Vũ Văn E |
| Công chức (chung) | Bà/Ông + họ tên mẫu (Nguyễn Văn G, Trần Thị H...) |
| Người dân | Ông Nguyễn Văn Dân / Bà Trần Thị Dân |

## 4. Thông tin liên hệ, địa chỉ hư cấu

- Địa chỉ: "Số 123 đường B, xã A, tỉnh A"
- Điện thoại: 0900 000 001 (dãy số 0900 000 0xx)
- Email: @xa-a.gov.vn (vd: vanphong@xa-a.gov.vn) — tên miền hư cấu
- Số hiệu văn bản mẫu: "123/QĐ-UBND", "45/TB-UBND" kèm năm hư cấu phù hợp ngữ cảnh

## 5. Quy tắc bắt buộc trong mục "Ví dụ mô phỏng"

1. Đầu mục ví dụ phải có dòng ghi chú: *"Dữ liệu dưới đây là giả lập 100% phục vụ minh họa."*
2. Không dùng tên tỉnh/xã/phường có thật (Hà Nội, TP.HCM, Đà Nẵng...).
3. Số liệu (ngân sách, diện tích, dân số...) là số tròn, dễ nhận biết giả lập.
4. Output mẫu phải tuân đúng **Cấu trúc output chuẩn** của skill.
5. Không đưa số CCCD, địa chỉ thật, số điện thoại thật của bất kỳ ai.

---

## 6. Quy ước bổ sung cho skill cấp tỉnh

Áp dụng cùng nguyên tắc hư cấu 100% như mục 1–5, với các tên mẫu sau:

| Loại | Tên mẫu | Ví dụ sử dụng |
|------|---------|---------------|
| Tỉnh | Tỉnh A | "UBND tỉnh A", "HĐND tỉnh A" |
| Sở | Sở [tên] tỉnh A | "Sở Tài chính tỉnh A", "Sở Xây dựng tỉnh A" |
| Chi cục | Chi cục [tên] trực thuộc Sở [tên] tỉnh A | "Chi cục Quản lý thị trường tỉnh A" |

Nhân sự hư cấu cấp tỉnh (không trùng tên với tuyến xã):

| Vai trò | Tên mẫu |
|---------|---------|
| Chủ tịch UBND tỉnh | Ông Phạm Văn P |
| Phó Chủ tịch UBND tỉnh | Bà Lê Thị Q |
| Giám đốc Sở | Ông Hoàng Văn S / Bà Vũ Thị T (theo sở) |
| Phó Giám đốc Sở | Ông Đỗ Văn U |
| Chánh Văn phòng Sở | Bà Ngô Thị V |
| Trưởng phòng chuyên môn thuộc Sở | Ông/Bà + tên mẫu (Bùi Văn X, Đặng Thị Y...) |
| Chuyên viên | Ông/Bà + tên mẫu |

- Số hiệu văn bản mẫu cấp tỉnh: "1234/QĐ-UBND", "56/TB-UBND".
- Khi skill cấp tỉnh dẫn ví dụ phối hợp với cấp xã, dùng "UBND xã A" và nhân sự tuyến xã
  theo mục 3 (ông Nguyễn Văn A – Chủ tịch UBND xã A...).

---

## 7. Quy ước bổ sung cho skill cấp trung ương

Áp dụng cùng nguyên tắc hư cấu 100% như mục 1–6. Dùng họ tên **chữ cái kép** để phân biệt
với tuyến xã (chữ đơn A–H) và tuyến tỉnh (chữ đơn P–Y):

| Vai trò | Tên mẫu |
|---------|---------|
| Thủ tướng Chính phủ | Ông Nguyễn Văn AA |
| Phó Thủ tướng Chính phủ | Bà Trần Thị BB |
| Bộ trưởng | Ông Lê Văn CC – Bộ trưởng Bộ [tên] |
| Thứ trưởng | Bà Phạm Thị DD – Thứ trưởng Bộ [tên] |
| Vụ trưởng | Ông Hoàng Văn EE – Vụ trưởng Vụ [tên] |
| Cục trưởng | Bà Vũ Thị FF – Cục trưởng Cục [tên] |
| Chánh Văn phòng Bộ | Ông/Bà + tên mẫu chữ kép |
| Chuyên viên vụ/cục | Ông/Bà + tên mẫu chữ kép |

- Đơn vị: "Chính phủ", "Văn phòng Chính phủ", "Bộ [tên]", "Vụ [tên] – Bộ [tên]", "Cục [tên] – Bộ [tên]".
- Số hiệu văn bản mẫu: quyết định "1234/QĐ-BQP"; thông tư "12/2026/TT-BQP".
- Khi ví dụ cần phối hợp với địa phương: dùng "UBND tỉnh A" + nhân sự tuyến tỉnh (mục 6),
  "UBND xã A" + nhân sự tuyến xã (mục 3).
