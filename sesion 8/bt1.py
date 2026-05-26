# Dữ liệu	Kiểu  dữ liệu	Mô tả
# menu_choice	string	lựa chọn menu
# username	string	tên tài khoản TikTok
# video_title	string	tiêu đề video
# video_description	string	mô tả video
# hashtags	string	hashtag cách nhau dấu phẩy
# keyword	string	từ khóa cần tìm
# replace_keyword	string	từ thay thế
# hashtag_check	string	hashtag cần kiểm tra
# Output

# Chương trình hiển thị:

# Báo cáo thống kê video
# Username chuẩn hóa
# Kiểm tra hashtag hợp lệ / không hợp lệ
# Kết quả tìm kiếm & thay thế từ khóa
# Thông báo lỗi Edge Cases
# Thông báo thoát chương trình
# 2. Đề xuất giải pháp
# Các phương thức String sử dụng
# Method	Mục đích
# strip()	xóa khoảng trắng
# title()	viết hoa chữ cái đầu
# lower()	chuyển chữ thường
# upper()	chuyển chữ hoa
# split()	tách chuỗi
# join()	nối chuỗi
# replace()	thay thế
# count()	đếm từ khóa
# startswith()	kiểm tra ký tự đầu
# isdigit()	kiểm tra số
# isalnum()	kiểm tra chữ/số
# Kiểm tra dữ liệu hợp lệ
# Username

# Nếu:
# username.strip() == ""
#  Báo lỗi.

# Mô tả video

# Nếu:
# description.strip()==""
#  Không thống kê.

# Menu

# Kiểm tra:

# phải là số
# nằm trong khoảng 1→5
# Hashtag hợp lệ

# Điều kiện:

# không rỗng

# bắt đầu bằng #

#  không chứa khoảng trắng

# tối thiểu 2 ký tự

# sau # chỉ chứa:
# chữ cái
# số
# dấu _

username = ""
video_title = ""
video_description = ""
hashtag_list = []

while True:

    print("""
===== HỆ THỐNG TIKTOK =====
1. Nhập dữ liệu & thống kê
2. Chuẩn hóa tài khoản
3. Kiểm tra hashtag
4. Tìm kiếm & thay thế
5. Thoát
""")

    menu_choice = input("Nhập lựa chọn: ").strip()

    
    if not menu_choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    menu_choice = int(menu_choice)

    
    if menu_choice < 1 or menu_choice > 5:
        print("Lựa chọn không hợp lệ!")
        continue



    if menu_choice == 1:

        username = input("Tên tài khoản: ")
        video_title = input("Tiêu đề video: ")
        video_description = input("Mô tả video: ")
        hashtags = input("Hashtag (cách nhau dấu phẩy): ")

        
        if username.strip() == "":
            print("Tên tài khoản không được rỗng")
            continue

        
        username = username.strip()

        video_title = video_title.strip().title()

        
        if video_description.strip() == "":
            print("Mô tả video không được rỗng")
            continue

        video_description = video_description.strip()

        
        hashtag_list = []

        for tag in hashtags.split(","):
            cleaned_tag = tag.strip()

            if cleaned_tag != "":
                hashtag_list.append(cleaned_tag)

        
        description_length = len(video_description)

        word_count = len(video_description.split())

        print("\n===== BÁO CÁO =====")

        print("Username:", username)

        print("Tiêu đề:", video_title)

        print("Mô tả:", video_description)

        print("Độ dài mô tả:", description_length)

        print("Số từ:", word_count)

        print("Danh sách hashtag:", hashtag_list)

        print("Số lượng hashtag:", len(hashtag_list))

        print("Mô tả chữ thường:")

        print(video_description.lower())

        print("Mô tả chữ hoa:")

        print(video_description.upper())

    

    elif menu_choice == 2:

        account = input("Nhập tài khoản: ")

        if account.strip() == "":
            print("Tên tài khoản không được rỗng")
            continue

        original_account = account

        account = "@" + account.strip().lower()

        print("Ban đầu:", original_account)

        print("Chuẩn hóa:", account)

  

    elif menu_choice == 3:

        hashtag = input("Nhập hashtag: ").strip()

        if hashtag == "":
            print("Hashtag không được rỗng")

        elif not hashtag.startswith("#"):
            print("Hashtag phải bắt đầu bằng #")

        elif " " in hashtag:
            print("Hashtag không được chứa khoảng trắng")

        elif len(hashtag) < 2:
            print("Hashtag phải có ít nhất 2 ký tự")

        else:

            valid = True

            for char in hashtag[1:]:

                if not (char.isalnum() or char == "_"):
                    valid = False
                    break

            if valid:

                print("Hashtag hợp lệ")

                hashtag_list.append(hashtag)

                print("Đã thêm vào danh sách.")

            else:

                print("Hashtag chỉ được chứa chữ, số hoặc _")


    elif menu_choice == 4:

        if video_description.strip() == "":
            print("Chưa có mô tả video.")
            continue

        keyword = input("Từ khóa cần tìm: ")

        replace_keyword = input("Từ khóa thay thế: ")

        if keyword in video_description:

            count_keyword = video_description.count(keyword)

            new_description = video_description.replace(
                keyword,
                replace_keyword
            )

            print("Mô tả mới:")

            print(new_description)

            print("Số lần xuất hiện:", count_keyword)

        else:

            print("Không tìm thấy từ khóa.")

  
    elif menu_choice == 5:

        print("Thoát chương trình")

        break