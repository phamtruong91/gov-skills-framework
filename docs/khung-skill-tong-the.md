# KHUNG SKILL TỔNG THỂ — Khung mẫu áp dụng chung cho chính quyền cấp xã Việt Nam

> **Mục đích:** khung mẫu đóng gói skill AI cho khối cơ quan hành chính cấp xã, áp dụng được cho
> mọi xã/phường/đặc khu (đối chiếu mã đơn vị với `khung-phong-ban-cap-xa.md`).
> **Kiến trúc 2 tầng:**
> - **Tầng 1 — Skill lõi dùng chung (15 skill):** năng lực AI xuyên đơn vị: soạn thảo văn bản,
>   họp, báo cáo, tiếp dân, một cửa... Mọi xã đều dùng được ngay.
> - **Tầng 2 — Skill nghiệp vụ theo đơn vị (48 skill):** chi tiết từng nghiệp vụ, gắn mã X1–X4.
>   Khi xã tổ chức khác khung chuẩn (NĐ 370/2025 cho phép xã tự quyết định), tra bảng mapping
>   lĩnh vực → đầu mối trong `khung-phong-ban-cap-xa.md` — không cần đóng gói lại.

---

## Chuẩn cấu trúc file SKILL.md (áp dụng cho mọi skill trong khung)

Mỗi skill = 1 thư mục `skills/<mã-skill>/SKILL.md` gồm 10 mục:

1. **Frontmatter**: `name` (mã skill), `description` (1–2 câu, nêu khi nào dùng)
2. **Khi nào dùng**
3. **Đầu vào (Input)**: bảng Trường | Mô tả | Bắt buộc
4. **Quy trình**: các bước chi tiết để thực hiện nghiệp vụ — mỗi bước gồm:
   - **Làm gì**: thao tác cụ thể, không chung chung;
   - **Dùng input**: trường dữ liệu nào của Input được dùng ở bước này;
   - **Vai trò**: nhân sự thực hiện bước này (chức danh/đơn vị cụ thể: công chức, trưởng phòng,
     chủ tịch UBND xã...) + cách AI hỗ trợ bước đó — kèm thời gian ước tính;
   - **Lưu ý nghiệp vụ**: quy tắc, điểm kiểm tra;
   - **→ Kết quả bước**: bán thành phẩm cụ thể của bước đó.
5. **Đầu ra (Output)**: danh sách sản phẩm + **Cấu trúc output chuẩn** (khung mẫu cố định
   của sản phẩm chính: các phần bắt buộc theo đúng thứ tự, đúng thể thức văn bản hành chính
   theo NĐ 30/2020/NĐ-CP về công tác văn thư)
6. **Checklist nghiệm thu**: bộ tiêu chí đánh giá output đạt/không đạt (đủ phần theo cấu trúc
   chuẩn, số liệu khớp input, không bịa dữ liệu, đúng thể thức, đã qua human gate)
7. **Ví dụ mô phỏng**: Input mẫu + Output mẫu bằng **dữ liệu giả lập 100%** theo
   `quy-uoc-du-lieu-demo.md` (ghi chú rõ giả lập) — Output mẫu phải tuân đúng
   **Cấu trúc output chuẩn** ở mục 5
8. **Human gate (người kiểm duyệt)**: ai phải duyệt ở bước nào trước khi output được dùng/phát hành
   (vd: công chức soạn → Trưởng phòng kiểm tra → Chủ tịch UBND xã ký duyệt)
9. **Giới hạn (guardrails)**: những việc AI tuyệt đối KHÔNG được làm (không ra quyết định hành chính
   thay người có thẩm quyền, không tự ký/phát hành văn bản, không bịa số liệu/căn cứ pháp lý,
   không tư vấn vượt thẩm quyền, không dùng văn bản hết hiệu lực)
10. **Căn cứ & lưu ý**: văn bản pháp lý liên quan — CHỈ trích dẫn văn bản có thật trong
    `tai-lieu-moi-nhat.md` (NĐ 150/2025, NĐ 370/2025, chuỗi NĐ 120–152/2025, các thông tư bộ ngành,
    NĐ 30/2020/NĐ-CP về thể thức văn bản...). Tuyệt đối không bịa số hiệu văn bản.

> Mô hình thực thi của mọi skill: **Input → từng bước quy trình (mỗi bước cho ra bán thành phẩm)
> → Output theo khung chuẩn**. Có input đầy đủ và làm đúng các bước thì cho ra output chuẩn —
> đúng như một quy trình nghiệp vụ thực tế tại cấp xã.

---

## TẦNG 1 — Skill lõi dùng chung (15 skill)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `soan-cong-van` | Soạn công văn | Công văn hành chính đúng thể thức NĐ 30/2020 |
| `soan-to-trinh` | Soạn tờ trình | Tờ trình xin chủ trương/phê duyệt của cấp trên |
| `soan-quyet-dinh-hc` | Soạn quyết định hành chính | Quyết định cá biệt (khen thưởng, xử phạt, bổ nhiệm...) |
| `soan-thong-bao` | Soạn thông báo | Thông báo kết luận, lịch, kết quả giải quyết |
| `soan-bao-cao` | Soạn báo cáo | Báo cáo định kỳ, đột xuất, chuyên đề |
| `soan-bien-ban-hop` | Soạn biên bản họp | Biên bản giao ban, họp chuyên đề, hội nghị |
| `soan-ke-hoach-cong-tac` | Lập kế hoạch công tác | Kế hoạch tuần/tháng/quý/năm của đơn vị |
| `phieu-trinh-ky` | Phiếu trình ký duyệt | Phiếu trình lãnh đạo ký văn bản |
| `ra-soat-the-thuc-van-ban` | Rà soát thể thức văn bản | Kiểm tra thể thức NĐ 30/2020 → bảng lỗi + bản sạch |
| `tiep-cong-dan` | Tổ chức tiếp công dân | Lịch tiếp định kỳ/đột xuất, biên bản tiếp dân |
| `phan-loai-xu-ly-don-thu` | Phân loại, xử lý đơn thư | Đơn khiếu nại/tố cáo/kiến nghị → phân loại, chuyển xử lý, theo dõi hạn |
| `mot-cua-tiep-nhan-hs` | Tiếp nhận hồ sơ một cửa | Kiểm tra tính đầy đủ, hợp lệ; giấy hẹn trả kết quả |
| `tong-hop-bao-cao-dinh-ky` | Tổng hợp báo cáo định kỳ | Gộp báo cáo các phòng/ban theo mẫu, gap log số liệu thiếu |
| `chuan-bi-hop-giao-ban` | Chuẩn bị họp & theo dõi việc | Tài liệu họp, trích kết luận, giao việc theo đầu mối/hạn |
| `so-hoa-luu-tru-ho-so` | Số hóa, lưu trữ hồ sơ | Quy trình số hóa, đặt tên, lưu trữ, tra cứu hồ sơ điện tử |

## TẦNG 2 — Skill nghiệp vụ theo đơn vị (49 skill)

### X1. Văn phòng HĐND và UBND (15)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `dang-ky-khai-sinh` | Đăng ký khai sinh | TT 09/2025/TT-BTP; Luật Hộ tịch |
| `dang-ky-khai-tu` | Đăng ký khai tử | TT 09/2025/TT-BTP; Luật Hộ tịch |
| `dang-ky-ket-hon` | Đăng ký kết hôn | TT 09/2025/TT-BTP; Luật Hộ tịch |
| `chung-thuc-ban-sao` | Chứng thực bản sao, chữ ký | TT 09/2025/TT-BTP |
| `quan-ly-ho-tich-dien-tu` | Quản lý sổ hộ tịch, CSDL hộ tịch điện tử | TT 09/2025/TT-BTP |
| `pho-bien-giao-duc-phap-luat` | Phổ biến, giáo dục pháp luật | TT 09/2025/TT-BTP |
| `hoa-giai-co-so` | Hòa giải ở cơ sở | Luật Hòa giải ở cơ sở; TT 09/2025/TT-BTP |
| `ho-tro-tiep-can-tgpl` | Hỗ trợ tiếp cận trợ giúp pháp lý | TT 09/2025/TT-BTP |
| `theo-doi-thi-hanh-phap-luat` | Theo dõi tình hình thi hành pháp luật | TT 09/2025/TT-BTP |
| `tu-kiem-tra-van-ban` | Tự kiểm tra văn bản QPPL do cấp xã ban hành | TT 09/2025/TT-BTP |
| `chuan-bi-ky-hop-hdnd` | Chuẩn bị kỳ họp HĐND xã | Luật Tổ chức CQĐP 72/2025/QH15 |
| `thi-dua-khen-thuong-xa` | Xét thi đua, khen thưởng cấp xã | NĐ 152/2025/NĐ-CP |
| `cai-cach-hanh-chinh-xa` | Kế hoạch & báo cáo CCHC cấp xã | TT 06/2026/TT-BNV |
| `quan-ly-cbcc-xa` | Quản lý, đào tạo bồi dưỡng CBCC cấp xã | TT 10/2025/TT-BNV; TT 06/2026/TT-BNV |
| `doi-ngoai-xa` | Công tác đối ngoại cấp xã (đón tiếp đoàn khách, lễ tân) | NĐ 134/2025/NĐ-CP; NĐ 150/2025/NĐ-CP |

### X2. Phòng Kinh tế (14)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `lap-du-toan-ns-xa` | Lập dự toán ngân sách xã hằng năm | TT 57/2025/TT-BTC |
| `quyet-toan-ns-xa` | Quyết toán ngân sách xã | TT 57/2025/TT-BTC |
| `ke-hoach-ktxh-xa` | Kế hoạch phát triển KT-XH xã hằng năm | TT 57/2025/TT-BTC |
| `cap-gcn-qsd-dat` | Cấp Giấy chứng nhận QSD đất lần đầu (Chủ tịch UBND xã ký) | NĐ 151/2025/NĐ-CP |
| `xac-nhan-nguon-goc-dat` | Xác nhận nguồn gốc, hiện trạng sử dụng đất | NĐ 151/2025/NĐ-CP; TT 19/2025/TT-BNNMT |
| `giao-dat-chuyen-muc-dich` | Giao đất, cho thuê đất, chuyển mục đích SD đất (cá nhân/hộ gia đình) | NĐ 151/2025/NĐ-CP |
| `hoa-giai-tranh-chap-dat` | Hòa giải tranh chấp đất đai ở cơ sở | NĐ 151/2025/NĐ-CP |
| `quan-ly-trat-tu-xay-dung` | Quản lý trật tự xây dựng, xử lý vi phạm | TT 10/2025/TT-BXD |
| `cap-phep-xay-dung-nha-o` | Cấp phép xây dựng nhà ở riêng lẻ (theo phân cấp) | TT 10/2025/TT-BXD |
| `quan-ly-cho` | Quản lý chợ, điểm kinh doanh trên địa bàn | TT 37/2025/TT-BCT |
| `phuong-an-pctt` | Phương án PCTT-TKCN cấp xã | TT 19/2025/TT-BNNMT |
| `nong-thon-moi` | Duy trì, nâng chất tiêu chí nông thôn mới | TT 19/2025/TT-BNNMT |
| `bvmt-co-so` | Bảo vệ môi trường cơ sở | TT 19/2025/TT-BNNMT |
| `quan-ly-thuy-loi-nho` | Quản lý công trình thủy lợi nhỏ, đê bao nội đồng | TT 19/2025/TT-BNNMT |

### X3. Phòng Văn hóa – Xã hội (16)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `quan-ly-truong-hoc` | Quản lý nhà nước về trường MN, TH, THCS trên địa bàn | TT 15/2025/TT-BGDĐT; TT 45/2026/TT-BGDĐT |
| `pho-cap-giao-duc` | Phổ cập giáo dục, xóa mù chữ | TT 15/2025/TT-BGDĐT |
| `quan-ly-di-tich-le-hoi` | Quản lý di tích, lễ hội | TT 10/2025/TT-BVHTTDL |
| `hoat-dong-vh-the-thao` | Tổ chức hoạt động văn hóa, thể thao cơ sở | TT 10/2025/TT-BVHTTDL |
| `truyen-thanh-co-so` | Quản lý đài truyền thanh cơ sở | TT 10/2025/TT-BVHTTDL |
| `to-cong-nghe-so-cd` | Tổ công nghệ số cộng đồng | TT 10/2025/TT-BKHCN |
| `y-te-du-phong-coso` | Y tế dự phòng cơ sở (tiêm chủng, phòng dịch) | TT 20/2025/TT-BYT |
| `attp-co-so` | Bảo đảm ATTP cơ sở | TT 20/2025/TT-BYT |
| `chinh-sach-ncc` | Thực hiện chính sách người có công | TT 10/2025/TT-BNV |
| `tro-giup-xa-hoi` | Xét hưởng trợ giúp xã hội | TT 20/2025/TT-BYT (TT 14); TT 10/2025/TT-BNV |
| `giam-ngheo` | Rà soát hộ nghèo/cận nghèo, chương trình giảm nghèo | TT 10/2025/TT-BNV |
| `bao-ve-tre-em` | Bảo vệ, chăm sóc trẻ em cơ sở | TT 10/2025/TT-BNV |
| `quan-ly-ton-giao-coso` | Quản lý tín ngưỡng, tôn giáo ở cơ sở | TT 02/2025/TT-BDTTG |
| `ho-tro-viec-lam` | Tư vấn, giới thiệu việc làm | TT 10/2025/TT-BNV |
| `binh-dang-gioi` | Công tác bình đẳng giới, vì sự tiến bộ phụ nữ | TT 10/2025/TT-BNV |
| `phong-chong-te-nan` | Phòng, chống tệ nạn xã hội cơ sở | TT 20/2025/TT-BYT (TT 14) |

### X4. Trung tâm Phục vụ hành chính công (4)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `van-hanh-mot-cua` | Vận hành bộ phận một cửa, phối hợp liên thông | NĐ 118/2025/NĐ-CP; VB 7216/VPCP-KSTT |
| `danh-gia-hai-long-tthc` | Khảo sát mức độ hài lòng giải quyết TTHC | NĐ 118/2025/NĐ-CP |
| `bao-cao-kiem-soat-tthc` | Báo cáo kiểm soát TTHC, thống kê hồ sơ trễ hạn | NĐ 118/2025/NĐ-CP |
| `niem-yet-cong-khai-tthc` | Niêm yết, công khai TTHC | NĐ 118/2025/NĐ-CP |

---

**Tổng: 64 skill** (Tầng 1: 15 · X1: 15 · X2: 14 · X3: 16 · X4: 4).
Chi tiết từng skill xem tại `skills/<mã-skill>/SKILL.md` và chỉ mục `skills/README.md`.
