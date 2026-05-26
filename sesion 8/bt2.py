# Input

# Người dùng thao tác qua menu CLI.

# Dữ liệu	Kiểu dữ liệu
# menu_choice	string
# shop_name	string
# product_name	string
# product_description	string
# category	string
# keyword_list	string
# discount_code	string
# search_keyword	string
# replace_keyword	string
# Output

# Hệ thống hiển thị:

# Báo cáo thống kê sản phẩm
# Tên shop chuẩn hóa
# Kiểm tra mã giảm giá hợp lệ
# Kết quả tìm kiếm/thay thế từ khóa
# Thông báo lỗi edge case
# Thông báo thoát chương trình

# Các phương thức String sử dụng
# Method	Công dụng
# strip()	Xóa khoảng trắng
# title()	Viết hoa chữ cái đầu
# lower()	Chuyển chữ thường
# upper()	Chuyển chữ hoa
# split()	Tách chuỗi
# join()	Nối chuỗi
# replace()	Thay thế
# count()	Đếm từ khóa
# startswith()	Kiểm tra chuỗi bắt đầu
# isupper()	Kiểm tra viết hoa
# isalnum()	Kiểm tra chữ+số
# isdigit()	Kiểm tra số

# Tên shop

# Nếu:

# shop_name.strip()==""

# → Báo:

# Tên shop không được bỏ trống
# Mô tả sản phẩm

# Nếu:

# product_description.strip()==""

# → Báo:

# Mô tả sản phẩm không được rỗng
# Menu

# Kiểm tra:

# là số
# thuộc [1–5]
# Mã giảm giá

# Điều kiện:

# ✔ không rỗng

# ✔ không chứa khoảng trắng

# ✔ dài 6→12 ký tự

# ✔ viết hoa toàn bộ

# ✔ chỉ gồm chữ + số

# ✔ bắt đầu bằng SALE 



shop_name = ""
product_name = ""
product_description = ""
category = ""

keyword_list = []
discount_code_list = []

while True:

    print("""
========= MENU =========
1. Nhập dữ liệu sản phẩm
2. Chuẩn hóa tên shop
3. Kiểm tra mã giảm giá
4. Tìm kiếm & thay thế
5. Thoát
========================
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

        shop_name = input("Tên shop: ")
        product_name = input("Tên sản phẩm: ")
        product_description = input("Mô tả sản phẩm: ")
        category = input("Danh mục sản phẩm: ")
        keywords = input("Danh sách từ khóa: ")

        
        if shop_name.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        
        if product_description.strip() == "":
            print("Mô tả sản phẩm không được rỗng")
            continue

        shop_name = shop_name.strip()

        product_name = product_name.strip().title()

        product_description = product_description.strip()

        category = category.strip().lower()

    
        keyword_list = []

        for word in keywords.split(","):

            cleaned_word = word.strip()

            if cleaned_word != "":
                keyword_list.append(cleaned_word)

        
        description_length = len(product_description)

        print("\n===== BÁO CÁO =====")

        print("Tên shop:", shop_name)

        print("Tên sản phẩm:", product_name)

        print("Mô tả:", product_description)

        print("Độ dài mô tả:", description_length)

        print("Danh mục:", category)

        print("Danh sách từ khóa:", keyword_list)

        print("Số lượng từ khóa:", len(keyword_list))

        print("Mô tả chữ thường:")

        print(product_description.lower())

        print("Mô tả chữ hoa:")

        print(product_description.upper())


    elif menu_choice == 2:

        raw_shop = input("Nhập tên shop: ")

        if raw_shop.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        original_shop = raw_shop

        standardized_shop = raw_shop.strip().lower()

        standardized_shop = "-".join(
            standardized_shop.split()
        )

        if not standardized_shop.startswith("shop-"):

            standardized_shop = "shop-" + standardized_shop

        print("Tên shop ban đầu:")

        print(original_shop)

        print("Tên shop chuẩn hóa:")

        print(standardized_shop)



    elif menu_choice == 3:

        discount_code = input(
            "Nhập mã giảm giá: "
        ).strip()

        if discount_code == "":

            print("Mã giảm giá không được rỗng")

        elif " " in discount_code:

            print("Mã giảm giá không được chứa khoảng trắng")

        elif len(discount_code) < 6 or len(discount_code) > 12:

            print("Mã giảm giá phải từ 6-12 ký tự")

        elif not discount_code.isupper():

            print("Mã giảm giá phải viết hoa toàn bộ")

        elif not discount_code.isalnum():

            print("Mã giảm giá chỉ chứa chữ và số")

        elif not discount_code.startswith("SALE"):

            print("Mã giảm giá phải bắt đầu bằng SALE")

        else:

            print("Mã giảm giá hợp lệ")

            discount_code_list.append(
                discount_code
            )

            print(
                "Danh sách mã giảm giá:"
            )

            print(discount_code_list)



    elif menu_choice == 4:

        if product_description.strip() == "":

            print("Chưa có mô tả sản phẩm.")

            continue

        search_keyword = input(
            "Từ khóa cần tìm: "
        )

        replace_keyword = input(
            "Từ khóa thay thế: "
        )

        if search_keyword in product_description:

            total = product_description.count(
                search_keyword
            )

            new_description = (
                product_description.replace(
                    search_keyword,
                    replace_keyword
                )
            )

            print(
                "Số lần xuất hiện:",
                total
            )

            print(
                "Mô tả sau thay thế:"
            )

            print(new_description)

        else:

            print(
                "Không tìm thấy từ khóa."
            )

    elif menu_choice == 5:

        print("Thoát chương trình")

        break