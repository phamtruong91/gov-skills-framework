# KHUNG SKILL TỔNG THỂ CẤP TỈNH — Khung mẫu áp dụng chung cho UBND cấp tỉnh Việt Nam

> **Mục đích:** khung mẫu đóng gói skill AI cho khối cơ quan chuyên môn thuộc UBND cấp tỉnh,
> áp dụng được cho mọi tỉnh/thành phố (đối chiếu mã đơn vị với `khung-phong-ban-cap-tinh.md`).
> **Kiến trúc 2 tầng:**
> - **Tầng 1 — Skill lõi dùng chung (20 skill):** 15 skill đã đóng gói ở đợt cấp xã
>   (soạn thảo, họp, báo cáo, tiếp dân, một cửa...) **dùng chung nguyên trạng**, cộng 5 skill
>   lõi đặc thù cấp tỉnh đóng gói mới trong đợt này.
> - **Tầng 2 — Skill nghiệp vụ theo sở (106 skill):** chi tiết từng nghiệp vụ, gắn mã T1–T12.
>   Định vị khác cấp xã: tập trung **tham mưu chính sách, thẩm định, cấp phép (đối với tổ chức),
>   thanh tra, kiểm tra, tổng hợp báo cáo ngành, hướng dẫn nghiệp vụ cho cấp xã**.

**Chuẩn SKILL.md:** áp dụng nguyên chuẩn 10 mục như đợt cấp xã (xem `khung-skill-tong-the.md`):
frontmatter → Khi nào dùng → Input → Quy trình (mỗi bước 5 dòng: Làm gì / Dùng input /
Vai trò nhân sự + AI hỗ trợ + thời gian / Lưu ý nghiệp vụ / → Kết quả bước) → Output +
Cấu trúc output chuẩn (thể thức NĐ 30/2020/NĐ-CP) → Checklist nghiệm thu → Ví dụ mô phỏng
(dữ liệu giả lập 100% theo `quy-uoc-du-lieu-demo.md`, gồm cả mục 6 bổ sung cho cấp tỉnh) →
Human gate → Giới hạn → Căn cứ & lưu ý (chỉ văn bản có thật trong `tai-lieu-moi-nhat.md`).

---

## TẦNG 1 — Skill lõi (15 dùng chung + 5 mới cấp tỉnh)

**15 skill dùng chung** (đã đóng gói đợt cấp xã, dùng nguyên trạng): `soan-cong-van`,
`soan-to-trinh`, `soan-quyet-dinh-hc`, `soan-thong-bao`, `soan-bao-cao`, `soan-bien-ban-hop`,
`soan-ke-hoach-cong-tac`, `phieu-trinh-ky`, `ra-soat-the-thuc-van-ban`, `tiep-cong-dan`,
`phan-loai-xu-ly-don-thu`, `mot-cua-tiep-nhan-hs`, `tong-hop-bao-cao-dinh-ky`,
`chuan-bi-hop-giao-ban`, `so-hoa-luu-tru-ho-so`.

**5 skill lõi mới cấp tỉnh** (đóng gói đợt này):

| Mã | Tên | Mô tả |
|----|-----|-------|
| `tham-dinh-du-thao-qppl` | Thẩm định dự thảo văn bản QPPL | Thẩm định dự thảo VBQPPL của HĐND/UBND tỉnh trước khi trình |
| `danh-gia-tac-dong-cs` | Đánh giá tác động chính sách | Đánh giá tác động khi xây dựng chính sách, văn bản QPPL |
| `soan-de-an-chinh-sach` | Soạn đề án chính sách | Đề án chính sách trình HĐND/UBND tỉnh |
| `thanh-tra-chuyen-nganh` | Thanh tra chuyên ngành (mẫu chung) | Kế hoạch + kết luận thanh tra chuyên ngành |
| `bao-cao-ktxh-tinh` | Báo cáo KT-XH tỉnh định kỳ | Tổng hợp liên sở → báo cáo KT-XH tỉnh |

## TẦNG 2 — Skill nghiệp vụ theo sở (106 skill)

### T1. Sở Nội vụ (15)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `sap-xep-bo-may-tinh` | Tham mưu sắp xếp tổ chức bộ máy, biên chế | TT 10/2025/TT-BNV; TT 06/2026/TT-BNV |
| `tuyen-dung-cong-chuc-tinh` | Tuyển dụng công chức cấp tỉnh | TT 10/2025/TT-BNV |
| `bo-nhiem-dieu-dong-cb` | Bổ nhiệm, điều động cán bộ | TT 10/2025/TT-BNV |
| `danh-gia-cbcc-tinh` | Đánh giá, xếp loại CBCCVC | TT 10/2025/TT-BNV |
| `dao-tao-boi-duong-cbcc` | Kế hoạch đào tạo, bồi dưỡng CBCCVC | TT 10/2025/TT-BNV |
| `thi-dua-khen-thuong-tinh` | Xét thi đua, khen thưởng cấp tỉnh | NĐ 152/2025/NĐ-CP |
| `quan-ly-hoi-quy` | Quản lý hội, quỹ | TT 10/2025/TT-BNV |
| `chinh-sach-tien-luong` | Thực hiện chính sách tiền lương, phụ cấp | TT 10/2025/TT-BNV |
| `thuc-hien-ncc-tinh` | Thực hiện chính sách người có công (cấp tỉnh) | TT 10/2025/TT-BNV |
| `giam-ngheo-tinh` | Chương trình giảm nghèo cấp tỉnh | TT 10/2025/TT-BNV |
| `tro-giup-xh-tinh` | Quản lý trợ giúp xã hội cấp tỉnh | TT 10/2025/TT-BNV; TT 06/2026/TT-BNV |
| `bao-ve-tre-em-tinh` | Bảo vệ trẻ em cấp tỉnh | TT 10/2025/TT-BNV; TT 06/2026/TT-BNV |
| `viec-lam-tinh` | Quản lý nhà nước về việc làm cấp tỉnh | TT 10/2025/TT-BNV; TT 06/2026/TT-BNV |
| `binh-dang-gioi-tinh` | Bình đẳng giới cấp tỉnh | TT 10/2025/TT-BNV; TT 06/2026/TT-BNV |
| `phong-chong-tn-xh-tinh` | Phòng, chống tệ nạn xã hội cấp tỉnh | TT 10/2025/TT-BNV; TT 06/2026/TT-BNV |
| `tro-giup-xh-tinh` | Quản lý trợ giúp xã hội cấp tỉnh | TT 10/2025/TT-BNV; TT 14/2025/TT-BYT |
| `bao-ve-tre-em-tinh` | Bảo vệ trẻ em cấp tỉnh | TT 10/2025/TT-BNV |
| `viec-lam-tinh` | Quản lý nhà nước về việc làm cấp tỉnh | TT 10/2025/TT-BNV |
| `binh-dang-gioi-tinh` | Bình đẳng giới cấp tỉnh | TT 10/2025/TT-BNV |
| `phong-chong-tn-xh-tinh` | Phòng, chống tệ nạn xã hội cấp tỉnh | TT 10/2025/TT-BNV; TT 14/2025/TT-BYT |

### T2. Sở Tư pháp (8)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `xd-vb-qppl-tinh` | Xây dựng văn bản QPPL của HĐND/UBND tỉnh | TT 09/2025/TT-BTP |
| `pbgdpl-tinh` | Phổ biến, giáo dục pháp luật cấp tỉnh | TT 09/2025/TT-BTP |
| `tgpl-tinh` | Quản lý hoạt động trợ giúp pháp lý | TT 09/2025/TT-BTP |
| `quan-ly-bo-tro-tu-phap` | Quản lý công chứng, đấu giá, luật sư | TT 09/2025/TT-BTP |
| `ho-tich-yeu-to-nuoc-ngoai` | Đăng ký hộ tịch có yếu tố nước ngoài | TT 09/2025/TT-BTP |
| `cap-phieu-ly-lich-tu-phap` | Cấp phiếu lý lịch tư pháp | TT 09/2025/TT-BTP |
| `theo-doi-thads` | Theo dõi, phối hợp thi hành án dân sự | TT 09/2025/TT-BTP |
| `qlxphc-tinh` | Quản lý công tác xử lý VPHC | TT 09/2025/TT-BTP |

### T3. Sở Tài chính (10)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `lap-du-toan-ns-tinh` | Lập dự toán ngân sách địa phương | TT 57/2025/TT-BTC |
| `quyet-toan-ns-tinh` | Quyết toán ngân sách địa phương | TT 57/2025/TT-BTC |
| `ke-hoach-dau-tu-cong` | Kế hoạch đầu tư công | TT 57/2025/TT-BTC |
| `tham-dinh-du-an-dau-tu` | Thẩm định dự án đầu tư | TT 57/2025/TT-BTC |
| `dau-thau-mua-sam-cong` | Đấu thầu, mua sắm công | TT 57/2025/TT-BTC |
| `dang-ky-kinh-doanh-tinh` | Đăng ký kinh doanh | TT 57/2025/TT-BTC |
| `ho-tro-dnnvv` | Hỗ trợ DNNVV, kinh tế tập thể | TT 57/2025/TT-BTC |
| `quan-ly-tai-san-cong` | Quản lý tài sản công | TT 57/2025/TT-BTC |
| `tham-dinh-gia-tinh` | Thẩm định giá | TT 57/2025/TT-BTC |
| `thong-ke-tinh` | Công tác thống kê địa phương | TT 57/2025/TT-BTC |

### T4. Sở Công Thương (8)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `quan-ly-cum-cn` | Quản lý cụm công nghiệp | TT 37/2025/TT-BCT |
| `khuyen-cong-tinh` | Chương trình khuyến công | TT 37/2025/TT-BCT |
| `quan-ly-thi-truong-tinh` | Quản lý thị trường (chống buôn lậu, hàng giả) | TT 37/2025/TT-BCT |
| `xuc-tien-thuong-mai` | Xúc tiến thương mại | TT 37/2025/TT-BCT |
| `quan-ly-dien-tinh` | Quản lý an toàn điện, phát triển lưới điện | TT 37/2025/TT-BCT |
| `quan-ly-cho-sieuthi` | Quản lý chợ, siêu thị, trung tâm thương mại | TT 37/2025/TT-BCT |
| `tmdt-bv-ntd` | Thương mại điện tử & bảo vệ người tiêu dùng | TT 37/2025/TT-BCT |
| `attp-cong-thuong-tinh` | ATTP lĩnh vực công thương | TT 37/2025/TT-BCT |

### T5. Sở Nông nghiệp và Môi trường (12)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `quan-ly-de-dieu` | Quản lý đê điều, thủy lợi | TT 19/2025/TT-BNNMT |
| `pctt-tinh` | PCTT-TKCN cấp tỉnh | TT 19/2025/TT-BNNMT |
| `kiem-lam-bao-ve-rung` | Kiểm lâm, bảo vệ rừng | TT 19/2025/TT-BNNMT |
| `quan-ly-thuy-san-tinh` | Quản lý thủy sản, kiểm ngư | TT 19/2025/TT-BNNMT |
| `chan-nuoi-thu-y-tinh` | Chăn nuôi, thú y | TT 19/2025/TT-BNNMT |
| `trong-trot-bvtv-tinh` | Trồng trọt, bảo vệ thực vật | TT 19/2025/TT-BNNMT |
| `ntm-tinh` | Xây dựng nông thôn mới cấp tỉnh | TT 19/2025/TT-BNNMT |
| `giao-dat-to-chuc` | Giao đất, cho thuê đất đối với tổ chức | NĐ 151/2025/NĐ-CP |
| `thu-hoi-dat-bt-tdc` | Thu hồi đất, bồi thường, hỗ trợ, tái định cư | NĐ 151/2025/NĐ-CP |
| `tham-dinh-dtm` | Thẩm định báo cáo đánh giá tác động môi trường | TT 19/2025/TT-BNNMT |
| `cap-phep-khoang-san` | Cấp phép khai thác khoáng sản | TT 19/2025/TT-BNNMT |
| `quan-ly-tnn-tinh` | Quản lý tài nguyên nước | TT 19/2025/TT-BNNMT |

### T6. Sở Xây dựng (10)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `tham-dinh-quy-hoach-xd` | Thẩm định quy hoạch xây dựng, quy hoạch đô thị | TT 10/2025/TT-BXD |
| `cap-phep-xd-cong-trinh` | Cấp phép xây dựng công trình (theo phân cấp) | TT 10/2025/TT-BXD |
| `quan-ly-chat-luong-ct` | Quản lý chất lượng công trình xây dựng | TT 10/2025/TT-BXD |
| `quan-ly-nha-o-tinh` | Quản lý nhà ở, nhà ở xã hội | TT 10/2025/TT-BXD |
| `quan-ly-thi-truong-bds` | Quản lý thị trường bất động sản | TT 10/2025/TT-BXD |
| `ha-tang-ky-thuat-do-thi` | Quản lý hạ tầng kỹ thuật đô thị | TT 10/2025/TT-BXD |
| `quan-ly-van-tai-tinh` | Quản lý vận tải | TT 10/2025/TT-BXD |
| `atgt-tinh` | Bảo đảm an toàn giao thông | TT 10/2025/TT-BXD |
| `quan-ly-dang-kiem` | Quản lý đăng kiểm phương tiện | TT 10/2025/TT-BXD |
| `quan-ly-kch-gt-duong-bo` | Quản lý kết cấu hạ tầng giao thông đường bộ | TT 10/2025/TT-BXD |

### T7. Sở Khoa học và Công nghệ (10)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `quan-ly-nv-khcn-tinh` | Quản lý nhiệm vụ KH&CN cấp tỉnh | TT 10/2025/TT-BKHCN |
| `ho-tro-kn-dmst` | Hỗ trợ khởi nghiệp đổi mới sáng tạo | TT 10/2025/TT-BKHCN |
| `ho-tro-shtt-tinh` | Hỗ trợ đăng ký sở hữu trí tuệ | TT 10/2025/TT-BKHCN |
| `tieu-chuan-do-luong-tinh` | Tiêu chuẩn, đo lường, chất lượng | TT 10/2025/TT-BKHCN |
| `ke-hoach-cds-tinh` | Kế hoạch chuyển đổi số cấp tỉnh | TT 10/2025/TT-BKHCN |
| `dich-vu-cong-truc-tuyen` | Dịch vụ công trực tuyến (chính quyền số) | TT 10/2025/TT-BKHCN |
| `an-toan-thong-tin-tinh` | Bảo đảm an toàn thông tin mạng | TT 10/2025/TT-BKHCN |
| `quan-ly-bao-chi-tinh` | Quản lý báo chí, xuất bản địa phương | TT 10/2025/TT-BKHCN |
| `thong-tin-co-so-tinh` | Thông tin cơ sở, thông tin đối ngoại | TT 10/2025/TT-BKHCN |
| `quan-ly-ha-tang-vt` | Quản lý hạ tầng viễn thông, Internet | TT 10/2025/TT-BKHCN |

### T8. Sở Văn hóa, Thể thao và Du lịch (8)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `quan-ly-di-san-tinh` | Quản lý di sản văn hóa cấp tỉnh | TT 10/2025/TT-BVHTTDL |
| `to-chuc-le-hoi-tinh` | Tổ chức lễ hội cấp tỉnh | TT 10/2025/TT-BVHTTDL |
| `phat-trien-tdtt` | Phát triển thể dục thể thao | TT 10/2025/TT-BVHTTDL |
| `quan-ly-luu-tru-lu-hanh` | Quản lý lữ hành, lưu trú, khu điểm du lịch | TT 10/2025/TT-BVHTTDL |
| `xuc-tien-du-lich-tinh` | Xúc tiến, quảng bá du lịch | TT 10/2025/TT-BVHTTDL |
| `quan-ly-bieu-dien-nt` | Quản lý biểu diễn nghệ thuật | TT 10/2025/TT-BVHTTDL |
| `quan-ly-thu-vien-dien-anh` | Quản lý thư viện, điện ảnh | TT 10/2025/TT-BVHTTDL |
| `quan-ly-quang-cao-tinh` | Quản lý hoạt động quảng cáo | TT 10/2025/TT-BVHTTDL |

### T9. Sở Giáo dục và Đào tạo (8)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `quan-ly-thpt-gdnn` | Quản lý trường THPT, trung tâm GDNN-GDTX | TT 15/2025/TT-BGDĐT |
| `to-chuc-thi-tn-thpt` | Tổ chức kỳ thi tốt nghiệp THPT | TT 15/2025/TT-BGDĐT |
| `tuyen-sinh-dau-cap-tinh` | Chỉ đạo tuyển sinh đầu cấp | TT 15/2025/TT-BGDĐT |
| `kiem-dinh-clgd-tinh` | Kiểm định chất lượng giáo dục | TT 15/2025/TT-BGDĐT |
| `quan-ly-nha-giao-tinh` | Quản lý nhà giáo, CBQL giáo dục | TT 15/2025/TT-BGDĐT |
| `ql-giao-duc-nghe-nghiep` | Quản lý giáo dục nghề nghiệp | TT 15/2025/TT-BGDĐT |
| `pho-cap-gd-tinh` | Phổ cập giáo dục, trường chuẩn quốc gia | TT 15/2025/TT-BGDĐT |
| `chinh-sach-hoc-phi-tinh` | Chính sách học phí, miễn giảm | TT 45/2026/TT-BGDĐT |

### T10. Sở Y tế (8)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `phong-chong-dich-tinh` | Phòng chống dịch bệnh cấp tỉnh | TT 20/2025/TT-BYT |
| `quan-ly-benh-vien-tinh` | Quản lý bệnh viện, cơ sở KCB | TT 20/2025/TT-BYT |
| `cap-phep-hanh-nghe-y` | Cấp phép hành nghề y, giấy phép hoạt động CSYT | TT 20/2025/TT-BYT |
| `quan-ly-duoc-tinh` | Quản lý dược, mỹ phẩm | TT 20/2025/TT-BYT |
| `attp-tinh` | ATTP cấp tỉnh (liên ngành) | TT 20/2025/TT-BYT |
| `dan-so-sks-tinh` | Dân số, sức khỏe sinh sản | TT 20/2025/TT-BYT |
| `yhct-tinh` | Y học cổ truyền | TT 20/2025/TT-BYT |
| `phoi-hop-bhyt` | Phối hợp thực hiện BHYT | TT 20/2025/TT-BYT |

### T11. Thanh tra tỉnh (4)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `ke-hoach-thanh-tra-tinh` | Kế hoạch thanh tra hằng năm | NĐ 141/2025/NĐ-CP |
| `ket-luan-thanh-tra-tinh` | Kết luận thanh tra | NĐ 141/2025/NĐ-CP |
| `tiep-dan-gq-kntc-tinh` | Tiếp dân, tham mưu giải quyết KNTC thuộc thẩm quyền Chủ tịch UBND tỉnh | NĐ 141/2025/NĐ-CP |
| `pctn-ke-khai-ts` | PCTN, kê khai tài sản, thu nhập | NĐ 141/2025/NĐ-CP |

### T12. Văn phòng UBND tỉnh (5)

| Mã | Tên | Căn cứ chính |
|----|-----|--------------|
| `phuc-vu-chi-dao-dh-tinh` | Tham mưu tổng hợp phục vụ chỉ đạo, điều hành | NĐ 150/2025/NĐ-CP |
| `kiem-soat-tthc-tinh` | Kiểm soát thủ tục hành chính cấp tỉnh | NĐ 118/2025/NĐ-CP |
| `van-hanh-tt-pvhcc-tinh` | Vận hành Trung tâm PVHCC tỉnh | NĐ 118/2025/NĐ-CP |
| `quan-tri-cong-ttdt-tinh` | Quản trị Cổng thông tin điện tử tỉnh | NĐ 150/2025/NĐ-CP |
| `le-tan-doi-ngoai-tinh` | Lễ tân, đối ngoại của UBND tỉnh | NĐ 134/2025/NĐ-CP |

---

**Tổng đợt tỉnh: 111 skill mới** (Tầng 1 mới: 5 · T1: 15 · T2: 8 · T3: 10 · T4: 8 · T5: 12 ·
T6: 10 · T7: 10 · T8: 8 · T9: 8 · T10: 8 · T11: 4 · T12: 5).
Cộng 15 skill Tầng 1 dùng chung đợt xã → khung cấp tỉnh bao phủ **126 skill**.
Chi tiết từng skill xem tại `skills/<mã-skill>/SKILL.md`.
