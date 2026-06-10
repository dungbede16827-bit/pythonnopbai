# IndexError: tuple index out of range
# Dữ liệu của Levi
# ("Levi", 120, 2500)

# Tuple này có 3 phần tử:

# Index	Giá trị
# 0	"Levi"
# 1	120
# 2	2500

# Khi chương trình thực hiện:

# r = p[2]

# Python lấy được giá trị:

# 2500

# nên không có lỗi.

# Dữ liệu của SofM
# ("SofM", 150)

# Tuple này chỉ có 2 phần tử:

# Index	Giá trị
# 0	"SofM"
# 1	150

# Nhưng chương trình vẫn cố truy cập:

# r = p[2]

# Trong khi index 2 không tồn tại.

# Do đó Python phát sinh:

# IndexError: tuple index out of range

# Ý nghĩa:

# Đang truy cập vào vị trí nằm ngoài phạm vi của Tuple.

# Giả sử:

# ("SofM", 150, 2800)

# thì Levi và SofM đều chạy được.

# Khi đến Optimus:

# ("Optimus", 100, "N/A")

# Chương trình thực hiện:

# b = (m * 10) + (int(r) * 0.5)

# Tức là:

# int("N/A")

# Python chỉ có thể chuyển chuỗi chứa số sang kiểu int.

# Ví dụ:

# int("2500")

# hợp lệ.

# Nhưng:

# int("N/A")

# không thể chuyển đổi được.

# Do đó lỗi xuất hiện tại dòng:

# b = (m * 10) + (int(r) * 0.5)

# Exception được in ra:

# ValueError: invalid literal for int() with base 10: 'N/A'

# Tên lỗi là:

# ValueError
# Nếu thêm:

# print("Đang xử lý:", p)

# ngay sau:

# for p in ds:

# thì chương trình sẽ hiển thị bản ghi hiện tại đang được xử lý.

# Ví dụ:

# --- BẢNG TÍNH THƯỞNG RP ---
# Đang xử lý: ('Levi', 120, 2500)
# Tuyển thủ Levi nhận được 2450.0 RP

# Đang xử lý: ('SofM', 150)

# Sau đó chương trình sập.

# Nhìn vào kết quả ta biết ngay:

# Levi xử lý thành công
# SofM là bản ghi cuối cùng được in ra
# Lỗi xảy ra trong lúc xử lý SofM

# Đây là kỹ thuật Debug cơ bản bằng print() giúp nhanh chóng xác định:

# Dữ liệu nào gây lỗi
# Vòng lặp nào gây lỗi
# Chương trình đang chạy đến đâu trước khi crash

# Code cũ
# def process(ds):
#     for p in ds:
#         t = p[0]
#         m = p[1]
#         r = p[2]
#         b = ...

# Các tên biến quá ngắn và không diễn tả ý nghĩa.

# Biến cũ	Vấn đề
# ds	Không biết là danh sách gì
# p	Không biết là đối tượng nào
# t	Không rõ tên tuyển thủ
# m	Không rõ số trận hay MMR
# r	Không rõ dữ liệu gì
# b	Không rõ tiền thưởng
# Nên đổi thành
# Tên cũ	Tên mới
# ds	player_records
# p	record
# t	name
# m	matches
# r	mmr
# b	bonus

# Ví dụ:

# for record in player_records:
#     name = record[0]
#     matches = record[1]
#     mmr = record[2]

# Code trở nên dễ đọc và tự giải thích ý nghĩa (Self-documenting Code).


player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]


def calculate_bonus(matches, mmr):
    """
    Tính tiền thưởng RP theo công thức:
    Bonus RP = (Matches * 10) + (MMR * 0.5)
    """
    return (matches * 10) + (mmr * 0.5)


def process_bonus(player_records):
    """
    Duyệt danh sách tuyển thủ
    và xử lý các lỗi dữ liệu.
    """
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:

        name = record[0]

        try:
            matches = record[1]
            mmr = record[2]

            mmr = int(mmr)

            bonus = calculate_bonus(
                matches,
                mmr
            )

            print(
                f"Tuyển thủ {name} nhận được {bonus} RP"
            )

        except IndexError:
            print(
                f"Tuyển thủ {name}: Lỗi - Hồ sơ bị thiếu thông tin!"
            )
            continue

        except ValueError:
            print(
                f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!"
            )
            continue

    print("--- HOÀN TẤT ---")


process_bonus(player_records)