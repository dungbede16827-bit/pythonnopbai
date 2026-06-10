# ZeroDivisionError: division by zero?

# Trong Python, phép chia cho 0 là không hợp lệ.

# Khi chương trình xử lý tuyển thủ ShowMaker:

# ("ShowMaker", "15", "0", "10")

# Sau khi ép kiểu:

# int(k) = 15
# int(d) = 0
# int(a) = 10

# Công thức KDA trở thành:

# (15 + 10) / 0

# Tức là:

# 25 / 0

# Python không thể thực hiện phép chia cho 0 nên phát sinh Exception:

# ZeroDivisionError: division by zero
# Dữ liệu của Chovy:

# ("Chovy", "12", "ba", "5")

# Khi thực hiện:

# int(d)

# tức là:

# int("ba")

# Python chỉ có thể chuyển chuỗi chứa số thành kiểu int.

# Ví dụ:

# int("3")   # Hợp lệ
# int("12")  # Hợp lệ

# Nhưng:

# int("ba")

# không thể chuyển đổi được.

# Do đó Python phát sinh:

# ValueError

# Thông báo đầy đủ thường là:

# ValueError: invalid literal for int() with base 10: 'ba'
    
#     ode cũ
# def tinh_toan(ds):
#     for x in ds:
#         n = x[0]
#         k = x[1]
#         d = x[2]
#         a = x[3]

# Các tên biến:

# Biến	Vấn đề
# ds	Không biết là danh sách gì
# x	Không biết đang đại diện cho dữ liệu nào
# n	Không rõ là tên gì
# k	Không rõ là số mạng hạ gục
# d	Không rõ là số lần chết
# a	Không rõ là số hỗ trợ

# Đây là ví dụ điển hình của Magic Variables làm code khó đọc.

# Nên đổi thành
# Tên cũ	Tên mới
# ds	player_stats
# x	player
# n	name
# k	kills
# d	deaths
# a	assists

# Ví dụ:

# for player in player_stats:
#     name = player[0]
#     kills = player[1]
#     deaths = player[2]
#     assists = player[3]

# Người đọc không cần xem comment vẫn hiểu ý nghĩa code.



player_stats = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]


def calculate_kda(kills, deaths, assists):
    """
    Tính chỉ số KDA theo công thức:
    KDA = (Kills + Assists) / Deaths
    """
    return (kills + assists) / deaths


def display_kda_ranking(player_stats):
    """
    Hiển thị bảng xếp hạng KDA
    và xử lý các ngoại lệ phát sinh.
    """
    print("--- BẢNG XẾP HẠNG KDA ---")

    for player in player_stats:
        name = player[0]
        kills = player[1]
        deaths = player[2]
        assists = player[3]

        try:
            kills = int(kills)
            deaths = int(deaths)
            assists = int(assists)

            kda = calculate_kda(
                kills,
                deaths,
                assists
            )

            print(
                f"Tuyển thủ {name} có chỉ số KDA là: {kda}"
            )

        except ZeroDivisionError:
            print(
                f"Tuyển thủ {name}: KDA Hoàn hảo (Perfect Game)!"
            )
            continue

        except ValueError:
            print(
                f"Tuyển thủ {name}: Lỗi dữ liệu không hợp lệ!"
            )
            continue

    print("--- HOÀN TẤT ---")


display_kda_ranking(player_stats)